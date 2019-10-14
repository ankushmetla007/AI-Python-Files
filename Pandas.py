import numpy as np
import pandas as pd

data1=[1,2,3,4,5,6]
s1=pd.Series(data1)
print(s1)
index=['a','b','c','d','e','f']
s2=pd.Series(data1,index)
print(s2)

dict1={'a':1, 'b':2, 'c':3, 'd':4, 'e':5}  
s3=pd.Series(dict1)
print(s3)

data2=[[1,2,3],[4,5,6]]
s4=pd.Series(data2)
print(s4)

df1=pd.DataFrame(data1)
print(df1)

dict2 ={'a':1, 'b':2, 'c':3, 'd':4}        
dict3 ={'a':2, 'b':4, 'c':6, 'd':8, 'e':10}  
data3 = {'first':dict2, 'second':dict3}   
df2 = pd.DataFrame(data3) 
print(df2)

s5 = pd.Series([1, 3, 4, 5, 6, 2, 9])            
s6 = pd.Series([1.1, 3.5, 4.7, 5.8, 2.9, 9.3])  
s7 = pd.Series(['a', 'b', 'c', 'd', 'e'])      
data4 ={'first':s4, 'second':s3, 'third':s3'}  
df3 = pd.DataFrame(data4)
print(df3)

d1 =[[2, 3, 4], [5, 6, 7]]
d2 =[[2, 4, 8], [1, 3, 9]]
data5 ={'first': d1, 'second': d2}  
df4 = pd.DataFrame(data5) 
print(df4)







