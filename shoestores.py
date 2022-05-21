import pandas as pd; 

# shoestores.xlsx contains copy of data from google sheets challenge
salesData = pd.read_excel('shoestores.xlsx') 

# short form
oa = ['order_amount']
ti = ['total_items']

# find IQR
q1 = salesData[oa].quantile(0.25)
q3 = salesData[oa].quantile(0.75)
iqr = q3 - q1

# set upper and lower bounds
lowerBounds = (q1 - 1.5 * iqr)
upperBounds = (q3 + 1.5 * iqr)

# exclude data outside boundaries
filterData = ~((salesData[oa] < lowerBounds) | (salesData[oa] > upperBounds)).any(axis= 1)

# create new dataframe with outliers removed
salesDataModified = salesData[filterData]

# calculate average order value (AOV)
AOV = float(round(salesDataModified[oa].mean(), 2))
print('Average order value (AOV): ' , AOV)

# is it realistic?
AIT = float(round(salesDataModified[ti].mean(), 2))
print('Avg number of items: ', AIT)
print('Avg unit price: ', AOV/AIT)
print('(# rows, # columns): ', salesDataModified.shape)