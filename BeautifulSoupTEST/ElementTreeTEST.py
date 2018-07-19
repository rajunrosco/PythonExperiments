import io
import sys
from xml.etree import ElementTree as ET

XMLraw = """<?xml version="1.0"?>
<data>
    <country name="Liechtenstein">
        <rank>1</rank>
        <year>2008</year>
        <gdppc>141100</gdppc>
        <neighbor name="Austria" direction="E"/>
        <neighbor name="Switzerland" direction="W"/>
    </country>
    <country name="Singapore">
        <rank>4</rank>
        <year>2011</year>
        <gdppc>59900</gdppc>
        <neighbor name="Malaysia" direction="N"/>
    </country>
    <country name="Panama">
        <rank>68</rank>
        <year>2011</year>
        <gdppc>13600</gdppc>
        <neighbor name="Costa Rica" direction="W"/>
        <neighbor name="Colombia" direction="E"/>
    </country>
</data>
"""


def main(argv):
    root = ET.fromstring( XMLraw )

    countries = root.findall('country')
    for currentcountry in countries:
        if( ET.iselement(currentcountry) ):
            print( ET.tostring(currentcountry, encoding='unicode' ))
            print('\n')


if __name__ == "__main__":
    main(sys.argv)