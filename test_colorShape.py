import eval7
# https://pypi.org/project/eval7/
from pprint import pprint
import sys
import datetime
sys.path.insert(0, ".")
sys.path.insert(0, ".libs")
from pokereval import PokerEval
pokereval = PokerEval()
from tqdm import tqdm
from operator import add


def colorShape5(n,m):
    '''
    n equals number of board cards.
    m equals the number of colors displayed in board.
    r1,r2,r3,r4,r5 represents rank class of board cards.
    '''
    fre=fre1=fre2=fre3=fre4=0
    for r1 in range(4):
        for r2 in range(4):
            for r3 in range(4):
                for r4 in range(4):
                    for r5 in range(4):
                        if r1==0:
                            b1 = [1,0,0,0]
                        elif r1==1:
                            b1 = [0,1,0,0]
                        elif r1==2:
                            b1 = [0,0,1,0]
                        else:
                            b1 = [0,0,0,1]

                        if r2==0:
                            b2 = [1,0,0,0]
                        elif r2==1:
                            b2 = [0,1,0,0]
                        elif r2==2:
                            b2 = [0,0,1,0]
                        else:
                            b2 = [0,0,0,1]

                        if r3==0:
                            b3 = [1,0,0,0]
                        elif r3==1:
                            b3 = [0,1,0,0]
                        elif r3==2:
                            b3 = [0,0,1,0]
                        else:
                            b3 = [0,0,0,1]

                        if r4==0:
                            b4 = [1,0,0,0]
                        elif r4==1:
                            b4 = [0,1,0,0]
                        elif r4==2:
                            b4 = [0,0,1,0]
                        else:
                            b4 = [0,0,0,1]

                        if r5==0:
                            b5 = [1,0,0,0]
                        elif r5==1:
                            b5 = [0,1,0,0]
                        elif r5==2:
                            b5 = [0,0,1,0]
                        else:
                            b5 = [0,0,0,1]

                        result=[0,0,0,0]
                        result = list( map(add, result, b1))
                        result = list( map(add, result, b2))
                        result = list( map(add, result, b3))
                        result = list( map(add, result, b4))
                        result = list( map(add, result, b5))
                        # if result.count(2) == 2 and result.count(1) == 1 and result.count(0) ==1: #   shape of [2, 2, 1, 0] three color #360
                        # if result.count(3) == 1 and result.count(1) == 2 and result.count(0) ==1:  #   shape of [3, 1, 1, 0] three color #240

                        # if result.count(3) == 1 and result.count(2) == 1:  #   shape of [3, 2, 0, 0] two color #120
                        # if result.count(2) == 1 and result.count(1) == 3:  #   shape of [2, 1, 1, 1] four color #120

                        if result.count(0) ==1:  #   shape of three color #600


                            # print(result,r1,r2,r3,r4,r5)

                            if r1!=r2: #
                                fre1=fre1+1
                                # print(result,r1,r2,r3,r4,r5)
                            if r1!=r3 and r2!=r4 :
                                fre2=fre2+1
                                print(result,r1,r2,r3,r4,r5)
                            if r1!=r2 and r1!=r3 and r2!=r3:  # three card do not have same color
                                fre3=fre3+1
                            if r1!=r2 and r1!=r3 and r2!=r3 and r4!=r5:
                                fre4=fre4+1
                                # print(result,r1,r2,r3,r4,r5)
                            fre=fre+1


    print(fre, fre1,fre2,fre3,fre4)


    '''
    onePair: two cards have different color

    (2,2,1,0) All, onep, twopair, set, fulhouse (360, 288, 240, 144, 144)
    (3,1,1,0) all, onep, twopair, set, fulhouse (240, 168, 96, 72, 0)

    sum threeColor                            (600, 456, 336, 216, 144)






    '''


colorShape5(4,5)







# rb={}
# for idx1,b1 in enumerate(rank1):  #949,104
#     for idx2, b2 in enumerate(rank1):
#         for idx3, b3 in enumerate(rank2):
#             for idx4, b4 in enumerate(rank2):
#                 for idx5, b5 in enumerate(rank3):
#                     if idx1==idx3<idx2<idx4<idx5:  # 715 orderShape = 2+2+1  (C2,5*C2,3/2 - 1*C2,3)*colorShape(6)*C3,4
#                         # pass
#                         rb[(b1+b3+b2+b4+b5)]=384
#
# pprint(rb)
# print(len(rb))
