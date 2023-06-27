'''
Currency Converter
-------------------------------------------------------------
pip install requests
'''
import requests
import datetime
import pytz

currency_list = "CurrencyList.txt"  # Replace with your file name

choice = input("Do you want to read the currency list? (Y/N): ")

if choice.upper() == "Y":
    try:
        with open(currency_list, "r") as file:
            content = file.read()
        print("File content:")
        print(content)
    except FileNotFoundError:
        print("File not found!")
    except Exception as e:
        print("An error occurred:", str(e))


def convert_currency():
   init_currency = input('Enter an initial currency: ')
   target_currency = input('Enter a target currency: ')

   while True:
       try:
           amount = float(input('Enter the amount: '))
       except:
           print('The amount must be a numeric value!')
           continue

       if not amount > 0:
           print('The amount must be greater than 0')
           continue
       else:
           break

   url = ('https://api.apilayer.com/fixer/convert?to='
          + target_currency + '&from=' + init_currency +
          '&amount=' + str(amount))

   payload = {}
   headers = {'apikey': 'Ibr1ouTT2mUhdsMVKZ65wkKPz16LCvmQ'}
   response = requests.request('GET', url, headers=headers, data=payload)
   status_code = response.status_code

   if status_code != 200:
       print('Uh oh, there was a problem. Please try again later')
       quit()

   result = response.json()
   print('Conversion result: ' + str(result['result']))


# Get the current GMT time
   gmt_timezone = pytz.timezone('GMT')
   gmt_time = datetime.datetime.now(gmt_timezone).strftime("%Y-%m-%d %H:%M:%S")
   print("(GMT-0) local time:", gmt_time)

if __name__ == '__main__':
   convert_currency()