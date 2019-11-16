#Hello
import os
import sys
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

    s2 = pd.Series(['aa','bb','cc'])
    print("s=\n",s)
    print()
    print("s2=\n",s2)
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

	TABLE01df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataWithHeader.csv')
	print(TABLE01df)
	TABLE01df["Modified"] = pd.to_datetime(TABLE01df.Modified)
	"""TABLE01df:
		Key           Text             Modified
	0  Key1  Text for Key1  01/01/2019 01:11:11
	1  Key2  Text for Key2  02/02/2019 02:22:22
	2  Key3  Text for Key3  03/03/2019 03:33:33
	3  Key4  Text for Key4  04/04/2019 04:44:44
	"""
	TABLE02df = TABLE01df.set_index("Key")
	print(TABLE02df)
	"""TABLE02df:
				Text            Modified
	Key                                    
	Key1  Text for Key1 2019-01-01 01:11:11
	Key2  Text for Key2 2019-02-02 02:22:22
	Key3  Text for Key3 2019-03-03 03:33:33
	Key4  Text for Key4 2019-04-04 04:44:44
	"""
	TABLE03df = TABLE01df.set_index("Key",drop=False)
	print(TABLE03df)
	"""TABLE03df:  drop=False option does not drop column after making it the index
		Key           Text            Modified
	Key                                          
	Key1  Key1  Text for Key1 2019-01-01 01:11:11
	Key2  Key2  Text for Key2 2019-02-02 02:22:22
	Key3  Key3  Text for Key3 2019-03-03 03:33:33
	Key4  Key4  Text for Key4 2019-04-04 04:44:44
	"""

	# Import csv with no header and provide column names, otherwise column names are assumed to be provided by first row
	TABLE11df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None,names=["Key","Text","Modified"])
	print(TABLE11df)
	"""TABLE11df:
		Key                    Text             Modified
	0  Key1  Text for Key1 Modified  01/01/2019 11:11:11
	1  Key2  Text for Key2 Modified  02/02/2019 22:22:22
	2  Key5           Text for Key5  05/05/2019 05:55:55
	3  Key6           Text for Key6  06/06/2019 06:66:66
	"""

	TABLE12df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None)
	print(TABLE12df)
	"""TABLE12df:  when header=None and names are not specified, column names are just index numbers
		0                       1                    2
	0  Key1  Text for Key1 Modified  01/01/2019 11:11:11
	1  Key2  Text for Key2 Modified  02/02/2019 22:22:22
	2  Key5           Text for Key5  05/05/2019 05:55:55
	3  Key6           Text for Key6  06/06/2019 06:66:66
	"""

	TABLE13df = pd.read_csv(os.path.dirname(sys.argv[0])+'\\TestDataNoHeader.csv',header=None,names=["Key","Text","Modified"],index_col="Key")
	print(TABLE13df)
	"""TABLE13df:  Set key on import csv
							Text             Modified
	Key                                              
	Key1  Text for Key1 Modified  01/01/2019 11:11:11
	Key2  Text for Key2 Modified  02/02/2019 22:22:22
	Key5           Text for Key5  05/05/2019 05:55:55
	Key6           Text for Key6  06/06/2019 06:66:66
	"""

	JOIN01df = TABLE02df.join(TABLE13df, on="Key",how="outer",lsuffix=".a",rsuffix=".b",sort=True)
	print(JOIN01df)
	"""JOIN01df:  outer join with suffix
				Text.a          Modified.a                  Text.b           Modified.b
	Key                                                                                 
	Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
	Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
	Key3  Text for Key3 2019-03-03 03:33:33                     NaN                  NaN
	Key4  Text for Key4 2019-04-04 04:44:44                     NaN                  NaN
	Key5            NaN                 NaT           Text for Key5  05/05/2019 05:55:55
	Key6            NaN                 NaT           Text for Key6  06/06/2019 06:66:66
	"""

	JOIN02df = TABLE02df.join(TABLE13df, on="Key",how="inner",lsuffix=".a",rsuffix=".b",sort=True)
	print(JOIN02df)
	"""JOIN02df: Inner join like an intersection of both sets
				Text.a          Modified.a                  Text.b           Modified.b
	Key                                                                                 
	Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
	Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
	"""

	JOIN03df = TABLE02df.join(TABLE13df, on="Key",how="left",lsuffix=".a",rsuffix=".b",sort=True)
	print(JOIN03df)
	"""
				Text.a          Modified.a                  Text.b           Modified.b
	Key                                                                                 
	Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
	Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
	Key3  Text for Key3 2019-03-03 03:33:33                     NaN                  NaN
	Key4  Text for Key4 2019-04-04 04:44:44                     NaN                  NaN
	"""

	JOIN04df = TABLE02df.join(TABLE13df, on="Key",how="right",lsuffix=".a",rsuffix=".b",sort=True)
	print(JOIN04df)
	"""
				Text.a          Modified.a                  Text.b           Modified.b
	Key                                                                                 
	Key1  Text for Key1 2019-01-01 01:11:11  Text for Key1 Modified  01/01/2019 11:11:11
	Key2  Text for Key2 2019-02-02 02:22:22  Text for Key2 Modified  02/02/2019 22:22:22
	Key5            NaN                 NaT           Text for Key5  05/05/2019 05:55:55
	Key6            NaN                 NaT           Text for Key6  06/06/2019 06:66:66
	"""

	# Select rows where Text.a column is null (Nan)
	TEMPdf = JOIN01df[ (JOIN01df["Text.a"].isnull())]
	print(TEMPdf)
	"""
			Text.a Modified.a         Text.b           Modified.b
	Key
	Key5    NaN        NaT  Text for Key5  05/05/2019 05:55:55
	Key6    NaN        NaT  Text for Key6  06/06/2019 06:66:66
	"""

	# Selecting Text.b and Modified.b columns for a subset automatically selects index.
	TEMPdf = TEMPdf[['Text.b','Modified.b']].copy()
	print(TEMPdf)
	"""
				Text.b           Modified.b
	Key
	Key5  Text for Key5  05/05/2019 05:55:55
	Key6  Text for Key6  06/06/2019 06:66:66
"""


	print()

	
