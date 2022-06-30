from bs4 import BeautifulSoup
import requests

def getLinkHtml(url) :
        return BeautifulSoup(requests.get(url).content,'html5lib')

def getEthereumPriceInUsdDollar() :
        soup = getLinkHtml("https://coinmarketcap.com/currencies/ethereum/")
        dive_elements = soup.find_all('div')
        priceStr = [dive_element.contents for dive_element in dive_elements if dive_element.has_attr("class") and 'priceValue' in  dive_element.get("class")][0][0].text

	#the string of price is in this form e.g. $1,0618.22
        return float(priceStr[1] + priceStr[3:])

def getRialPriceInUsdDollar() :
        pass
