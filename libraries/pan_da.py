#!/usr/bin/python
import pandas as pd
import numpy as np

# 1) Series: one-dimensional ndarray with axis labels (including time series)

print "1) creating a Series by passing a list of values, letting pandas create a default integer index"
series = pd.Series([1, 3, 5, np.nan, 6, 8])
print series

# 2.1) DataFrame: two-dimensional size-mutable, potentially heterogeneous tabular data structure with labeled axes
#               (rows and columns)

print "2.1) creating a DataFrame by passing a numpy array, with a datetime index and labeled columns"
rng = pd.date_range('20160701', periods=6)
print rng

df = pd.DataFrame(np.random.randn(len(rng), len(list('ABCD'))), index=rng, columns=list('ABCD'))
print df

# append a row to the data frame
print 'append a row to data frame'
row = pd.Series(['X', 'X', 'X', 'X'], index=['A', 'B', 'C', 'D'], name=pd.to_datetime('20160707'))
print df.append(row)

# remove a row from the data frame
print 'remove a row to data frame'
df.drop(df.index[[5]])
print df

# 2.2) Time Series
print "2.2) simple, powerful, efficient functionality for performing resampling operations during frequency conversion"
rng = pd.date_range('11/1/2016', periods=4, freq='H')
print rng
ts = pd.Series(np.random.randint(0, 500, len(rng)), index=rng)
print ts

print "2.2) creating a DataFrame by passing a dict of objects that can be converted to series-like"

df2 = pd.DataFrame({ 'A' : 1.,
                     'B' : pd.Timestamp('20130102'),
                     'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
                     'D' : np.array([3] * 4,dtype='int32'),
                     'E' : pd.Categorical(["test","train","test","train"]),
                     'F' : 'foo' })
print df2
print df2.dtypes

# 3) View data
print "3.1) display the top & bottom rows of the frame"
print df.head(2)
print df.tail(2)

print "3.2) display the index, columns, and the underlying numpy data"
print df.index
print df.columns
print df.values

print "3.3) sorting by values"
print df.sort_values(by='B')

# 4) Selection
print "4.1) selecting a single column, which yields a Series, equivalent to df.A"
print df["A"]

print "4.2) showing label slicing, both endpoints are included"
print df.loc['20160702':'20160704',['A','B']]
#
# 5) Boolean indexing
print "5.1) using a single column's values to select data"
print df[df.A > 0]

print "5.2) a where operation for getting"
print df[df > 0]

# 6) Missing Data
print "pandas primarily uses the value np.nan to represent missing data"
print "6.1) to drop any rows that have missing data"
print (df[df > 0]).dropna(how="any")

print "6.2) filling missing data"
print (df[df > 0]).fillna(value=5)

# 7) Operations
print "7.1) stats: performing a descriptive statistic (compute the mean of each column)"
print df.mean()

print "7.2) stats: same operation on the other axis (compute the mean of each row)"
print df.mean(1)

print "7.3) apply: applying functions to the data"
print df.apply(lambda x: x.max() - x.min())

print "7.4) join: SQL style merges"
left = pd.DataFrame({'key': ['foo', 'foo'], 'lval': [1, 2]})
right = pd.DataFrame({'key': ['foo', 'foo'], 'rval': [4, 5]})
print left
print right
print pd.merge(left, right, on="key")

# 8) Getting Data In/Out
df.to_csv("foo.csv")
df.to_excel("foo.xlsx", sheet_name="MySheet")
