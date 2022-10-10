import requests
import time

URL = 'https://starsharks.com/go/api/market/sharks'
URL_statistic = 'https://starsharks.com/go/api/market/exchange-rate'
HEADERS = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.74 Safari/537.36',
    'accept': '*/*'}
payload = {"class": [], "star": 0, "pureness": 0, "hp": [0, 200], "speed": [0, 200], "skill": [0, 200],
           "morale": [0, 200], "body": [], "parts": [], "rent_cyc": 0, "rent_except_gain": [0, 0],
           "skill_id": [0, 0, 0, 0], "full_energy": False, "page": 1, "filter": "rent", "sort": "PriceAsc"}


def get_html(url):
    r = requests.post(url, headers=HEADERS, json=payload)
    return r


def statistic(url):
    res = requests.get(url, headers=HEADERS)
    return res


def parse():
    list_price = []
    error = 0
    for i in range(get_html(URL).json()['data']['total_page']):
        time.sleep(0.65)
        html = get_html(URL)
        payload['page'] += 1
        if html.status_code == 200:
            try:
                count = len(html.json()['data']['sharks'])
                for i_sharks in range(count):
                    list_price.append(float(html.json()['data']['sharks'][i_sharks]['sheet']['rent_except_gain']))
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
    print('Парсер акулок. (аренда)\n')
    print(f'Курс токенов - 1 BNB =  {bnb}$ / 1 sea = {sea}$\n')
    for i in second_list:
        print(f'Прайс за аренду - {i} sea ({round(i * sea, 2)}$) / Кол-во акул за такую цену - {list_price.count(i)}')


parse()
