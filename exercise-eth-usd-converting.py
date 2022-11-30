import converts

symbols = {0 : 'eth', 1 : 'usd'}

inputSymbol = None
outputSymbol = None

def getConvertCode() :
	typed = input("for eth to usd type 1 / for usd to eth type 2 : ")
	try :
		convert_code = int(typed)

		if convert_code == 1 or convert_code == 2 :
			global inputSymbol, outputSymbol
			inputSymbol = symbols[convert_code -1]
			outputSymbol = symbols[abs(2 - convert_code)]
			return

		else :
			print("INVALID INPUT.")
			getConvertCode()

	except ValueError :
		print("INVALID INPUT.")
		getConvertCode()


def getCurrencyValue() :

	currencyStr = input(f"insert value in {inputSymbol} : ")

	try :
		return float(currencyStr)

	except ValueError :
		print("can't convert input value , you must input numerical value")
		getCurrencyValue()


getConvertCode()
value  = getCurrencyValue()

def ethInUsd() :
        return converts.getEthereumPriceInUsdDollar()

ethToUsd = lambda eth : eth * ethInUsd()
usdToEth = lambda usd : usd / ethInUsd()

print(f"\netherium price = {ethInUsd()}$")
print(f"\n{inputSymbol} = {value}\n{outputSymbol} = {ethToUsd(value) if inputSymbol == 'eth' else usdToEth(value)}")

