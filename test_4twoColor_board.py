import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
from tqdm import tqdm
pokereval = PokerEval()
# import a new API to create a thread pool
# from concurrent.futures import ThreadPoolExecutor as PoolExecutor   #real	1m11.866s
from concurrent.futures import ProcessPoolExecutor as PoolExecutor    #real	0m32.562s
import concurrent.futures
# create a thread pool of 4 threads
executor = PoolExecutor(max_workers=4)

'''
 full flop: 52*51*50/6 = 22,100
 rainbow : 2197(given three color) * 4 (C1,4) = 8788  39%
 TwoColor: 2*(13*12/2)*13* 6 (C2,4) = 12168  55%
 OneColor: 13*12*11/6 * 4 (C1,4) = 1144 5.2%

'''

# hr1 3-bet for value
# hr2 3-bet for lesser value
# hr3 for call

hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
64s, 75s, 86s, 97s, T8s, J9s")

rank1 = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
rank2 = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
rank3 = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
rank4 = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]

# hr = eval7.HandRange("AsKs")
# hand vs hand 0.08s  total game: 1979010
# range vs range 78*6 15s total game: 585293940  78*78  0:03:39.749825
hr = hr1
op_hr = hr1
scoop=total=tie=0

pairs = []
for i in range(len(hr)):
    for j in range(len(op_hr)):
        first = str(hr.hands[i][0][0])
        second = str(hr.hands[i][0][1])
        third = str(op_hr.hands[j][0][0])
        fourth = str(op_hr.hands[j][0][1])
        pairs.append((first+second+third+fourth))

rb={}   ## turn twoColor  # 81,120 =>3224
for idx1,b1 in enumerate(rank1):
    for idx2, b2 in enumerate(rank1):
        for idx3, b3 in enumerate(rank2):
            for idx4, b4 in enumerate(rank2):

                if idx1<idx2<idx3<idx4:  # 715
                    # pass
                    rb[(b1+b2+b3+b4)]=36
                    '''
                    Range vs Range
                    [QQ, AQs,AQo]
                    board = AsBdCh, AdBsCh

                    '''
                if idx1==idx3<idx2<idx4:  #286
                    # pass
                    rb[(b1+b3+b2+b4)]=12
                if idx1<idx2==idx3<idx4:  # 286
                    # pass
                    rb[(b1+b2+b3+b4)]=12
                if idx1<idx3<idx2==idx4:  # 286
                    # pass
                    rb[(b1+b3+b2+b4)]=12
                # if idx1==idx2==idx3<idx4:  #78
                #     # pass
                #     rb[(b1+b2+b3+b4)]=0
                # if idx3<idx4==idx1==idx2:  #78
                #     # pass
                #     rb[(b3+b4+b1+b2)]=0
                if idx1==idx3<idx2==idx4:  #78
                    # pass
                    rb[(b1+b3+b2+b4)]=6
                # if idx1==idx2==idx3==idx4:  #13
                #     # pass
                #     rb[(b1+b2+b3+b4)]=0
for idx1,b1 in enumerate(rank1):
    for idx2, b2 in enumerate(rank1):
        for idx3, b3 in enumerate(rank1):
            for idx4, b4 in enumerate(rank2):
                if idx1<idx2<idx3<idx4:  # 715
                    # pass
                    rb[(b1+b2+b3+b4)]=48
                    '''
                    Range vs Range
                    [QQ, AQs,AQo]
                    board = AsBdCh, AdBsCh

                    '''
                if idx1==idx4<idx2<idx3:  # 286
                    # pass
                    rb[(b1+b4+b2+b3)]=12
                if idx1<idx2==idx4<idx3:  # 286
                    # pass
                    rb[(b1+b2+b4+b3)]=12
                if idx1<idx2<idx3==idx4:  # 286
                    # pass
                    rb[(b1+b2+b3+b4)]=12

# pprint(rb)
# print(len(rb))

for i in rb.values():
    total +=i
print(total) # 158,184

groups = {}
pprint(len(rb))
for pair in pairs:
    for bd in rb:
        groups[(pair+bd)]=rb[bd]
# pprint(groups)
# print(len(groups))
# print(len(pairs),len(rb))
 # 'TsThTsThThTdTc': 1}



#XXX rainbow ascend repeat
# Multi-Processing
def try_my_operation(group):
        try:
            array = [group[i:i+2] for i in range(0, len(group), 2)]
            '''
            test for cards duplication
            '''
            if len(array) != len(set(array)) :
                # f.close()
                return None
            # print(array)
            fc = groups[group]
            me = array[:2]
            op = array[2:4]
            board = [array[4], array[5], array[6], array[7], '__']
            # print(group)
            # print(me , op)
            # print(board)

            # f=open("guru100.txt","a+")
            result = pokereval.poker_eval(game='holdem', pockets=[me, op], board=board)
            #pprint(result['eval'][0]['scoop'])
            #pprint(result['info'][0])
            scoop = result['eval'][0]['scoop']*fc
            tie = result['eval'][0]['tiehi']*fc
            total = result['info'][0]*fc
            # f.write("%s %s %s %s\n " %  (group,scoop,tie,total))
            # f.close()
            return (scoop,tie,total)
        except Exception as e:
            print('Caught exception in worker thread %s' % group)

            # This prints the type, value, and stack trace of the
            # current exception being handled.
            traceback.print_exc()
            print()

            raise e

# futures = [executor.submit(try_my_operation, group) for group in groups]
# concurrent.futures.wait(futures)

for group in tqdm(groups):
    if try_my_operation(group) != None:
        scoop1=tie1=total1 =0
        scoop1, tie1, total1 = try_my_operation(group)
        scoop+=scoop1; tie+=tie1; total+=total1
        # print(group,scoop,tie,total)

print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
print("total game: %s" % total)
# print("iteration: %s" % fre)

'''
 full flop: 52*51*50/6 = 22,100
 rainbow : 2197(given three color) * 4 (C1,4) = 8788  39%
 TwoColor: 2*(13*12/2)*13* 6 (C2,4) = 12168           55%
 OneColor: 13*12*11/6 * 4 (C1,4) = 1144               5.2%

 full turn: 52*51*50*49/24 = 270,725
 rainbow: 13**4 = 28,561                                      10.5%
 threeColor: C3,4 * C1,3 * (C1,13*C1,13*C2,13)  = 158,184     58.4%
 twoColor: C2,4 * (C2,13 *C2,13 + C1,2*C1,13*C3,13) = 81,120  30.0%
 OneColor: C1,4 * C4,13 = 2,860   1.1%
'''

'''
flop      Range vs Range          Time
rainbow   78comb vs 78 comb       355.97s
twoColor  78comb vs 78 comb       785.69s
oneColor  78comb vs 78 comb       221.97s

turn      Range vs Range          Time
rainbow   78comb vs 78 comb
threeColor78comb vs 78 comb       
twoColor  78comb vs 78 comb
oneColor  78comb vs 78 comb
'''
