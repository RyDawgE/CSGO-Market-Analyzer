import steammarket as sm
import requests
import threading
from data.data import weapons

def main():
    steamcookie = {'steamLoginSecure': '76561198258642304%7C%7C02BE9D6BFCD1032254A0DB2B65671FD87094B597'}
    csgameid = '730'
    startlisting = '0'
    listingcount = '50'
    req = requests.get(f'https://steamcommunity.com/market/search/render/?start={startlisting}&search_descriptions=0&sort_column=default&sort_dir=desc&appid={csgameid}&norender=1&count={listingcount}', cookies=steamcookie)
    listings = req.json()

    for listing in listings['results']:
        print(listing['name'] + listing['sell_price_text'])










    # for i in [0]:
    #     csfloatlistings = requests.get("https://csgofloat.com/api/v1/listings", params={'page': i})
    #     for listing in csfloatlistings.json():
    #         itemhash = listing['item']['market_hash_name']
    #         marketitem = sm.get_csgo_item("AWP | Dragon Lore (Factory New)", currency='USD')
    #         print(marketitem)
    #             #print(dict(marketitem)['lowest_price'])
    #             #print(f"{itemhash} - Profit Margin: {str(abs(float(marketitem['lowest_price'].replace('$', '')) - float(listing['price']/100)))}")


if __name__ == "__main__":
    main()