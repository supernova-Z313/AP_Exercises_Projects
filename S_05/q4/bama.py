from urllib.request import urlopen, Request
import requests
import json


url = 'https://bama.ir/api/car/search'

cookies = {
    'auth.strategy': '',
    'CSRF-TOKEN-BAMA-COOKIE': 'CfDJ8FUD4k3_87RCpQGDMQAsah2rczaKViI9XxIDYeULyPYRfjZ7b9GouoWu_ILsWWP-nd3-rXq-2mET3cOikXtZrp1QjO1xMmMlKRbRpCNqW5aLUPPex8bl6MQHnuwGSi01prDJRJpai0R2_6LooiQHl1Q',
}

headers = {
    'authority': 'bama.ir',
    'accept': 'application/json, text/plain, */*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'no-cache',
    # Requests sorts cookies= alphabetically
    # 'cookie': 'auth.strategy=; CSRF-TOKEN-BAMA-COOKIE=CfDJ8FUD4k3_87RCpQGDMQAsah2rczaKViI9XxIDYeULyPYRfjZ7b9GouoWu_ILsWWP-nd3-rXq-2mET3cOikXtZrp1QjO1xMmMlKRbRpCNqW5aLUPPex8bl6MQHnuwGSi01prDJRJpai0R2_6LooiQHl1Q',
    'pragma': 'no-cache',
    'referer': 'https://bama.ir/car',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'sec-gpc': '1',
    'traceparent': '00-685e6d8e7d17757ff5c53169558e622e-b37f6f827e81a67f-01',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.5005.61 Safari/537.36',
}


# response = requests.get(url, cookies=cookies, headers=headers)

request = Request(url, headers=headers)
response = urlopen(request).read()
data = json.loads(response)
cars = data['data']['ads']

for car in cars:
    print(car['detail']['title'])
    print(car['detail']['time'])
    print(f"آدرس: {car['detail']['location']}")
    print(f"کارکرد: {car['detail']['mileage']}") 
    print(f"مدل: {car['detail']['year']}")
    print(f"قیمت: {car['price']['value']}")
    print("---------------------------------------")