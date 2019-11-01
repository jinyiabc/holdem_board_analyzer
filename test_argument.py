
import sys

# print("Number of arguments: %d" % len(arg))
# print ('Argument list: %s' % str(arg))

'''
usage:
 python test_argument.py as asis
 Argument list: ['test_argument.py', 'as', 'asis']

'''

def scope(arg):
    rank1 = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
    rank2 = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
    rank3 = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
    rank4 = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]
    if arg[1] =="flop":
        if arg[2] == 'one':
            rank=[rank1,rank1,rank1]
        elif arg[2] == 'two':
            rank=[rank1,rank1,rank2]
        elif arg[2] == 'three':
            rank=[rank1,rank2,rank3]
        # elif arg[2] == 'four':
        #     rank=[rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    elif arg[1] =="turn":
        if arg[2] == 'one':
            rank=[rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1]
        elif arg[2] == 'two':
            rank=[rank1,rank1,rank2,rank2,rank1,rank1,rank1,rank2]
        elif arg[2] == 'three':
            rank=[rank1,rank2,rank3,rank3,rank1,rank1,rank1,rank1]
        elif arg[2] == 'four':
            rank=[rank1,rank2,rank3,rank4,rank1,rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    elif arg[1] =="river":
        if arg[2] == 'one':
            rank=[rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1,rank1]
        elif arg[2] == 'two':
            rank=[rank1,rank1,rank2,rank2,rank2,rank1,rank1,rank1,rank1,rank2]
        elif arg[2] == 'three':
            rank=[rank1,rank2,rank3,rank3,rank3,rank1,rank1,rank2,rank2,rank3]
        elif arg[2] == 'four':
            rank=[rank1,rank2,rank3,rank4,rank4,rank1,rank1,rank1,rank1,rank1]
        else:
            print("The 2nd argument for color is not correct.Please retype: ")
            quit()
    else:
        print("The 1st argument for board type is not correct.Please retype: ")
        quit()

    scope=0
    if arg[3] == '6':
        scope=5
    elif arg[3] == '7':
        scope=6
    elif arg[3] == '8':
        scope=7
    elif arg[3] == '9':
        scope=8
    elif arg[3] == 'T':
        scope=9
    elif arg[3] == 'J':
        scope=10
    elif arg[3] == 'Q':
        scope=11
    elif arg[3] == 'K':
        scope=12
    else:
        scope=13
        # print("The 2st argument for range is not correct.Please retype: ")
        # quit()
    if len(rank)==3:
        new_rank1=rank[0][:scope]
        new_rank2=rank[1][:scope]
        new_rank3=rank[2][:scope]
        return (new_rank1,new_rank2,new_rank3)
    if len(rank)==8:
        new_rank1=rank[0][:scope]
        new_rank2=rank[1][:scope]
        new_rank3=rank[2][:scope]
        new_rank4=rank[3][:scope]
        new_rank5=rank[4][:scope]
        new_rank6=rank[5][:scope]
        new_rank7=rank[6][:scope]
        new_rank8=rank[7][:scope]
        return (new_rank1,new_rank2,new_rank3,new_rank4, \
                new_rank5,new_rank6,new_rank7,new_rank8)
    if len(rank)==10:
        new_rank1=rank[0][:scope]
        new_rank2=rank[1][:scope]
        new_rank3=rank[2][:scope]
        new_rank4=rank[3][:scope]
        new_rank5=rank[4][:scope]
        new_rank6=rank[5][:scope]
        new_rank7=rank[6][:scope]
        new_rank8=rank[7][:scope]
        new_rank1=rank[8][:scope]
        new_rank2=rank[9][:scope]
        return (new_rank1,new_rank2,new_rank3,new_rank4, \
                new_rank5,new_rank6,new_rank7,new_rank8,new_rank9,new_rank10)


def main():
    rank_list = scope(sys.argv)
    if len(rank_list) == 3:
        for idx1,b1 in enumerate(rank_list[0]):  # 1014 *12 = 12168
            for idx2, b2 in enumerate(rank_list[1]):
                for idx3, b3 in enumerate(rank_list[2]):
                    print(idx1, idx2,idx3)
                    print(b1, b2, b3)
    if len(rank_list)==8:
        pass
    if len(rank_list)==10:
        pass



if __name__ == "__main__":
    main()
