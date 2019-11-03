import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import traceback
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
from tqdm import tqdm
pokereval = PokerEval()

'''
 full flop: 52*51*50/6 = 22,100
 rainbow : 2197(given three color) * 4 (C1,4) = 8788  39%
 TwoColor: 2*(13*12/2)*13* 6 (C2,4) = 12168  55%
 OneColor: 13*12*11/6 * 4 (C1,4) = 1144 5.2%

'''
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
rank_list=[rank1,rank2,rank3]
def group_card_river2(hr, op_hr, rank_list):
    rb={}   ## River Two Color     iteration: 5005(3,2,0,0) + 2002(4,1,0,0)   => 2288 + 1435=3723
    for idx1,b1 in enumerate(rank_list[0]):
        for idx2, b2 in enumerate(rank_list[1]):
            for idx3, b3 in enumerate(rank_list[2]):
                for idx4, b4 in enumerate(rank_list[3]):
                    for idx5, b5 in enumerate(rank_list[4]):
                        '''
                        all     set&two noPair oneP fulHouse TwoPair
                        (22308, 0, 12870, 8580, 0, 858)
                        '''
                        if idx3<idx4<idx5 and idx1<idx2:

                            #total in (3,2,0,0)   22308 == C2,13*C3,13 =78*286=22308


                            #No Pair    #12870
                            if idx1<idx2<idx3<idx4<idx5:  # 1287 * 10(C2,5)
                                # pass
                                rb[(b1+b2+b3+b4+b5)]=12*10
                                # print(idx1,idx2,idx3,idx4,idx5)
                                '''
                                Range vs Range
                                [QQ, AQs,AQo]
                                board = AsBdCh, AdBsCh

                                '''

                            ## for one pair  = 8580 = 715*12(C1,4*)  iteration = 2860 = 715*4
                            if idx1==idx3<idx2<idx4<idx5:  # 715  # 1=3<4<5 => 2 can place 1=3<2<4<5,1=3<4<2<5,1=3<4<5<2
                                # pass
                                # print(idx1,idx3,idx2,idx4,idx5)
                                rb[(b1+b3+b2+b4+b5)]=12*3*4
                            # if idx1<idx3==idx2<idx4<idx5:
                            #     # pass
                            #     # print(idx1,idx3,idx2,idx4,idx5)
                            #     rb[(b1+b3+b2+b4+b5)]=12*3
                            # if idx1<idx3<idx2==idx4<idx5:
                            #     # pass
                            #     # print(idx1,idx3,idx2,idx4,idx5)
                            #     rb[(b1+b3+b2+b4+b5)]=12*3
                            # if idx3<idx1<idx4<idx2==idx5:
                            #     # pass
                            #     # print(idx1,idx3,idx2,idx4,idx5)
                            #     rb[(b3+b1+b4+b2+b5)]=12*3



                            ##For two paris  858
                            if idx1==idx3<idx2==idx4<idx5:  # 286
                                # pass
                                # print(idx1,idx3,idx2,idx4,idx5)
                                rb[(b1+b3+b2+b4+b5)]=12*3
                            # if idx1==idx3<idx4<idx2==idx5:
                            #     # pass
                            #     # print(idx1,idx3,idx2,idx4,idx5)
                            #     rb[(b1+b3+b4+b2+b5)]=12*1
                            # if idx3<idx1==idx4<idx2==idx5:
                            #     # pass
                            #     # print(idx1,idx3,idx2,idx4,idx5)
                            #     rb[(b3+b1+b4+b2+b5)]=12*1



    for idx1,b1 in enumerate(rank_list[5]):
        for idx2, b2 in enumerate(rank_list[6]):
            for idx3, b3 in enumerate(rank_list[7]):
                for idx4, b4 in enumerate(rank_list[8]):
                    for idx5, b5 in enumerate(rank_list[9]):
                        '''
                        all     set&two noPair oneP fulHouse
                        (9295, 0, 6435, 2860, 0, 0)
                        '''
                        if idx1<idx2<idx3<idx4:
                            # all = 9295 = C4,13*C1,13 = 715*13 =9295
                            # fre+=1
                            # print(idx1,idx2,idx3,idx4,idx5)

                            # No Pair  = 6435
                            if idx1<idx2<idx3<idx4<idx5:  # 6435 = C4,13*5  # for 5 = 5<1<2<3<4,1<5<2<3<4,1<2<5<3<4,1<2<3<5<4,1<2<3<4<5

                                # pass
                                rb[(b1+b2+b3+b4+b5)]= 12*5
                                # print(idx1,idx2,idx3,idx4,idx5)

                                '''
                                Range vs Range
                                [QQ, AQs,AQo]
                                board = AsBdCh, AdBsCh

                                '''

                            ## for one pair =2860
                            if idx1==idx5<idx2<idx3<idx4:  # 2860 = 715*4 => 1=5<2<3<4, 1<2=5<3<4, 1<2<3=5<4, 1<2<3<4=5
                                # pass
                                # print(idx1,idx3,idx2,idx4,idx5)
                                rb[(b1+b5+b2+b3+b4)]=12*4

    print("the number of board: %d" % len(rb))
    pairs = []
    for i in range(len(hr)):
        for j in range(len(op_hr)):
            first = str(hr.hands[i][0][0])
            second = str(hr.hands[i][0][1])
            third = str(op_hr.hands[j][0][0])
            fourth = str(op_hr.hands[j][0][1])
            pairs.append((first+second+third+fourth))
    groups = {}
    pprint(len(rb))
    for pair in pairs:
        for bd in rb:
            groups[(pair+bd)]=rb[bd]
    return groups


