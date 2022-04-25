import requests
import threading
import steammarket as sm
from data.data import weapons
import math
from time import sleep

def getcsmarketlistings(page=0, listings=23, cookie={'steamLoginSecure': '76561198258642304%7C%7C02BE9D6BFCD1032254A0DB2B65671FD87094B597'}):
    csreq = requests.get(f'https://steamcommunity.com/market/search/render/?start={page*listings}&search_descriptions=0&sort_column=default&sort_dir=desc&appid=730&norender=1&count={listings}', cookies=cookie)
    cslistings = csreq.json()
    csitems = {}
    for l in cslistings['results']:
        csitems[l['name']] = l['sell_price']
    return csitems

def getcsfloatlistings(page=0, listings=23):
    csfreq = requests.get(f'https://csgofloat.com/api/v1/listings', params={'page': page, 'limit': listings})
    csflistings = csfreq.json()
    csfitems = {}
    for l in csflistings:
        csfitems[l['item']['market_hash_name']] = l['price']
    return csfitems

def main():
    csfitems = {}
    for inx, x in enumerate(range(0, 45)):
        csfitems.update(getcsfloatlistings(page=x))
        print(f"Obtaining float.db Listings: {round((inx/45)*100)}%")

    for item in csfitems.keys():
        marketitem = sm.get_csgo_item(item, currency='USD')
        if marketitem != None:
            if 'lowest_price' in marketitem.keys():
                prof = abs(csfitems[item]/100 - float(marketitem['lowest_price'].replace('$', '').replace(',', '')))
                if csfitems[item]/100 < float(marketitem['lowest_price'].replace('$', '').replace(',', '')):
                    perc = 100 - ((csfitems[item]/100) / float(marketitem['lowest_price'].replace('$', '').replace(',', ''))) * 100
                else:
                    perc = 100 -(float(marketitem['lowest_price'].replace('$', '').replace(',', '')) / (csfitems[item]/100)) * 100
                print(f"{item} - Profit: ${round(prof, 3)} ({round(perc)}%)")
                print(f"  - CSGO Float Listing: ${csfitems[item]/100}")
                print(f"  - Steam Market Listing: ${float(marketitem['lowest_price'].replace('$', '').replace(',', ''))}")
        sleep(15)
if __name__ == "__main__":
    main()