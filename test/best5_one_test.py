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
# handRanges = [hr1,hr2,hr3]
# rank_list=[rank1,rank2,rank3]

# f=open("guru103.txt","a+")
# f.write("  NoPair  OnePair TwoPair Trips Straight  Flush   FlHouse Quads   StFlush \n")
# f.close()

def list_group_card_flop1(handRanges,rank_list):
    list=[]
    for hr in handRanges:
        pairs = []
        for i in range(len(hr)):
            # for j in range(len(op_hr)):
                first = str(hr.hands[i][0][0])
                second = str(hr.hands[i][0][1])
                pairs.append((first+second))

        rb={}   ## oneColor
        for idx1,b1 in enumerate(rank_list[0]):  # (2197->455)
            for idx2, b2 in enumerate(rank_list[1]):
                for idx3, b3 in enumerate(rank_list[2]):
                    if idx1<idx2<idx3:
                        # pass  # 858
                        rb[(b1+b2+b3)]=4
                        '''
                        Range vs Range
                        [QQ, AQs,AQo]
                        board = AsBdCh, AdBsCh

                        '''
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

def handRange_remove_dead(rb, hr, dead_cards):
    pairs = {}
    for i in range(len(hr)):
        first = str(hr.hands[i][0][0])
        second = str(hr.hands[i][0][1])
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
    groups = {}
    pprint(len(rb))
    for pair in pairs:
        for bd in rb:
            groups[(pair+bd)]=rb[bd]*pairs[pair]
    # pprint(groups)
    return groups

def main():
    rb={}   ## oneColor
    for idx1,b1 in enumerate(rank1):  # 286*4 = 1144
        for idx2, b2 in enumerate(rank2):
            for idx3, b3 in enumerate(rank3):
                if idx1<idx2<idx3:
                    # fre+=1
                    # pass  # 286(C3,13)
                    rb[(b1+b2+b3)]=1   # C1,4 for color
                    '''
                    Range vs Range
                    [QQ, AQs,AQo]
                    board = AsBdCh, AdBsCh

                    '''
    # print(fre)
    # pprint(rb)
    print("the number of board: %d" % len(rb))

    hr1 = eval7.HandRange("TT,TA")
    # pprint(hr1.hands)
    dead_cards = ['Td','Ad']
    groups = handRange_remove_dead(rb, hr1, dead_cards)
    pprint(groups)


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
