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
rank_list=[rank1[3:12],rank2[3:12],rank3[3:12]]
# rank_list=[rank1,rank2,rank3]


# f=open("guru103.txt","a+")
# f.write("  NoPair  OnePair TwoPair Trips Straight  Flush   FlHouse Quads   StFlush \n")
# f.close()

def try_my_operation(group,fc):
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
def handRange_remove_dead(rb, hr, dead_cards):
    pairs = {}
    for i in range(len(hr)):
        first = str(hr.hands[i][0][0])
        second = str(hr.hands[i][0][1])
        if dead_cards[0] == '' or dead_cards[1] == '':
            pairs[first+second]=1
            continue
        if dead_cards[0][0] == dead_cards[1][0]:

            '''
            A=B=a=b
            '''
            if first[0] == dead_cards[0][0] and second[0] == dead_cards[0][0]:
                pairs[first+second]=1.0/6
                '''
                A==a,B!=a
                A!=a,B==a
                '''
            elif first[0] == dead_cards[0][0] and second[0] != dead_cards[0][0] :
                pairs[first+second]=3.0/4
            elif first[0] != dead_cards[0][0] and second[0] == dead_cards[0][0] :
                pairs[first+second]=3.0/4
            else:
                pairs[first+second]=1

        if dead_cards[0][0] != dead_cards[1][0]:
            '''
            A=B=a or A=B=b
            '''
            if (first[0]==second[0]==dead_cards[0][0]) or (first[0]==second[0]==dead_cards[1][0]) :
                pairs[first+second]=1.0/2

                '''
                (A==a, A!=b, B!=a, B!=b)
                (A==b, A!=a, B!=a, B!=b)
                '''
            elif (first[0]==dead_cards[0][0] and second[0]!=dead_cards[0][0]) and \
                 (first[0]!=dead_cards[1][0] and second[0]!=dead_cards[1][0]) :
                pairs[first+second]=3.0/4
            elif (first[0]==dead_cards[1][0] and second[0]!=dead_cards[0][0]) and \
                 (first[0]!=dead_cards[0][0] and second[0]!=dead_cards[1][0]) :
                pairs[first+second]=3.0/4
                '''
                (A!=a, A!=b, B==a, B!=b)
                (A!=a, A!=b, B==b, B!=a)
                '''

            elif (first[0]!=dead_cards[0][0] and second[0]==dead_cards[0][0]) and \
                 (first[0]!=dead_cards[1][0] and second[0]!=dead_cards[1][0]) :
                pairs[first+second]=3.0/4
            elif (first[0]!=dead_cards[0][0] and second[0]==dead_cards[1][0]) and \
                 (first[0]!=dead_cards[1][0] and second[0]!=dead_cards[0][0]) :
                pairs[first+second]=3.0/4
                '''
                (A==a, B==b)
                (A==b, B==a)
                '''
            elif (first[0]==dead_cards[0][0] and second[0]==dead_cards[1][0]) or \
                 (first[0]==dead_cards[1][0] and second[0]==dead_cards[0][0]) :
                pairs[first+second]=9.0/16
            else:
                pairs[first+second]=1

    # pprint(pairs)
    # groups = {}
    # pprint(len(rb))
    # for pair in pairs:
    #     for bd in rb:
    #         groups[(pair+bd)]=rb[bd]*pairs[pair]
    pprint(pairs)
    return pairs
def list_group_card_flop3(handRanges,rank_list,dead_cards):
    list=[]
    for hr in handRanges:
        rb={}   ## rainbow
        for idx1,b1 in enumerate(rank_list[0]):  # (2197->455)
            for idx2, b2 in enumerate(rank_list[1]):
                for idx3, b3 in enumerate(rank_list[2]):
                    if idx1<idx2<idx3:
                        # pass
                        rb[(b1+b2+b3)]=6
                        '''
                        Range vs Range
                        [QQ, AQs,AQo]
                        board = AsBdCh, AdBsCh

                        '''
                    if idx1==idx2 and idx2<idx3:
                        # pass
                        rb[(b1+b2+b3)]=3
                    if idx1<idx2 and idx2==idx3:
                        # pass
                        rb[(b1+b2+b3)]=3
                    if idx1==idx2==idx3:
                        # pass
                        rb[(b1+b2+b3)]=1
        pairs = handRange_remove_dead(rb, hr, dead_cards)

        groups = {}
        pprint(len(rb))
        for pair in pairs:
            for bd in rb:
                groups[(pair+bd)]=rb[bd]
        # pprint(groups)
        # print(len(groups))
        # print(len(pairs),len(rb))
         # 'TsThTsThThTdTc': 1}

        list.append(groups)

    return list

def main():
    dead_cards = ['', '']
    list_groups = list_group_card_flop3(handRanges,rank_list,dead_cards)
    for groups in list_groups:

        NoPair=OnePair=TwoPair=Trips=Straight=Flush=Quads=StFlush=0
        result=newResult=[0,0,0,0,0,0,0,0,0]
        for group in tqdm(groups):
            fc = groups[group]
            if try_my_operation(group, fc) != None:
                result = list( map(add, result, try_my_operation(group, fc)))
                # print(result,group)

        # print("Equity: %18.9f " % ((scoop+tie*1.0/2)*1.0/total))
        # print("total game: %s" % total)              # 990* 455 = 450450  990*2041 = 2,020,590 (13*13*13=2197, A<=B<=C A=C<B(78) and A=C>B (78)excluded)
        # # print("iteration: %s" % fre)  # 2197 => 546
        # print(result)
        total=0
        for i in result:
            total += i

        newResult=[result[i]*1.0/total for i in range(len(result))]
        f=open("guru103.txt","a+")
        # f.write("NoPair OnePair TwoPair Trips Straight Flush FlHouse Quads StFlush \n")
        f.write("%7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f %7.3f \n" % (newResult[0],newResult[1],newResult[2],newResult[3],newResult[4],newResult[5],newResult[6],newResult[7],newResult[8]))
        f.close()
        # print("NoPair=%.3f, OnePair=%.3f, TwoPair=%.3f, Trips=%.3f, \n Straight=%.3f, Flush=%.3f, FlHouse=%.3f, Quads=%.3f,StFlush=%.3f" %  \
        # (newResult[0],newResult[1],newResult[2],newResult[3],newResult[4],newResult[5],newResult[6],newResult[7],newResult[8]))

if __name__ == "__main__":
    main()

'''
 full flop: 52*51*50/6 = 22,100
 rainbow : 2197(given three color) * 4 (C1,4) = 8788  39%
 TwoColor: 2*(13*12/2)*13* 6 (C2,4) = 12168  55%
 OneColor: 13*12*11/6 * 4 (C1,4) = 1144 5.2%

'''

'''
          Range vs Range          Time
rainbow   78comb vs 78 comb       355.97s
twoColor  78comb vs 78 comb       785.69s
oneColor  78comb vs 78 comb       221.97s
'''
