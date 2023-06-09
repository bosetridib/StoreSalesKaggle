import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

train = pd.read_csv('train.csv')
test = pd.read_csv('test.csv')
print("train (rows, cols) :", train.shape)
print("test (rows, cols) :", test.shape)

# Datatype of each column
print(train.info())
print(test.info())
# Missing Values
print(train.isna().sum())
print(test.isna().sum())

# There are 6 columns, and 2 of them are objects.
# There are no missing values.

train['date'] = train['date'].astype('datetime64[ns]')
test['date'] = test['date'].astype('datetime64[ns]')
train['family'] = train['family'].astype('category')
test['family'] = test['family'].astype('category')
train.set_index('id', inplace=True)
test.set_index('id', inplace=True)

hol_evs = pd.read_csv('holidays_events.csv')
print(hol_evs.shape)
print(hol_evs.info())
print(hol_evs.isna().sum())
hol_evs['date'] = hol_evs['date'].astype('datetime64[ns]')
hol_evs['type'] = hol_evs['type'].astype('category')
hol_evs['locale'] = hol_evs['locale'].astype('category')
hol_evs['locale_name'] = hol_evs['locale_name'].astype('category')
hol_evs.drop(columns='description', inplace=True)
hol_evs['transferred'] = hol_evs['transferred'].astype('int')


oil = pd.read_csv('oil.csv')
print(oil.shape)
print(oil.info())
print(oil.isna().sum())

stores = pd.read_csv('stores.csv')
print(stores.shape)
print(stores.info())
print(stores.isna().sum())

sub = pd.read_csv('sub.csv')
transactions = pd.read_csv('transactions.csv')

print(train['family'].value_counts())
print(test['family'].value_counts())

# One hot encoding of family

X_train = train.drop(columns = ['family','sales'])
X_test = test.drop(columns='family')

X_train = pd.concat(
    [
        X_train,
        pd.get_dummies(train['family'], prefix='family').astype('int')
    ],
    axis=1
)

X_test = pd.concat(
    [
        X_test,
        pd.get_dummies(test['family'], prefix='family').astype('int')
    ],
    axis=1
)
del train, test