#XXX rainbow ascend repeat
# Multi-Processing
def try_my_operation(group,fc):
        try:
            array = [group[i:i+2] for i in range(0, len(group), 2)]
            '''
            test for cards duplication
            '''
            if len(array) != len(set(array)) :
                # f.close()
                return None
            # print(array)
            # fc = groups[group]
            me = array[:2]
            op = array[2:4]
            board = [array[4], array[5], array[6], '__', '__']
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

def main():

    groups = group_card_river2(hr, op_hr, rank_list)
    scoop=total=tie=0
    for group in tqdm(groups):
        fc = groups[group]
        if try_my_operation(group, fc) != None:
            scoop1=tie1=total1 =0
            scoop1, tie1, total1 = try_my_operation(group,fc)
            scoop+=scoop1; tie+=tie1; total+=total1
            # print(group,scoop,tie,total)

    print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
    print("total game: %s" % total)              # 990* 455 = 450450  990*2041 = 2,020,590 (13*13*13=2197, A<=B<=C A=C<B(78) and A=C>B (78)excluded)

if __name__ == "__main__":
    main()


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

 full river: 52*51*50*49*48/120 = 2,598,960
 rainbow:    (4 shape)*(13**3)*C2,13 = 685,464    26.4%
 threeColor: C3,4*[C2,13*C2,13*C1,13*(3 shape) + C3,13*C1,13*C1,13*(3 shape)] = 509,704*3 = 1,529,112  58.8%
 twoColor:   C2,4*[C1,13*C4,13*(2 shape) + C2,13*C3,13*(2 shape)]= 189,613*2 = 379,236  14.6%
 oneColor:   C1,4*C5,13 = 1287*4 = 5148  0.2%

'''

'''
flop      Range vs Range          Time
rainbow   78comb vs 78 comb       355.97s
twoColor  78comb vs 78 comb       785.69s
oneColor  78comb vs 78 comb       221.97s

turn      Range vs Range          Time
rainbow   78comb vs 78 comb       10min
threeColor78comb vs 78 comb       1314.13s
twoColor  78comb vs 78 comb       38min=2280s
oneColor  78comb vs 78 comb       8min=480s

river      Range vs Range      rb   Time
rainbow   78comb vs 78 comb    2366   2hour+
threeColor78comb vs 78 comb    11882
twoColor  78comb vs 78 comb    7007
oneColor  78comb vs 78 comb    1287  13min
'''
