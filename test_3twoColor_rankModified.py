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


fre=fre1=fre2=fre3=sub=0
rb={}   ## TwoColor
for idx1,b1 in enumerate(rank1):  # 1014 *12 = 12168
    for idx2, b2 in enumerate(rank1):
        for idx3, b3 in enumerate(rank2):
            '''
            (858, 156, 0)
            onePair twoPair set
            '''
            if idx1<9 and idx2<9 and idx3<9:
                if idx1<idx2:
                    if idx1<idx2<idx3:  #286
                        # pass  # 858
                        rb[(b1+b2+b3)]=12*3     # 1<2<3, 1<3<2, 3<1<2
                        '''
                        Range vs Range
                        [QQ, AQs,AQo]
                        board = AsBdCh, AdBsCh

                        '''
                        print(idx1,idx2,idx3)
                    if idx1==idx3<idx2:   #78
                        # pass  #156
                        rb[(b1+b2+b3)]=12*2     # C2,4*C1,2 = 12, 2 (1=3<2, 1<2=3)
                        # print(idx1,idx2,idx3)

#                 array = set([idx1,idx2,idx3])
#                 if len(array) == 3:
#                     fre +=1
#                 elif len(array) ==2:
#                     fre1+=1
#                 else:
#                     fre2+=1
#
# print(fre,fre1,fre2)
# print("the number of board: %d" % len(rb))
for i in rb.values():
    sub +=i
print(sub)

print("the number of board: %d" % len(rb))
