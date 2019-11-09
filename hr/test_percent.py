import numpy as np
from pprint import pprint
import eval7
import pandas as pd
import re
with open("guru_1fictious_palyers=9_betStruct=1_rounds=20_'2019-11-08'.txt", "r") as ins:
    pos=[]
    for line in ins:
        pos.append(line.split(','))
with open("guru_fictious_9__20__'2019-11-08'.txt", "r") as ins:
    pos1=[]
    for line in ins:
        pos1.append(line.split(','))

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

def percentile(cardStringList, n):
    hr=[]
    for i in range(len(cardStringList)):
        hr += eval7.HandRange(cardStringList[i]).hands

    i=len(hr)
    index=np.percentile(np.arange(i), n, interpolation='nearest')
    # print hr[index]
    # print( str(hr[index][0][0]) )
    if str(hr[index][0][0])[1] != str(hr[index][0][1])[1]:
        if str(hr[index][0][0])[0]!= str(hr[index][0][1])[0]:
            hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0] +'o'
        else:
            hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0]
    else:
        hand = str(hr[index][0][0])[0]+str(hr[index][0][1])[0] +'s'
    # print(hand)
    new_list=cardStringList[:(cardStringList.index(hand)+1)]
    # print(new_list)
    return new_list




cardStringList1 = [i[0] for i in pos ]
cardStringList2 = [i[0] for i in pos1 ]

perc50 = percentile(cardStringList1, 5)
test = [i if i[0]  not in perc50 else [i[0], 20]  for i in pos]
pprint(test)

# for pert in [5,10,25,35,45,55,65,75,85,95]:
#     print("Diffrence for # %d of hands" % pert)
#     card_diff10 = Diff(percentile(cardStringList1,pert), percentile(cardStringList2,pert))
#     print(card_diff10)
#
#     card_diff10_re = Diff(percentile(cardStringList2,pert), percentile(cardStringList1,pert))
#     print(card_diff10_re)
#
# print(percentile(cardStringList1, 5))
# percentile(cardStringList, 10)       # ['AA', 'KK', 'QQ', 'JJ', 'AKs', 'AQs', 'TT', 'AKo', 'AJs', 'KQs', 'ATs', 'AQo', '99', 'KJs', 'KTs', 'QJs', 'KQo', 'AJo', 'A9s', 'QTs', '88', 'A8s']
# print(percentile(cardStringList2, 13))       #['AA', 'KK', 'QQ']
# percentile(cardStringList, 0.1)    # ['AA']
