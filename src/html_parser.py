import requests
import json


def html_kernel():
    response = requests.get('https://www.dongchedi.com/auto/series/690')

    with open('index.html', 'w', encoding='utf-8') as file:
        json.dump(response.text, file, indent=4, ensure_ascii=False)

    print(response.text)