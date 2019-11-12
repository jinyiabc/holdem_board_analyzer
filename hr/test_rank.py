import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import eval7
import pandas as pd
import re
import seaborn as sns

sns.set()


data = "./log3/guru_proceed_palyers=3_betStruct=1_rounds=150_'2019-11-13T02:02:12'.txt"
data1 = "guru_1fictious_palyers=6_betStruct=3_rounds=20_'2019-11-10'.txt"
data2 = "guru_1fictious_palyers=3_betStruct=3_rounds=20_'2019-11-08'.txt"

def Diff(li1, li2):
    return (list(set(li1) - set(li2)))

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

def loadData_group(data):
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
        # first+=first1
        # second+=second1
        # cardRankValue1+=cardRankValue


    cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos_new ]
    # cardRankValue1= [(i+1) for i in range(len(pos_new)) ]
    #
    # # pprint(cardRankValue1)
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



'''
compare two hand rankings
'''
# for pert in [5,10,25,35,45,55,65,75,85,95]:
#     print("Diffrence for # %d of hands" % pert)
#     card_diff10 = Diff(percentile(cardStringList1,pert), percentile(cardStringList2,pert))
#     print(card_diff10)
#
#     card_diff10_re = Diff(percentile(cardStringList2,pert), percentile(cardStringList1,pert))
#     print(card_diff10_re)


pivot_data91 = loadData_group(data)


labels =  np.array([['AA','AK','AQ','AJ','AT','A9','A8','A7','A6','A5','A4','A3','A2'],
                    ['AK','KK','KQ','KJ','KT','K9','K8','K7','K6','K5','K4','K3','K2'],
                    ['AQ','KQ','QQ','QJ','QT','Q9','Q8','Q7','Q6','Q5','Q4','Q3','Q2'],
                    ['AJ','KJ','QJ','JJ','JT','J9','J8','J7','J6','J5','J4','J3','J2'],
                    ['AT','KT','QT','JT','TT','T9','T8','T7','T6','T5','T4','T3','T2'],
                    ['A9','K9','Q9','J9','T9','99','98','97','96','95','94','93','92'],
                    ['A8','K8','Q8','J8','T8','98','88','87','86','85','84','83','82'],
                    ['A7','K7','Q7','J7','T7','97','87','77','76','75','74','73','72'],
                    ['A6','K6','Q6','J6','T6','96','86','76','66','65','64','63','62'],
                    ['A5','K5','Q5','J5','T5','95','85','75','65','55','54','53','52'],
                    ['A4','K4','Q4','J4','T4','94','84','74','64','54','44','43','42'],
                    ['A3','K3','Q3','J3','T3','93','83','73','63','53','43','33','32'],
                    ['A2','K2','Q2','J2','T2','92','82','72','62','52','42','32','22']
                    ])
rank = ['A','K','Q','J','T','9','8','7','6','5','4','3','2']

#http://alanpryorjr.com/visualizations/seaborn/heatmap/heatmap/

f, ax = plt.subplots(figsize=(9, 6))
p = sns.heatmap(   pivot_data91,
                   # annot=True ,
                   cmap='Oranges',
                   fmt="",
                   annot = labels,
                   annot_kws={'size':10},
                   square=True,
                   linewidths=.5,
                   robust=True,
                   ax=ax)

# plt.text(5,12.3,"Title", fontsize = 95, color='Black', fontstyle='italic')
plt.ylabel('')
plt.xlabel('')
plt.title("EV+ Players=3")
ax.set_xticks([])
ax.set_yticks([])
# plt.show()
ax.get_figure().savefig('EV+3.png')
