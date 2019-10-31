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

rank1 = ["2h","3h","4h","5h","6h","7h","8h","9h","Th","Jh","Qh","Kh","Ah"]
rank2 = ["2d","3d","4d","5d","6d","7d","8d","9d","Td","Jd","Qd","Kd","Ad"]
rank3 = ["2c","3c","4c","5c","6c","7c","8c","9c","Tc","Jc","Qc","Kc","Ac"]
rank4 = ["2s","3s","4s","5s","6s","7s","8s","9s","Ts","Js","Qs","Ks","As"]
list = [0,1,2,3,4,5,6,7,8,9,10,11,12]
scoop=total=tie=fre=fre1=fre2=fre3=fre4=fre5=fre6=fre7=fre8=0


# rb={}   ## River rainbow  # Theory:1,529,112 ? (real: 2,572,440=>12038)
# for idx1,b1 in enumerate(rank1):  # (3,1,1,0)      # 48334= c3,13*C1,13*C1,13
#     for idx2, b2 in enumerate(rank2):
#         for idx3, b3 in enumerate(rank3):
#             for idx4, b4 in enumerate(rank3):
#                 for idx5, b5 in enumerate(rank3):
#
#                     if idx3<idx4<idx5:
#                     '''
#                     total in (3,1,1,0) = 48334
#                     '''
#                         fre+=1
#                         # print(idx1,idx2,idx3,idx4,idx5)
#                         # print(b1,b2,b3,b4,b5)
#
#                         if (idx1==idx3 or idx1==idx4 or idx1==idx5) and (idx2==idx3 or idx2==idx4 or idx2==idx5):
#                             '''
#                             two pairs & set in (3,1,1,0) color shape  = 2574 = 1716 + 858
#                             '''
#                             fre1+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                         if idx1 != idx2:
#                             # new_array = set(list) - set([idx3,idx4,idx5])
#                             # print(new_array)
#                             if  idx1 not in [idx3,idx4,idx5]:
#                                 if idx2 not in [idx3,idx4,idx5]:
#                                     '''
#                                     no pair in (3,1,1,0) = 25740
#                                     '''
#                                     fre2+=1
#                                     # print(idx1,idx2,idx3,idx4,idx5)
#                                     # print(b1,b2,b3,b4,b5)
#                         '''
#                         one pair in (3,1,1,0) = 20020
#                         '''
#                         if idx1 == idx2:
#                             if  idx1 not in [idx3,idx4,idx5]:
#                                 fre3+=1
#                                 print(idx1,idx2,idx3,idx4,idx5)
#                                 # print(b1,b2,b3,b4,b5)
#                         else:
#                             if idx1 in [idx3,idx4,idx5]:
#                                 if idx2 not in [idx3,idx4,idx5]:
#                                     fre3+=1
#                             if idx1 not in [idx3,idx4,idx5]:
#                                 if idx2 in [idx3,idx4,idx5]:
#                                     fre3+=1
#                             print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)
#
#
# print(fre, fre1, fre2, fre3)
# pprint(rb)
# print(len(rb))
#
# for i in rb.values():
#     total +=i
# print(total) # 1,529,112

# rb={}   ## River rainbow  # Theory:1,529,112 ? (real: 2,572,440=>12038)
# for idx1,b1 in enumerate(rank1):  # (2,2,1,0)
#     for idx2, b2 in enumerate(rank1):
#         for idx3, b3 in enumerate(rank2):
#             for idx4, b4 in enumerate(rank2):
#                 for idx5, b5 in enumerate(rank3):
#
#                     if idx1<idx2 and idx3<idx4:
#                         '''
#                         total in (2,2,1,0) =79092
#                         '''
#                         fre+=1
#                         # print(idx1,idx2,idx3,idx4,idx5)
#                         # print(b1,b2,b3,b4,b5)
#
#                         if idx1==idx3 or idx1==idx4 or idx2==idx3 or idx2==idx4:
#                             '''
#                             two pairs & set in (2,2,1,0) color shape  = 6006 = 4290 + 1716
#                             '''
#
#                             # temp = -1
#                             # for item in [idx1,idx2,idx3,idx4]:
#                             #     if item == idx5:
#                             #         temp =item
#                             #         break
#                             # for item in [idx1,idx2,idx3,idx4]:
#                             #     if item == temp:
#                                 # fre8+=1
#                                 # print(idx1,idx2,idx3,idx4,idx5)
#
#
#                             array = set([idx1,idx2,idx3,idx4,idx5])
#                             if len(array) == 3:
#                                 fre4+=1
#                                 # print(idx1,idx2,idx3,idx4,idx5)
#
#                                 # print(idx1,idx2,idx3,idx4,idx5)
#                         if idx1==idx3==idx5 or idx1==idx4==idx5 or idx2==idx3==idx5 or idx2==idx4==idx5:
#                             '''
#                             set in (2,2,1,0) = 1716
#                             '''
#                             array8 = set([idx1,idx2,idx3,idx4,idx5])
#                             if len(array8) == 3:
#                                 fre8+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#
#                         array1 = set([idx1,idx2,idx3,idx4,idx5])
#                         if len(array1) == 5:
#
#                             '''
#                             no pair in (2,2,1,0) = 38610
#                             '''
#                             fre5+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)
#                         '''
#                         one pair in (3,1,1,0) = 34320
#                         '''
#                         if len(array1) == 4:
#                             fre6+=1
#                             print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)
#                         '''
#                         Full house in (2,2,1,0) = 156
#                         '''
#                         if len(array1) == 2:
#                             fre7+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)

