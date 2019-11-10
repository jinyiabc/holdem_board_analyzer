import seaborn as sns
import matplotlib.pyplot as plt
sns.set(style="ticks")
import pandas as pd
import numpy as np


# g = sns.FacetGrid(tips, col="time",  row="smoker")
# g = g.map(plt.hist2d("total_bill", "tip",cmap='plasma'), edgecolor="w")
#
# plt.show()


with open("tips.csv", "r") as ins:
    pos=[]
    for line in ins:
        pos.append(line.split())

# print(len(pos[0]))
column = pos[0][:5]
b = np.array(pos[0][5:]).reshape((27, 5))
# print(b)

c = np.zeros((27, 5))   #  [3.     5.     0.8577 0.819  0.7356]
for k in range(27):
    for j in range(5):
        if j<=1:
            c[k][j] = int(b[k][j])
        else:
            c[k][j] = float(b[k][j][:-1])*0.01
# print(column)   # ['players', 'round', '90%', '95%', '99%']
df = pd.DataFrame(c, columns=column)
print(df)
plt.xticks(np.arange(0, 10, step=1))
g = sns.FacetGrid(df, col="players")
g = g.map(plt.plot, "round","90%",  color='green')
g = g.map(plt.plot, "round","95%",  color='red')
g = g.map(plt.plot, "round","99%",  color='blue')

g.set(xticks=np.arange(10))


#
plt.show()
