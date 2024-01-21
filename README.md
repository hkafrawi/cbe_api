# Central Bank of Egypt Foreign Currency API 
This API function provides a dictionary with the Official CBE FCY rates.

The Function **get_cbe_rate()** takes the following variables:

**start_date** -> a list containing day, month and year of the start date of the query
**end_date** -> a list containing day, month and year of the end date of the query
 **ccy** -> a list of the currencies you want the EGP rate for. The follwoing rates are currently available. 

| Input of Function | Currency|
| --- | --- |
| USD | US Dollars |
| EUR | EURO |
| GBP | Pound Sterling |
| CHF | Swiss FRANC |
| JPY | Japanese Yen |
| SAR | Saudi Riyal |
| KWD | Kuwaiti Dinar |
| AED | UAE Dirham |
| CNY | Chinese Yuan |

> You have to use the exact text in the Input Function Table.

The function outputs a dictionary with the Date, Currency, Buy Rate and Sell Rate as provided by the CBE. 

## Requirements
beautifulsoup4==4.12.3
certifi==2023.11.17
charset-normalizer==3.3.2
idna==3.6
requests==2.31.0
soupsieve==2.5
urllib3==2.1.0