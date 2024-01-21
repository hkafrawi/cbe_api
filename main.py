import requests
import json

def get_cbe_rate():
    url = "https://www.cbe.org.eg/api/statistics/GetHistoricalData"

    payload = "__RequestVerificationToken=3BSvkIrU2RXyPkfvelFrXZnW030Ag26_gk2zIxPURokFgBYJqY6MhNvn2seRJSFUfarZlmfSrncDtc6DeDBMBgOoo0ZmC-7zuy6MvaY_fys1&uid=54010050-4405-48c8-9c56-fe19328e9e65&DataSourceId=AAE2ED195E0649EB9C40FF484EC851B6&FallbackUrl=%2Fen%2Feconomic-research%2Fstatistics%2Fexchange-rates%2Fhistorical-data&LanguageName=en&FromDateRaw=15%2F01%2F2024&ToDateRaw=21%2F01%2F2024&SelectedSelectOptions=US+Dollar&multiselect_multipleSelectID=US+Dollar&SubmitAction=1"
    headers = {
    'authority': 'www.cbe.org.eg',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/x-www-form-urlencoded; charset=UTF-8',
    'cookie': 'SC_ANALYTICS_GLOBAL_COOKIE=17ba0376fb6e4af59f9c604e9916055c|False; 14565=1703330632687-120938919; cbe^#lang=en; shell^#lang=en; ASP.NET_SessionId=h1j0ags3o1oi2oxyslgqafhq; TS01dc4fc6=01cfa9e5ba364807cceba7f536a227e82febcc04b944b8085f2bd7085be1ab092347cb13545fa764f62e7b559412d4f3aabd68e2dc; __RequestVerificationToken=i-jAIuZ8Wom9Gapmvmyropj5aKbml1iIzwd0VQAlWxntjiEIpEEgI4fgDDvedwXVTruvGd8WCzfLTTLisKuwnjJ1HVNPfaC9KjV5DZAOU501; 145603=nSOXPKoGnpLbXhnMbEK0QmyX4/pbvEy4paaZh0v93JAS/PgxDWep3rmQJQhfNFe91d45dMkT+iFm6BhokZ9IcBnWjZeidLlnLSk4QRQm2LliSyfmuol9oSmvvXhtc7vEHHt4XG8EVwozAtnUPR40p2io9X8P8oReAmv7btDXWTFqsxlE',
    'origin': 'https://www.cbe.org.eg',
    'referer': 'https://www.cbe.org.eg/en/economic-research/statistics/exchange-rates/historical-data',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Microsoft Edge";v="120"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36 Edg/120.0.0.0',
    'x-requested-with': 'XMLHttpRequest'
    }

    r = requests.post(url,headers=headers,data=payload)
    return r.text
print(get_cbe_rate())
