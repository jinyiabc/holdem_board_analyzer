"""
Annotated heatmaps
==================

"""
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
sns.set()
from pprint import pprint
import pandas as pd
import re

data="guru_1fictious_palyers=9_betStruct=1_rounds=20_'2019-11-08'.txt"

def loadData(data):
    with open(data, "r") as ins:
        pos=[]
        for line in ins:
            pos.append(line.split(','))

    cardStringList1 = [i[0] for i in pos ]
    first = [i[0] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[1] for i in cardStringList1]
    second = [i[1] if len(i)==2 or (len(i)==3 and i[2]=='o') else i[0] for i in cardStringList1]

    cardRankValue1= [float(re.sub('\s','',i[1])) for i in pos ]
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

    return table1

table = loadData(data)
# # Load the example flights dataset and conver to long-form
# flights_long = sns.load_dataset("flights")
# flights = flights_long.pivot("month", "year", "passengers")
flights=np.random.rand(13,13)
# Draw a heatmap with the numeric values in each cell
f, ax = plt.subplots(figsize=(9, 6))
sns.heatmap(table, annot=False , fmt="f", linewidths=.5, ax=ax)
plt.show()
# plt.savefig('preflop_9')
