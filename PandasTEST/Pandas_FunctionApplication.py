import numpy as np
import pandas as pd
import PandasUtil

count = 0

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
                'Key5':["Text5",5, 55, np.nan,""], 
                }
                
    df = pd.DataFrame( list(data.values()), columns=['Text','Stat1','Stat2','Path','Option'], index=data.keys())
    PandasUtil.PrintDF("df",df)
    """
           Text  Stat1  Stat2           Path       Option
    Key1  Text1      1     11  Strings/Text/       Import
    Key2  Text2      2     22  Strings/Text/         None
    Key3  Text3      3     33  Strings/Text/          NaN
    Key4    NaN      4     44            NaN  Import/Test
    Key5  Text5      5     55            Nan   
    """
                
    df1 = df

    #Replace NaN and None with "" (empty string) in the 'Path' and 'Option' column
    df1[['Path','Option']] = df1[['Path','Option']].replace(to_replace=np.nan, value='')
    PandasUtil.PrintDF("df1",df1)
    """
           Text  Stat1  Stat2           Path       Option
    Key1  Text1      1     11  Strings/Text/       Import
    Key2  Text2      2     22  Strings/Text/
    Key3  Text3      3     33  Strings/Text/
    Key4    NaN      4     44                 Import/Test
    Key5  Text5      5     55            
    """

    #use in lambda function to create final folder path from Path and Option columns
    def FolderPath(Path,Option):
        if len(Option):
            return "Strings/Text/{}/".format(Option)
        else:
            if len(Path):
                return Path
            else:
                return "Strings/Import/Temp/"

    # Add folderPath column that is calculated by FolderPath() lambda above
    df1['folderPath'] = df1.apply( lambda x: FolderPath(x.Path, x.Option), axis='columns')
    PandasUtil.PrintDF("df1",df1)
    """
           Text  Stat1  Stat2           Path       Option                 folderPath
    Key1  Text1      1     11  Strings/Text/       Import       Strings/Text/Import/
    Key2  Text2      2     22  Strings/Text/                           Strings/Text/
    Key3  Text3      3     33  Strings/Text/                           Strings/Text/
    Key4    NaN      4     44                 Import/Test  Strings/Text/Import/Test/
    Key5  Text5      5     55                                  Strings2/Import/Temp/
    """

    
    # when not using a lambda, assume argument for function is current row when apply iterates the column
    def FolderPath2( dfrow ):
        global count
        count = count + 1
        print("Inside Counter: {}".format(count))
        if len(dfrow.Option):
            return "Strings2/Text/{}/".format(dfrow.Option)
        else:
            if len(dfrow.Path):
                return dfrow.Path
            else:
                return "Strings2/Import/Temp/"

    count = 0
    df1['folderPath'] = df1.apply(FolderPath2, axis='columns' )
    PandasUtil.PrintDF("df1",df1)

    def adder( e1, e2):
        return e1 + e2   # looks like e1 represents element in Dataframe and all params after are extra

    # NOTE only applying function to numeric subset of the DataFrame
    print(df1[['Stat1','Stat2']].pipe(adder,2))
    print()
    print(df1[['Stat1','Stat2']].pipe( lambda x: x*2)) # multiply every element in table by 2
    print()
    df1['Stat1']=df1['Stat1'].pipe( lambda x: x*100)
    PandasUtil.PrintDF("df1",df1)


    print(df1[['Stat1','Stat2']].apply(lambda x: sum(x)*100))  # apply() by default takes entire column as list argument
    print()


    print(df1[['Stat1','Stat2']].applymap(lambda x: x+x/100))  # map will touch each element
    print()


    for key, value in df.iterrows():
        print(key)
        print( value.values )
        print( value.values.tolist())
        print()
    print()

    for key, value in df.iteritems():
        print(key)
        print( value.values )
        print( value.values.tolist())
        print()
    print()

    for row in df.itertuples():
        print(row)
        print(row.Stat2) # Named Tuple!
    print()


###################################################################################################################################
#
# pandas function application examples
#
###################################################################################################################################

FunctionApplicationExample()