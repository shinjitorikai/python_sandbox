import pandas as pd
from sklearn import datasets
import matplotlib.pyplot as plt

X,y = datasets.make_hastie_10_2(n_samples=100,random_state=None)

print('X.shape = ',X.shape)
print('y.shape = ',y.shape)

print('y = ',y)

dataframe = pd.DataFrame(data=X)
print('dataframe : ')
print(dataframe)

datalabel = pd.Series(data=y)
gr = pd.plotting.scatter_matrix(dataframe,c=datalabel,figsize=(12,12))
plt.show()
