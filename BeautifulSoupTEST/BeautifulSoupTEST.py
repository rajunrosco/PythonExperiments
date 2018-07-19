import io
import sys
from bs4 import BeautifulSoup

def main(argv):
    htmlFile = open("TestData.html","r")
    htmlData = htmlFile.read()

    soup = BeautifulSoup(htmlData, 'html.parser')


    soupElement = soup.find('style')
    styletext = soup.style.text


    for link in soup.findAll('p'):
        currentclass = link.get("class")
        if(link.get('class') == ['story']):
            linktext = link.text
        pass

    sys.exit(0)


if __name__ == "__main__":
    main(sys.argv)
