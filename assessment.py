import numpy as np
import pandas as pd

n = 20 # number, 班里有多少学生
col = 5 # column, 有几项需要随机（学习、思想等）

p1 = 0.2 # (5, first 20%)
p2 = 0.2 # (4, second 40%)
p3 = 0.6 # (3, last 40%)

scores = np.zeros((n,col+1))
p = np.concatenate([np.repeat(5,int(n*p1)), np.repeat(4,int(n*p2)), np.repeat(3,n - int(n*(p1+p2)))])

for c in range(col):
    scores[:,c] = np.random.choice(p, n, replace = False)
scores[:,col] = np.nansum(scores, axis=1)

data = pd.DataFrame(scores)
data.to_excel(r'D:\YAO_Shuyang\Students work\assessment.xlsx', sheet_name = '2022')

print(scores)