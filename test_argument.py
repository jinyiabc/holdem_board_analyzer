
import sys
sys.path.insert(0, "./board")
from flop1 import group_card_flop1
from flop2 import group_card_flop2
from flop3 import group_card_flop3
from turn1 import group_card_turn1
from turn2 import group_card_turn2
from turn3 import group_card_turn3
from turn4 import group_card_turn4
from river1 import group_card_river1
from river2 import group_card_river2
from river3 import group_card_river3
from river4 import group_card_river4


import eval7
from tqdm import tqdm
import traceback
from pokereval import PokerEval
pokereval = PokerEval()

'''
usage:
 python test_argument.py str=flop color=one high=K low=5

str: flop or turn or river
color: one, two, three, four
low,high: 23456789TJQKA
'''

def scope(arg):
    rank1 = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
    rank2 = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
    rank3 = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
    rank4 = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]
    scope=12;scope0=0;low=1;high=13;
    for i in range(len(arg)):
        if 'high=' in arg[i]:
            # print(arg[i][5:])
            if arg[i][5:] == 'T':
                high=9; scope=9
            elif arg[i][5:] == 'J':
                high=10; scope=10
            elif arg[i][5:] == 'Q':
                high=11; scope=11
            elif arg[i][5:] == 'K':
                high=12; scope=12
            elif int(arg[i][5:]) == 6 or 7 or 8:
                high = int(arg[i][5:])-1; scope=high
            else:
                high=13; scope=12
        if 'low=' in arg[i]:
            if arg[i][4:] == 'T':
                low=9; scope0=8
            elif arg[i][4:] == 'J':
                low=10; scope0=9
            elif arg[i][4:] == 'Q':
                low=11; scope0=10
            elif arg[i][4:] == 'K':
                low=12; scope0=11
            elif int(arg[i][4:]) == 9 or 8 or 7:
                low = int(arg[i][4:])-1; scope0=low-1
            else:
                low=1; scope0=0

    # print("scope",scope)
    # print("scope0", scope0)
    # print(rank1[scope0], rank1[scope])
        if 'str=' in arg[i]:
            # print("str= %s" % arg[i][4:])
            str = arg[i][4:]
        if 'color=' in arg[i]:
            # print("color= %s" %arg[i][6:])
            color = arg[i][6:]

    if str=="flop":
        if color == 'one':
            rank=[rank1,rank1,rank1]
        elif color == 'two':
            rank=[rank1,rank1,rank2]
        elif color == 'three':
            rank=[rank1,rank2,rank3]
        # elif color == 'four':
        #     rank=[rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    elif str =="turn":
        if color == 'one':
            rank=[rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1]
        elif color == 'two':
            rank=[rank1,rank1,rank2,rank2,rank1,rank1,rank1,rank2]
        elif color == 'three':
            rank=[rank1,rank2,rank3,rank3,rank1,rank1,rank1,rank1]
        elif color == 'four':
            rank=[rank1,rank2,rank3,rank4,rank1,rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    elif str =="river":
        if color == 'one':
            rank=[rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1]
        elif color == 'two':
            rank=[rank1,rank1,rank2,rank2,rank2,rank1,rank1,rank1,rank1,rank2]
        elif color == 'three':
            rank=[rank1,rank2,rank3,rank3,rank3,rank1,rank1,rank2,rank2,rank3]
        elif color == 'four':
            rank=[rank1,rank2,rank3,rank4,rank4,rank1,rank1,rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    else:
        print("The 1st argument for board type is not correct.Please retype: ")
        quit()

        # print("The 2st argument for range is not correct.Please retype: ")
        # quit()
    if len(rank)==3:
        new_rank1=rank[0][scope0:scope]
        new_rank2=rank[1][scope0:scope]
        new_rank3=rank[2][scope0:scope]
        return (new_rank1,new_rank2,new_rank3)
    if len(rank)==8:
        new_rank1=rank[0][scope0:scope]
        new_rank2=rank[1][scope0:scope]
        new_rank3=rank[2][scope0:scope]
        new_rank4=rank[3][scope0:scope]
        new_rank5=rank[4][scope0:scope]
        new_rank6=rank[5][scope0:scope]
        new_rank7=rank[6][scope0:scope]
        new_rank8=rank[7][scope0:scope]
        return (new_rank1,new_rank2,new_rank3,new_rank4, \
                new_rank5,new_rank6,new_rank7,new_rank8)
    if len(rank)==10:
        new_rank1=rank[0][scope0:scope]
        new_rank2=rank[1][scope0:scope]
        new_rank3=rank[2][scope0:scope]
        new_rank4=rank[3][scope0:scope]
        new_rank5=rank[4][scope0:scope]
        new_rank6=rank[5][scope0:scope]
        new_rank7=rank[6][scope0:scope]
        new_rank8=rank[7][scope0:scope]
        new_rank9=rank[8][scope0:scope]
        new_rank10=rank[9][scope0:scope]
        return (new_rank1,new_rank2,new_rank3,new_rank4, \
                new_rank5,new_rank6,new_rank7,new_rank8,new_rank9,new_rank10)

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
    '''
    set up parameters required by the task
    '''
    hr1 = eval7.HandRange("TT+, AQ+, KQ+")  # 78 combo
    hr2 = eval7.HandRange("77+, A9+, KT+, QT+, JT, T9s, 98s, 87s, 76s, 65s")
    hr3 = eval7.HandRange("22+, A7o+, KT+, QT+, JT, T9, 98s, 87s, 76s, 65s, A2s+, K9s, K8s, Q9s, Q8s, \
    64s, 75s, 86s, 97s, T8s, J9s")

    hr = hr1
    op_hr = hr1

    '''
    pass the task function, followed by the parameters to processors
    '''
    rank_list = scope(sys.argv)
    if len(rank_list) == 3 and sys.argv[2][6:]=='one':
        groups = group_card_flop1(hr, op_hr, rank_list)
    if len(rank_list) == 3 and sys.argv[2][6:]=='two':
        groups = group_card_flop2(hr, op_hr, rank_list)
    if len(rank_list) == 3 and sys.argv[2][6:]=='three':
        groups = group_card_flop3(hr, op_hr, rank_list)


    if len(rank_list)==8 and sys.argv[2][6:]=='one':
        groups = group_card_turn1(hr, op_hr, rank_list)
    if len(rank_list)==8 and sys.argv[2][6:]=='two':
        groups = group_card_turn2(hr, op_hr, rank_list)
    if len(rank_list)==8 and sys.argv[2][6:]=='three':
        groups = group_card_turn3(hr, op_hr, rank_list)
    if len(rank_list)==8 and sys.argv[2][6:]=='four':
        groups = group_card_turn4(hr, op_hr, rank_list)

    if len(rank_list)==10 and sys.argv[2][6:] == 'one':
        groups = group_card_river1(hr, op_hr, rank_list)
    if len(rank_list)==10 and (sys.argv[2][6:] == 'two') :
        groups = group_card_river2(hr, op_hr, rank_list)
    if len(rank_list)==10 and (sys.argv[2][6:] == 'three') :
        groups = group_card_river3(hr, op_hr, rank_list)
    if len(rank_list)==10 and (sys.argv[2][6:] == 'four') :
        groups = group_card_river4(hr, op_hr, rank_list)

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
    print("Number of arguments: %d" % len(sys.argv))
    print ('Argument list: %s' % str(sys.argv))


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
rainbow   78comb vs 78 comb    2366   26min
threeColor78comb vs 78 comb    11882
twoColor  78comb vs 78 comb    7007
oneColor  78comb vs 78 comb    1287  13min
'''
