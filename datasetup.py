import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
print(train.shape)
print(train.info())
print(train.isna().sum())
# There are 6 columns, and 2 of them are objects.
# There are no missing values.

train['date'] = train['date'].astype('datetime64[ns]')
train['family'] = train['family'].astype('category')

sns.lineplot(x=train['date'],y=train['sales'])
plt.show()