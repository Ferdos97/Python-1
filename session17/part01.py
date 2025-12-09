## module    ==> (single file) json, datetime, math, random)
## library   ==> (some file in a folders) bs4
## framework ==> (some folders and libraries) django

import requests
import time

path = 'https://apiv2.nobitex.ir/v3/orderbook/USDTIRT'

result = requests.get(path)
last_price = result.json().get('lastTradePrice')
last_price = float(last_price)
print('last_price: ', last_price)

# if result.status_code == 200:
#     print(result.json().get('lastTradePrice'))
# else:
#     print(result.error)

same_count = 0

while True:
    time.sleep(2)
    result = requests.get(path)
    new_price = float(result.json().get('lastTradePrice'))
    # new_price = float(new_price)
    print('new_price: ', new_price)
    
    if new_price == last_price:
        same_count += 1
    else:
        same_count = 0

    if new_price > last_price * 1.01 or new_price < last_price * 0.99:
        print('market alert!!')

    if same_count == 3:
            user_input = input("Price stayed the same 3 times. Press 'q' to quit or Enter to continue: ").strip().lower()
            if user_input == 'q':
                print("Program stopped.")
                break
            else:
                same_count = 0
    
    last_price = new_price



