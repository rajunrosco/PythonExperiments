import numpy as np
import pandas as pd
import PandasUtil

# pandas numpy series examples
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


###################################################################################################################################
#
# pandas numpy series examples
#
###################################################################################################################################
SeriesExample()