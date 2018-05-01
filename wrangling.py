import pandas as pd

# load csc file into a pandas data frame
df = pd.read_csv('data\\train.csv')

#print out contents of dataframe
#df
print(df)

#determine which cilumn have a null value
print(pd.isnull(df).any())

#show first few rows (first 5 lines)
print(df.head())

#remove rows that have null values
df.dropna()

## filter ##
# filter data: passagner older than 30
# (run in shell)
df[df['Age'] > 30]

#filter data: female passengers
#(copy to and run in shell)
df[df['Sex'] == 'female']

# filter data: females over 30
#(copy to and run in shell)
df[(df['Age'] > 30) & (df['Sex'] == 'female')]

# Save hte filter to a variable
#(copy to and run in shell)
femalesOver30 = df[(df['Age']>30) & (df['Sex']=='female')]
femalesUnder30 = df[(df['Age']<30) & (df['Sex']=='female')]
malesOver30 = df[(df['Age']>30) & (df['Sex']=='male')]
malesUnder30 = df[(df['Age']<30) & (df['Sex']=='male')]

# display the meta data on filtered data frames
femalesOver30.describe()
femalesUnder30.describe()
malesOver30.describe()
print(malesUnder30.describe())

## Grouping date ##
df.groupby('Sex').Survived.value_counts()

## time series data ##
from datetime import datetime
import numpy as np

# create an array of 200 elements at 1 sec intervals
# (copy to and run in shell, add data to show the result)
data = pd.date_range('1/1/2017', periods=150, freq = 's')
# data

# create times series data by assigning random integers
#
time_series = pd.Series(np.random.randint(0, 500, len(data)), index = data)

# print out a few values
print(time_series.head())
# just copy 'time_series.head()' to shell

# re-sample 1 second bins to munite and sum the corresponding values
time_series_min = time_series.resample('1Min').sum()
# you can run time_series_miin.head() in shell

# time zone conversion - assume original time series was UTC a s we want US EST
time_series_utc = time_series.tz_localize('UTC')

# now convert
time_series_est = time_series_utc.tz_convert('US/Eastern')
# run 'time_series_utc.head()' in shell
#run 'time_series_est.head()' in shell

# copy in shell. 
femalesOver30.head()

# export a filter to excel
# copy in shell
# (shell) import openpyxl
import openpyxl
femalesOver30.to_excel('femalesOver30.xlsx')














