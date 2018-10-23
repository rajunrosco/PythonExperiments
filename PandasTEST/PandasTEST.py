#Hello
import pandas as pd
import numpy as np

# pandas Series examples 
def SeriesExample():
	print("******************************************************")
	print("* Begin SeriesExample()")
	print("******************************************************")
	print()
	data = np.array(['a','b','c',1.25])
	s = pd.Series(data)
	print(s)
	print()


	s = pd.Series([1,2,3.5,"ben"], index=['A','B','C','D'])
	print(s)
	print()
	print('s[2]={}  type={}'.format(s[2], type(s[2])))
	print('s["B"]={}  type={}'.format(s["B"], type(s["B"])))
	print('s["D"]={}  type={}'.format(s["D"], type(s["D"])))
	print()
	
	print()


# pandas DataFrame examples
def DataFrameExample():
	print("******************************************************")
	print("* Begin DataFrameExample()")
	print("******************************************************")
	print()
	data = [['Alex',10],['Bob',12],['Clarke',13]]
	df = pd.DataFrame(data,columns=['Name','Age'])
	print(df)
	print()

	data = { 	'Key1':['Text1','Status1'],
				'Key2':['Text2','Status2'],
				'Key3':['Text3','Status3'] 
			}
	print( list(data.values()) )
	print()
			
	df = pd.DataFrame( list(data.values()), columns=['Text','Status'], index=data.keys())
	print(df)
	print()
	
	print( df['Status'] )
	print()
	print( df['Status'].values )  # will return the series as an array
	print()
	print( df['Status']['Key2'] )
	print()
	print( df.loc['Key2'] )			# use .loc to search based on index (row)
	print()
	print( df.iloc[0] )
	print()
	print( df.loc['Key2']['Text'] )
	print()
	
	print(df.shape)
	print(df.values)
	
	print()
	
# pandas function application
def FunctionApplicationExample():
	print("******************************************************")
	print("* Begin FunctionApplicationExample()")
	print("******************************************************")
	print()
	
	data = { 	'Key1':["Text1", 1, 11],
				'Key2':["Text2", 2, 22],
				'Key3':["Text3", 3, 33] 
				}
				
	df = pd.DataFrame( list(data.values()), columns=['Text','Stat1','Stat2'], index=data.keys())
	
	print(df)
	print()
				
	df1 = df
	
	def adder( e1, e2):
		return e1 + e2   # looks like e1 represents element in Dataframe and all params after are extra
	
	# NOTE only applying function to numeric subset of the DataFrame
	print(df1[['Stat1','Stat2']].pipe(adder,2))
	print()
	print(df1[['Stat1','Stat2']].pipe( lambda x: x*2)) # multiply every element in table by 2
	print()
	
	
	print(df1[['Stat1','Stat2']].apply(lambda x: sum(x)*100))  # apply() by default takes entire column as list argument
	print()
	
	
	print(df1[['Stat1','Stat2']].applymap(lambda x: x+x/100))  # map will touch each element
	print()
	
	
	for key, value in df.iterrows():
		print(key)
		print( value.values )
		print()
	print()
	
	for key, value in df.iteritems():
		print(key)
		print( value.values )
		print()
	print()
	
	for row in df.itertuples():
		print(row)
		print(row.Stat2) # Named Tuple!
	print()
	
SeriesExample()
DataFrameExample()
FunctionApplicationExample()