# pandas function application
def FunctionApplicationExample():
	print("******************************************************")
	print("* Begin FunctionApplicationExample()")
	print("******************************************************")
	print()
	
	data = { 	'Key1':["Text1", 1, 11, "Strings/Text/","Import"],
				'Key2':["Text2", 2, 22, "Strings/Text/",None],
				'Key3':["Text3", 3, 33, "Strings/Text/",np.nan], 
				'Key4':[np.nan, 4, 44, np.nan,"Import/Test"], 
				}
				
	df = pd.DataFrame( list(data.values()), columns=['Text','Stat1','Stat2','Path','Option'], index=data.keys())
	print(df)
	print()
	"""
		Text  Stat1  Stat2           Path       Option
	Key1  Text1      1     11  Strings/Text/       Import
	Key2  Text2      2     22  Strings/Text/         None
	Key3  Text3      3     33  Strings/Text/          NaN
	Key4    NaN      4     44            NaN  Import/Test
	"""
				
	df1 = df

	#Replace NaN and None with "" (empty string) in the 'Path' and 'Option' column
	df1[['Path','Option']] = df1[['Path','Option']].replace(to_replace=np.nan, value='')
	print(df1)
	print()
	"""
		Text  Stat1  Stat2           Path       Option
	Key1  Text1      1     11  Strings/Text/       Import
	Key2  Text2      2     22  Strings/Text/
	Key3  Text3      3     33  Strings/Text/
	Key4    NaN      4     44                 Import/Test
	"""

	#use in lambda function to creat final folder path from Path and Option columns
	def FolderPath(Path,Option):
		if len(Option):
			return "Strings/Text/{}/".format(Option)
		else:
			if len(Path):
				return Path
			else:
				return "Strings/Import/Temp"

	# Add folderPath column that is calculated by FolderPath() lambda above
	df1['folderPath'] = df1.apply( lambda x: FolderPath(x.Path, x.Option), axis='columns')
	print(df1)
	"""
		Text  Stat1  Stat2           Path       Option                 folderPath
	Key1  Text1      1     11  Strings/Text/       Import       Strings/Text/Import/
	Key2  Text2      2     22  Strings/Text/                           Strings/Text/
	Key3  Text3      3     33  Strings/Text/                           Strings/Text/
	Key4    NaN      4     44                 Import/Test  Strings/Text/Import/Test/
	"""

	# when not using a lambda, assume argument for function is current row when apply iterates the column
	def FolderPath2( dfrow):
		if len(dfrow.Option):
			return "Strings2/Text/{}/".format(dfrow.Option)
		else:
			if len(dfrow.Path):
				return dfrow.Path
			else:
				return "Strings2/Import/Temp"

	df1['folderPath'] = df1.apply(FolderPath2, axis='columns' )
	print(df1)
	
	def adder( e1, e2):
		return e1 + e2   # looks like e1 represents element in Dataframe and all params after are extra
	
	# NOTE only applying function to numeric subset of the DataFrame
	print(df1[['Stat1','Stat2']].pipe(adder,2))
	print()
	print(df1[['Stat1','Stat2']].pipe( lambda x: x*2)) # multiply every element in table by 2
	print()
	df1['Stat1']=df1['Stat1'].pipe( lambda x: x*100)
	print(df1)
	
	
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