# rb={}   ## River Two color
# for idx1,b1 in enumerate(rank1):  # (3,2,0,0)
#     for idx2, b2 in enumerate(rank1):
#         for idx3, b3 in enumerate(rank2):
#             for idx4, b4 in enumerate(rank2):
#                 for idx5, b5 in enumerate(rank2):
#
#                     if idx3<idx4<idx5 and idx1<idx2:
#                         '''
#                         total in (3,2,0,0) =22308
#                         '''
#                         fre+=1
#                         # print(idx1,idx2,idx3,idx4,idx5)
#                         # print(b1,b2,b3,b4,b5)
#
#                         if (idx1==idx3 or idx1==idx4 or idx1==idx5) and (idx2==idx3 or idx2==idx4 or idx2==idx5):
#                             '''
#                             two pairs in (3,2,0,0)  =858
#                             '''
#                             fre8+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#
#                         array1 = set([idx1,idx2,idx3,idx4,idx5])
#                         if len(array1) == 5:
#
#                             '''
#                             no pair in (3,2,0,0) = 12870
#                             '''
#                             fre5+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)
#                         '''
#                         one pair in (3,1,1,0) = 8580
#                         '''
#                         if len(array1) == 4:
#                             fre6+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)

# rb={}   ## River Two color
# for idx1,b1 in enumerate(rank1):   # (4,1,0,0) = 12*9295  iteration=
#     for idx2, b2 in enumerate(rank1):
#         for idx3, b3 in enumerate(rank1):
#             for idx4, b4 in enumerate(rank1):
#                 for idx5, b5 in enumerate(rank2):
#
#                     if idx1<idx2<idx3<idx4:
#                         '''
#                         total in (4,1,0,0) =9295
#                         '''
#                         fre+=1
#
#                         array1 = set([idx1,idx2,idx3,idx4,idx5])
#                         if len(array1) == 5:
#
#                             '''
#                             no pair in (4,1,0,0) = 6435
#                             '''
#                             fre5+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)
#                         '''
#                         one pair in (4,1,0,0) =
#                         '''
#                         if len(array1) == 4:
#                             fre6+=1
#                             # print(idx1,idx2,idx3,idx4,idx5)
#                             # print(b1,b2,b3,b4,b5)

rb={}   ## River One color
for idx1,b1 in enumerate(rank1):   # (5,0,0,0) = 12*1287(C5,13)  iteration=
    for idx2, b2 in enumerate(rank1):
        for idx3, b3 in enumerate(rank1):
            for idx4, b4 in enumerate(rank1):
                for idx5, b5 in enumerate(rank1):

                    if idx1<idx2<idx3<idx4<idx5:
                        '''
                        total in (4,1,0,0) =9295
                        '''
                        fre+=1

                        '''
                        no pair in (4,1,0,0) = 6435
                        '''
                        fre5+=1
                        # print(idx1,idx2,idx3,idx4,idx5)
                        # print(b1,b2,b3,b4,b5)


print(fre, fre4, fre5, fre6, fre7, fre8)
# pprint(rb)
# print(len(rb))
#
# for i in rb.values():
#     total +=i
# print(total) # 1,529,112

'''
all     set&two noPair oneP fulHouse
(79092, 6006, 38610, 34320, 156)

(3,2,0,0)
all     set&two noPair oneP fulHouse
(22308, 0, 12870, 8580, 0, 858)
(4,1,0,0)
all     set&two noPair oneP fulHouse
(9295, 0, 6435, 2860, 0, 0)
(5,0,0,0)
(1287, 0, 1287, 0, 0, 0)




'''
