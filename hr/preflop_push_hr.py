import matplotlib.pyplot as plt
import numpy as np
from pprint import pprint
import eval7
import pandas as pd
import re
import seaborn as sns
from statistics import mean
import sys

sns.set()

# with open("guru_1fictious_palyers=9_betStruct=1_rounds=20_'2019-11-08'.txt", "r") as ins:
#     pos=[]
#     for line in ins:
#         pos.append(line.split(','))
data = "./log/guru_proceed_palyers=9_betStruct=1_rounds=100_'2019-11-12T20:30:51'.txt"
data1 = "guru_1fictious_palyers=6_betStruct=3_rounds=20_'2019-11-10'.txt"
data2 = "guru_1fictious_palyers=3_betStruct=3_rounds=20_'2019-11-08'.txt"

# with open("guru_fictious_9__20__'2019-11-08'.txt", "r") as ins:
#     pos1=[]
#     for line in ins:
#         pos1.append(line.split(','))
# data1 = "guru_fictious_9__20__'2019-11-08'.txt"

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

def loadData_group(data, top):
    with open(data, "r") as ins:
        pos=[]
        for line in ins:
            pos.append(line.split(','))

    cards = [i[0] for i in pos ]

    # perc25 = percentile(cards, 25)
    # pos_new = [i if i[0]  not in perc25 else [i[0], '30']  for i in pos]
    pos_new = pos

    cardStringList1 = [i[0] for i in pos_new ]

    # first = [i[0] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[1] for i in cardStringList1]
    # second = [i[1] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[0] for i in cardStringList1]
    if top == 5:
        category = [0,5,5,5,5,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 15:
        category = [0,15,5,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 25:
        category = [0,25,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 10:
        category = [0,10,5,5,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 20:
        category = [0,20,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 30:
        category = [0,30,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 35:
        category = [0,35,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 40:
        category = [0,40,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 45:
        category = [0,45,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 50:
        category = [0,50,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 55:
        category = [0,55,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 60:
        category = [0,60,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 65:
        category = [0,65,5,5,5,5,5,5,5] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    if top == 70:
        category = [0,70,5,5,5,5,5,5] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...

    # category = [0,30,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    # category = [0,15,5,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...
    # category = [0,20,5,5,5,5,5,5,5,5,5,5,30] # Increments for each group # 0.1%, 5.1%, 10.1%, 15.1% ...

    cum=0
    first=[]
    second=[]
    cardRankValue1=[]
    for index, pert in enumerate(category):
        cum+=pert
        if pert == 0:
            card_diff10 = percentile(cardStringList1,0)
            group_mean_value = round(mean([float(re.sub('\s','',i[1])) for i in pos_new if i[0] in card_diff10 ]),1)
        else:
            card_diff10 = Diff(percentile(cardStringList1,cum), percentile(cardStringList1,cum-category[index]))
            group_mean_value = round(mean([float(re.sub('\s','',i[1])) for i in pos_new if i[0] in card_diff10 ]),1)
        cardRankValue=[group_mean_value for i in card_diff10]
        first1 = [i[0] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[1] for i in card_diff10]
        second1 = [i[1] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[0] for i in card_diff10]
        first+=first1
        second+=second1
        cardRankValue1+=cardRankValue


    # cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos_new ]
    # cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos_new ]
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




# cardStringList1 = [i[0] for i in pos ]
# cardStringList2 = [i[0] for i in pos1 ]

# perc50 = percentile(cardStringList1, 5)
# test = [i if i[0]  not in perc50 else [i[0], 20]  for i in pos]
# pprint(test)

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


pivot_data91 = [loadData_group(data, 5),
                loadData_group(data, 10),
                loadData_group(data, 15)]
                # loadData_group(data, 20),
                # loadData_group(data, 25),
                # loadData_group(data, 30),
                # loadData_group(data, 35),
                # loadData_group(data, 40),
                # loadData_group(data, 45),
                # loadData_group(data, 50),
                # loadData_group(data, 55),
                # loadData_group(data, 60),
                # loadData_group(data, 65),
                # loadData_group(data, 70)]




# pivot_data92 = loadData_group(data, 15)
# pivot_data93 = loadData_group(data, 10)

# pivot_data61 = loadData_group(data1, 40)
# pivot_data62 = loadData_group(data1, 25)
# pivot_data63 = loadData_group(data1, 15)
#
# pivot_data31 = loadData_group(data2, 65)
# pivot_data32 = loadData_group(data2, 40)
# pivot_data33 = loadData_group(data2, 30)

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

for i in range(len(pivot_data91)):
    #http://alanpryorjr.com/visualizations/seaborn/heatmap/heatmap/
    f, ax = plt.subplots(figsize=(9, 6))
    p = sns.heatmap(   pivot_data91[i],
                       #annot=True ,
                       cmap='cool',
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
    plt.title("Top"+str(5+i))
    ax.set_xticks([])
    ax.set_yticks([])
    # plt.show()
    ax.get_figure().savefig('EV+9'+str(i)+'.png')


# import matplotlib.pylab as pylab
# params = {'legend.fontsize': 'x-large',
#           'figure.figsize': (15, 5),
#          'axes.labelsize': '17',
#          'axes.titlesize':'x-large',
#          # 'xtick.labelsize':'x-large',
#          # 'ytick.labelsize':'x-large'
#          }
# pylab.rcParams.update(params)
#
# fig, axes = plt.subplots(nrows = 3, ncols = 3, figsize = (25,25));
#
# sns.heatmap(pivot_data91, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[0,0], cbar = False);
# axes[0,0].set_title('player 9 and Round 1(Top 30%)', fontsize=12)
# axes[0,0].set_xlabel('')
# axes[0,0].set_ylabel('')
# axes[0,0].set_xticks([])
# axes[0,0].set_yticks([])
#
# sns.heatmap(pivot_data92, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[0,1], cbar = False);
# axes[0,1].set_title('player 9 and Round 2(Top 15%)', fontsize=12)
# axes[0,1].set_xlabel('')
# axes[0,1].set_ylabel('')
# axes[0,1].set_xticks([])
# axes[0,1].set_yticks([])
#
#
# sns.heatmap(pivot_data93, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[0,2], cbar = False);
# axes[0,2].set_title('player 9 and Round 3(Top 10%)', fontsize=12)
# axes[0,2].set_xlabel('')
# axes[0,2].set_ylabel('')
# axes[0,2].set_xticks([])
# axes[0,2].set_yticks([])
#
# sns.heatmap(pivot_data61, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[1,0], cbar = False);
# axes[1,0].set_title('player 6 and Round 1(Top 40%)', fontsize=12)
# axes[1,0].set_xlabel('')
# axes[1,0].set_ylabel('')
# axes[1,0].set_xticks([])
# axes[1,0].set_yticks([])
#
# sns.heatmap(pivot_data62, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[1,1], cbar = False);
# axes[1,1].set_title('player 6 and Round 2(Top 25%)', fontsize=12)
# axes[1,1].set_xlabel('')
# axes[1,1].set_ylabel('')
# axes[1,1].set_xticks([])
# axes[1,1].set_yticks([])
#
# sns.heatmap(pivot_data63, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[1,2], cbar = False);
# axes[1,2].set_title('player 6 and Round 3(Top 15%)', fontsize=12)
# axes[1,2].set_xlabel('')
# axes[1,2].set_ylabel('')
# axes[1,2].set_xticks([])
# axes[1,2].set_yticks([])
#
# sns.heatmap(pivot_data31, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[2,0], cbar = False);
# axes[2,0].set_title('player 3 and Round 1(Top 65%)', fontsize=12)
# axes[2,0].set_xlabel('')
# axes[2,0].set_ylabel('')
# axes[2,0].set_xticks([])
# axes[2,0].set_yticks([])
#
# sns.heatmap(pivot_data32, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[2,1], cbar = False);
# axes[2,1].set_title('player 3 and Round 2(Top 40%)', fontsize=12)
# axes[2,1].set_xlabel('')
# axes[2,1].set_ylabel('')
# axes[2,1].set_xticks([])
# axes[2,1].set_yticks([])
#
# sns.heatmap(pivot_data33, annot=labels, fmt="", linewidths=.5, square = True, robust=True,cmap='cool', ax = axes[2,2], cbar = False);
# axes[2,2].set_title('player 3 and Round 3(Top 30%)', fontsize=12)
# axes[2,2].set_xlabel('')
# axes[2,2].set_ylabel('')
# axes[2,2].set_xticks([])
# axes[2,2].set_yticks([])
#
# plt.show()

# plt.savefig('preflop_9')
# p.get_figure().savefig('heatmap.png')

# print(percentile(cardStringList1, 5))
# percentile(cardStringList, 10)       # ['AA', 'KK', 'QQ', 'JJ', 'AKs', 'AQs', 'TT', 'AKo', 'AJs', 'KQs', 'ATs', 'AQo', '99', 'KJs', 'KTs', 'QJs', 'KQo', 'AJo', 'A9s', 'QTs', '88', 'A8s']
# print(percentile(cardStringList2, 13))       #['AA', 'KK', 'QQ']
# percentile(cardStringList, 0.1)    # ['AA']
