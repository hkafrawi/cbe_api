import requests
from bs4 import BeautifulSoup

currencies = {"USD":"US+Dollar",
              "EUR":"Euro",
              "GBP":"Pound+Sterling",
              "CHF":"Swiss+Franc",
              "JPY":"Japanese+Yen",
              "SAR":"Saudi+Riyal",
              "KWD":"Kuwaiti+Dinar",
              "AED":"UAE+Dirham",
              "CNY":"Chinese+yuan"}

def print_payload(inputs:list):
    input_text = ""
    for input in inputs:
        input_text += f"&SelectedSelectOptions={currencies[input]}"
    for input in inputs:
        input_text += f"&multiselect_multipleSelectID={currencies[input]}"
    return input_text

def get_cbe_rate(start_date: list=[1,1,2024],end_date: list=[15,1,2024],ccy:list = ["USD"]):
    
    #start_date -> [dd,mm,yyyy]
    #end_date -> [dd,mm,yyyy]
    url = "https://www.cbe.org.eg/api/statistics/GetHistoricalData"

    payload = f"__RequestVerificationToken=3BSvkIrU2RXyPkfvelFrXZnW030Ag26_gk2zIxPURokFgBYJqY6MhNvn2seRJSFUfarZlmfSrncDtc6DeDBMBgOoo0ZmC-7zuy6MvaY_fys1&uid=54010050-4405-48c8-9c56-fe19328e9e65&DataSourceId=AAE2ED195E0649EB9C40FF484EC851B6&FallbackUrl=%2Fen%2Feconomic-research%2Fstatistics%2Fexchange-rates%2Fhistorical-data&LanguageName=en&FromDateRaw={start_date[0]:02d}%2F{start_date[1]:02d}%2F{start_date[2]}&ToDateRaw={end_date[0]:02d}%2F{end_date[1]:02d}%2F{end_date[2]}{print_payload(ccy)}&SubmitAction=1"
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
    if r.status_code == 200:
        soup = BeautifulSoup(r.text, 'html.parser')
        table = soup.find('table', class_='table-comp')

        if table:
            rows = table.find_all('tr', class_='content-height')[1:]  # Skip the header row
            result = []

            for row in rows:
                columns = row.find_all('td', class_='column-width table-cell')
                date = columns[0].text.strip()
                currency = columns[1].text.strip()
                buy_rate = float(columns[2].text.strip())
                sell_rate = float(columns[3].text.strip())

                data = {
                    'date': date,
                    'currency': currency,
                    'buy_rate': buy_rate,
                    'sell_rate': sell_rate
                }

                result.append(data)

            return result

    print(f"Error: {r.status_code} - {r.text}")
    return None

# Save the extracted data to a JSON file
