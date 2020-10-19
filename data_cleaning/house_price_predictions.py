import pandas as pd
import numpy as np
import seaborn as sbn
import matplotlib.pyplot as plt

# save dataset into easy to use variable
data = 'house_price_prediction.csv'

# call in dataset to new dataframe
house_prices = pd.read_csv(data)

# check that data was read in correctly
print(house_prices.head())  # reads top 5 rows of dataframe

# check the data's data types - here we are finding whether we have continuous data, discrete data, or a mixture of both
print(house_prices.dtypes)

# check summary statistics of the data
print(house_prices.describe())

# check out a pair plot to determine correlations
sbn.pairplot(house_prices)
plt.show()