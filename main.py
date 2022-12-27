import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib import gridspec

#to read the data specify the file location of the dataset
data = pd.read_csv(r'C:\Users\Admin\hello\creditcard.csv')
#print(data)


#print(data.shape)
#print(data.describe())


#determine the fraud cases in the dataset

fraud = data[data['Class'] == 1]
valid = data[data['Class'] == 0]


#outlier fraction- the fraction of valid transactions to that of frauid transactions
outlierFraction = len(fraud)/float(len(valid))
#print(outlierFraction)
#print('Fraud Cases: {}'.format(len(fraud)))
#print('Valid Transactions: {}'.format(len(valid)))


#from the data there are only 0.17% fraudulent transaction out all the transactions
print("Amount details of the fraudulent transaction")
#fraud.Amount.describe()


# Correlation matrix
corrmat = data.corr()
fig = plt.figure(figsize = (12, 9))
sns.heatmap(corrmat, vmax = .8, square = True)
plt.show()
