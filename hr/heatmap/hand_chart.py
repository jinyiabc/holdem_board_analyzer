"""
Annotated heatmaps
==================

"""
# import matplotlib
# matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
from pprint import pprint
import pandas as pd
import re
import eval7
from pprint import pprint

data="guru_1fictious_palyers=9_betStruct=1_rounds=20_'2019-11-08'.txt"

raise1_r2c = ['A2o', '33o', 'A3o', '44o', 'K4o', 'A4o', '55o', 'J5o', 'Q5o', 'K5o', 'A5o', '66o', 'T6o', 'J6o', 'Q6o', 'K6o', 'A6o', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A7o', '87s', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'A8o', '95s', '96s', '97s', '98s', 'T9o', 'J9o', 'Q9o', 'K9o', 'A9o', 'T4s', 'T5s', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'A9s', 'ATo']
raise2_r2c = ['22o', 'A2o', '33o', 'K3o', 'A3o', '44o', 'Q4o', 'K4o', 'A4o', '55o', 'J5o', 'Q5o', 'K5o', 'A5o', '66o', 'T6o', 'J6o', 'Q6o', 'K6o', 'A6o', '76s', '87o', '97o', 'T7o', 'J7o', 'Q7o', 'K7o', 'A7o', '86s', '87s', '98o', 'T8o', 'J8o', 'Q8o', 'K8o', 'A8o', '95s', '96s', '97s', '98s', 'T9o', 'J9o', 'Q9o', 'K9o', 'A9o', 'T4s', 'T5s', 'T6s', 'T7s', 'T8s', 'T9s', 'JTo', 'QTo', 'KTo', 'J2s', 'J3s', 'J4s', 'J5s', 'J6s', 'J7s', 'J8s', 'J9s', 'JTs', 'QJo', 'KJo', 'Q2s', 'Q3s', 'Q4s', 'Q5s', 'Q6s', 'Q7s', 'Q8s', 'Q9s', 'QTs', 'QJs', 'KQo', 'K2s', 'K3s', 'K4s', 'K5s', 'K6s', 'K7s', 'K8s', 'K9s', 'KTs', 'KJs', 'A2s', 'A3s', 'A4s', 'A5s', 'A6s', 'A7s', 'A8s', 'KQs', 'A9s']

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

def loadlist(list, value):



    cardStringList1 = [i for i in list ]

    first = [i[0] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[1] for i in cardStringList1]
    second = [i[1] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[0] for i in cardStringList1]

    # cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos_new ]
    # cardRankValue1= [int(10*float(re.sub('\s','',i[1])))/200 for i in pos_new ]
    cardRankValue1 = np.ones(len(list))*value
    # pprint(cardRankValue1)
    data={'first':first,
          'second':second,
          'value':cardRankValue1}

    rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    df = pd.DataFrame(data)
    table = pd.pivot_table(df, values=['value'], index=['second'],
                                columns=['first'], aggfunc=np.sum)
    table = table.reindex(index=rank)
    table1 = table['value']
    table1 = table1.reindex(columns=rank)
    # print(table1)
    return table1


def loadData(data):
    with open(data, "r") as ins:
        pos=[]
        for line in ins:
            pos.append(line.split(','))

    cards = [i[0] for i in pos ]

    # perc25 = percentile(cards, 25)
    # pos_new = [i if i[0]  not in perc25 else [i[0], '30']  for i in pos]
    pos_new = pos

    cardStringList1 = [i[0] for i in pos_new ]

    first = [i[0] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[1] for i in cardStringList1]
    second = [i[1] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[0] for i in cardStringList1]

    # cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos_new ]
    cardRankValue1= [int(10*float(re.sub('\s','',i[1])))/200 for i in pos_new ]

    # pprint(cardRankValue1)
    data={'first':first,
          'second':second,
          'value':cardRankValue1}

    rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']
    df = pd.DataFrame(data)
    table = pd.pivot_table(df, values=['value'], index=['second'],
                                columns=['first'], aggfunc=np.sum)
    table = table.reindex(index=rank)
    table1 = table['value']
    table1 = table1.reindex(columns=rank)
    # print(table1)
    return table1

table = loadData(data)
table1 = loadlist(raise1_r2c, 3)
table2 = loadlist(raise2_r2c, 5)
print(table2)
# # Load the example flights dataset and conver to long-form
# flights_long = sns.load_dataset("flights")
# flights = flights_long.pivot("month", "year", "passengers")
# flights=np.random.rand(13,13)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(table1, annot=False , fmt="f", linewidths=.5, ax=ax)
plt.show()
# plt.savefig('preflop_9')
