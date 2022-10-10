import requests
import time

URL = 'https://starsharks.com/go/api/market/sharks'
URL_statistic = 'https://starsharks.com/go/api/market/exchange-rate'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': '*/*'}
payload = {"class": [], "star": 0, "pureness": 0, "hp": [0, 200], "speed": [0, 200], "skill": [0, 200],
           "morale": [0, 200], "body": [], "parts": [], "rent_cyc": 0, "rent_except_gain": [0, 0],
           "skill_id": [0, 51400, 0, 0], "full_energy": False, "page": 1, "filter": "sell", "sort": "PriceAsc"}


def get_html(url):
    r = requests.post(url, headers=HEADERS, json=payload)
    return r


def statistic(url):
    res = requests.get(url, headers=HEADERS)
    return res


def parse():
    while True:
        time.sleep(0.5)
        list_price = []
        error = 0
        for i in range(1):
            html = get_html(URL)
            if html.status_code == 200:
                try:
                    for i_sharks in range(36):
                        if float(html.json()['data']['sharks'][i_sharks]['sheet']['sell_price']) < 0.54:
                            list_price.append(float(html.json()['data']['sharks'][i_sharks]['sheet']['sell_price']))
                            print(
                                f'https://starsharks.com/ru/market/sharks/{html.json()["data"]["sharks"][i_sharks]["sheet"]["shark_id"]}')
                except:
                    pass
            else:
                print('Error')
                error += 1
                print(error)
        second_list = sorted(set(list_price[:]))
        price_tokens = statistic(URL_statistic).json()
        bnb = price_tokens['data']['bnb']
        sea = price_tokens['data']['sea']
        # print('Парсер акулок. (цена)\n')
        # print(f'Курс токенов - 1 BNB =  {bnb}$ / 1 sea = {sea}$\n')
        for i in second_list:
            print(
                f'Прайс за акулу - {i} BNB ({round(i * bnb, 2)}$) / Кол-во акул за такую цену - {list_price.count(i)}')


parse()
