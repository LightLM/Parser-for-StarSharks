import requests
import time
URL_statistic = 'https://starsharks.com/go/api/market/exchange-rate'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': '*/*'}

def statistic(url):
    res = requests.get(url, headers=HEADERS)
    return res


print('Курс.\n')
my_money = int(input('Введи сколько у тебя: '))
while True:
    time.sleep(1)
    price_tokens = statistic(URL_statistic).json()
    bnb = price_tokens['data']['bnb']
    sea = price_tokens['data']['sea']
    print(f'У тебя - {round(sea*my_money,2)}$')
    print(f'Курс токенов - 1 BNB =  {bnb}$ / 1 sea = {sea}$\n')