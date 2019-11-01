import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
from tqdm import tqdm
import traceback
from operator import add
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
handRanges = [hr1,hr2,hr3]
# op_hr = hr1
f=open("guru108.txt","a+")
f.write("  NoPair  OnePair TwoPair Trips Straight  Flush   FlHouse Quads   StFlush \n")
f.close()
for hr in handRanges:
    pairs = []
    for i in range(len(hr)):
        # for j in range(len(op_hr)):
            first = str(hr.hands[i][0][0])
            second = str(hr.hands[i][0][1])
            # third = str(op_hr.hands[j][0][0])
            # fourth = str(op_hr.hands[j][0][1])
            pairs.append((first+second))

    rb={}   ## River rainbow  # 685,464 => 2366
    for idx1,b1 in enumerate(rank1):
        for idx2, b2 in enumerate(rank2):
            for idx3, b3 in enumerate(rank3):
                for idx4, b4 in enumerate(rank4):
                    for idx5, b5 in enumerate(rank4):
                        if idx4<idx5:

                            if idx1<idx2<idx3<idx4<idx5:  # 1287
                                # pass
                                rb[(b1+b2+b3+b4+b5)]=240
                                '''
                                Range vs Range
                                [QQ, AQs,AQo]
                                board = AsBdCh, AdBsCh

                                '''
                            if idx1==idx2<idx3<idx4<idx5:  # 715
                                # pass
                                rb[(b1+b2+b3+b4+b5)]=432
                            if idx1==idx2==idx3<idx4<idx5:  #286  orderShape = 1+3+1/2+2+1
                                # pass
                                rb[(b1+b2+b3+b4+b5)]=228
                            if idx1==idx2==idx3==idx4<idx5:  #78   orderShape = 4+1/2+3
                                # pass
                                rb[(b1+b2+b3+b4+b5)]=32
                        # if idx1==idx2==idx3==idx4==idx5:  #
                        #     # pass
                        #     rb[(b1+b2+b3+b4+b5)]=0


    groups = {}
    pprint(len(rb))
    for pair in pairs:
        for bd in rb:
            groups[(pair+bd)]=rb[bd]
    # pprint(groups)
    # print(len(groups))
    # print(len(pairs),len(rb))
     # 'TsThTsThThTdTc': 1}

    NoPair=OnePair=TwoPair=Trips=Straight=Flush=Quads=StFlush=0

    def try_my_operation(group):
            try:
                # pass
                array = [group[i:i+2] for i in range(0, len(group), 2)]
                '''
                test for cards duplication
                '''
                if len(array) != len(set(array)) :
                    # f.close()
                    return None
                # print(array)
                fc = groups[group]
                # me = array[:2]
                # # op = array[2:4]
                # board = array[2:]

                best_hand = pokereval.best_hand("hi", array)
                # print(best_hand[0], groups[group])
                # print(best_hand[0], pokereval.card2string(best_hand[1:]))
                # print(best_hand[0])
                '''
                    Nothing (only if "side" equals "low")
                    NoPair
                    OnePair
                    TwoPair
                    Trips
                    Straight
                    Flush
                    FlHouse
                    Quads
                    StFlush
                '''
                if best_hand[0] == 'NoPair':
                    result = [fc,0,0,0,0,0,0,0,0]
                elif best_hand[0] == 'OnePair':
                    result = [0,fc,0,0,0,0,0,0,0]
                elif best_hand[0] == 'TwoPair':
                    result = [0,0,fc,0,0,0,0,0,0]
                elif best_hand[0] == 'Trips':
                    result = [0,0,0,fc,0,0,0,0,0]
                elif best_hand[0] == 'Straight':
                    result = [0,0,0,0,fc,0,0,0,0]
                elif best_hand[0] == 'Flush':
                    result = [0,0,0,0,0,fc,0,0,0]
                elif best_hand[0] == 'FlHouse':
                    result = [0,0,0,0,0,0,fc,0,0]
                elif best_hand[0] == 'Quads':
                    result = [0,0,0,0,0,0,0,fc,0]
                else:                #'StFlush'
                    result = [0,0,0,0,0,0,0,0,fc]
                return result

                # # f=open("guru100.txt","a+")
                # result = pokereval.poker_eval(game='holdem', pockets=[me, op], board=board)
                # #pprint(result['eval'][0]['scoop'])
                # #pprint(result['info'][0])
                # scoop = result['eval'][0]['scoop']*fc
                # tie = result['eval'][0]['tiehi']*fc
                # total = result['info'][0]*fc
                # # f.write("%s %s %s %s\n " %  (group,scoop,tie,total))
                # # f.close()
                # return (scoop,tie,total)
            except Exception as e:
                print('Caught exception in worker thread %s' % group)

                # This prints the type, value, and stack trace of the
                # current exception being handled.
                traceback.print_exc()
                print()

                raise e

    # futures = [executor.submit(try_my_operation, group) for group in groups]
    # concurrent.futures.wait(futures)
    result=newResult=[0,0,0,0,0,0,0,0,0]
    for group in tqdm(groups):
        if try_my_operation(group) != None:
            result = list( map(add, result, try_my_operation(group)))
            # print(result,group)


    # print(result)
    total=0
    for i in result:
        total += i

    newResult=[result[i]*1.0/total for i in range(len(result))]
    f=open("guru108.txt","a+")
    # f.write("NoPair OnePair TwoPair Trips Straight Flush FlHouse Quads StFlush \n")
    f.write("%7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f \n" % (newResult[0],newResult[1],newResult[2],newResult[3],newResult[4],newResult[5],newResult[6],newResult[7],newResult[8]))
    f.close()
    # print("NoPair=%.3f, OnePair=%.3f, TwoPair=%.3f, Trips=%.3f, \n Straight=%.3f, Flush=%.3f, FlHouse=%.3f, Quads=%.3f,StFlush=%.3f" %  \
    # (newResult[0],newResult[1],newResult[2],newResult[3],newResult[4],newResult[5],newResult[6],newResult[7],newResult[8]))



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
rainbow   78comb vs 78 comb       1371.85s
threeColor78comb vs 78 comb       1314.13s
twoColor  78comb vs 78 comb       38min*60=2280s
oneColor  78comb vs 78 comb

full river: 52*51*50*49*48/120 = 2,598,960
rainbow:    (4 shape)*(13**3)*C2,13 = 685,464    26.4%
threeColor: C3,4*[C2,13*C2,13*C1,13*(3 shape) + C3,13*C1,13*C1,13*(3 shape)] = 509,704*3 = 1,529,112  58.8%
twoColor:   C2,4*[C1,13*C4,13*(2 shape) + C2,13*C3,13*(2 shape)]= 189,613*2 = 379,236  14.6%
oneColor:   C1,4*C5,13 = 1287*4 = 5148  0.2%
'''