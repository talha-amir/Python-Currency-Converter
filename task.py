import requests
sample = "https://free.currconv.com/api/v7/convert?q=PKR_USD,USD_PKR&compact=ultra&apiKey="
api_key = "ff0ff8b8fa69d4fa532b"
from_ = "USD"
to = "PKR"
query = from_+"_"+to
key = "&compact=ultra&apikey="+api_key

url = 'https://api.currconv.com/api/v7/convert?q='+query+key
# Request for list  of all currencies
req_currencies = requests.get("https://free.currconv.com/api/v7/currencies?apiKey="+api_key)
# Request for list of all countries
req_countries = requests.get("https://free.currconv.com/api/v7/countires?apiKey="+api_key)
# Request for getting exchange rates
url = sample+api_key
req_rates = requests.get(url)
rates = req_rates.json()
rate =  rates['USD_PKR']
num = eval(input("Enter Amount to convert into USD = "))
print("Amounnt in PKR =",num*rate)          
