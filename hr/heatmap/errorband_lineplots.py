# """
# Timeseries plot with error bands
# ================================
#
# _thumb: .48, .45
#
# """
# import seaborn as sns
# sns.set(style="darkgrid")
from pprint import pprint
# # Load an example dataset with long-form data
# fmri = sns.load_dataset("fmri")
# pprint(fmri)
# # Plot the responses for different events and regions
# sns.lineplot(x="timepoint", y="signal",
#              hue="region", style="event",
#              data=fmri)

# import numpy as np
# import pandas as pd
# import seaborn as sns
# import matplotlib.pyplot as plt
#
# data = pd.read_csv('perc_hr.csv')
# df = pd.DataFrame(data)
# pprint(df)

import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import numpy as np

# data = np.array([[0.000000,0.000000],[-0.231049,0.000000],[-0.231049,0.000000]])
# labels =  np.array([['A','B'],['C','D'],['E','F']])
data = np.random.randn(13, 13)
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

import matplotlib.pylab as pylab
params = {'legend.fontsize': 'x-large',
          'figure.figsize': (15, 5),
         'axes.labelsize': '17',
         'axes.titlesize':'x-large',
         # 'xtick.labelsize':'x-large',
         # 'ytick.labelsize':'x-large'
         }
pylab.rcParams.update(params)

fig, axes = plt.subplots(nrows = 2, ncols = 3, figsize = (25,25));

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[0,0], cbar = False);

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[0,1], cbar = False);

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[0,2], cbar = False);

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[1,0], cbar = False);

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[1,1], cbar = False);

sns.heatmap(data, annot=labels, fmt="", linewidths=.5, square = True, cmap = 'Blues_r', ax = axes[1,2], cbar = False);

# fig, ax = plt.subplots()
# ax = sns.heatmap(data,
#                  xticklabels = False,
#                  annot = labels, fmt = '')
#
# plt.ylabel('')
# plt.xlabel('')
# plt.title('Scores by group and gender')
#
plt.show()
# ax.get_figure().savefig('heatmap.png')
