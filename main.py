import steammarket as sm
import requests
import threading
from data.data import weapons

def main():
    item = 'CZ75-Auto | Twist (Field-Tested)'
    a = sm.get_csgo_item(item, currency='USD')
    for i in range(0, 4):
        b = requests.get("https://csgofloat.com/api/v1/listings", params={'page': i})
        for item in b.json():
            print(item['item']['item_name'])

if __name__ == "__main__":
    main()