def JoinExamples():

    PretendCurrentText = pd.DataFrame( { "key":['key0','key1','key2','key3'], "Text":['Text0','Text1','Text2','Text3']} )

    PretendChangedText = pd.DataFrame( { "key":['key1','key2','key4'], "Updated":['Text1','Text2Changed','Text4']} )
        # key0 missing
        # key1 text same
        # key2 text changed
        # key3 is new


    print(PretendCurrentText)
    print()
    print(PretendChangedText)
    print()

    JoinedInner = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="inner")
    print("Inner Join:")
    print(JoinedInner)
    print()

    JoinedText = PretendCurrentText.join(PretendChangedText.set_index("key"), on="key", how="outer")
    print("Outer Join:")
    print(JoinedText)
    print()

    TextChanges = JoinedText['Text'] != JoinedText['Updated'] 
    #print(TextChanges)

    UpdateNotNull = JoinedText['Updated'].notnull() 
    #print(UpdateNotNull)

    JoinBools = TextChanges & UpdateNotNull
    #print(JoinBools)

    #ChangedOnly = JoinedText[ JoinBools ]
    ChangedOnly = JoinedText[ (JoinedText['Text'] != JoinedText['Updated'])  & ( JoinedText['Updated'].notnull() ) ]
    print(ChangedOnly)
    print()

    Updates = JoinedText.query('Text != Updated & Updated.notnull() & Text.notnull()', engine='python')
    print(Updates)

from collections import namedtuple, OrderedDict
def Namedtuple2Dataframe():
	_Headers = ["identifier","SourceText","stringType"]
	Tnamedtuple = namedtuple("Tnamedtuple",_Headers)

	LocDirect=OrderedDict()
	LocDirect["key1"]=Tnamedtuple._make(["key1","key1 text","type4"])
	LocDirect["key2"]=Tnamedtuple._make(["key2","key2 text","type2"])
	LocDirect["key3"]=Tnamedtuple._make(["key3","key3 text","type3"])
	LocDirect["key4"]=Tnamedtuple._make(["key4","key4 text","type4"])

	print(LocDirect.values())

	LocDirect_df = pd.DataFrame( list(LocDirect.values()), columns=_Headers, index=LocDirect.keys())

	print(LocDirect_df)


	print(LocDirect_df["SourceText"]["key3"])

	print(LocDirect_df.loc["key2"]["stringType"])

	print(LocDirect_df.loc["key2",:])

	print(LocDirect_df.loc['key2','SourceText'])

	dfobject =  LocDirect_df.get('SourceText',default='Not valid!')
	print(dfobject)

	dfobject = LocDirect_df.at['key4','SourceText']
	print(dfobject)

	dfobject = LocDirect_df[LocDirect_df.index == 'key2']
	print(dfobject['SourceText']['key2'])

	dfobject = LocDirect_df[LocDirect_df.index == 'key6']
	if(dfobject.empty):
		print("Empty!")
	else:
		print(dfobject)





Namedtuple2Dataframe()
SeriesExample()
DataFrameExample()
FunctionApplicationExample()
JoinExamples()
