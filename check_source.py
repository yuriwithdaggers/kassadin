import requests
import re

class Check:
    def __init__(self, region, nick):
        self.nick = nick
        regions = ('br', 'na', 'oce', 'las', 'lan', 'eune', 'euw', 'kr', 'jp', 'ru', 'tr')
        self.region = region.lower()
        if self.region not in regions:
            print("Região incorreta.")
            exit()
        self.url = f'https://lols.gg/en/name/checker/{self.region}/' + self.nick
        self.headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/73.0.3683.103 Safari/537.36"}

    def daysLeft(self):
        r = requests.get(self.url, headers=self.headers)
        r = r.text
        countDown = re.search("available in([^.]*)days", r)
        days = int(countDown.group(1))
        print(f'"{self.nick}" estará disponível em {days} dias.')
        
    
    def available(self):
        r = requests.get(self.url, headers=self.headers)
        r = r.text
        if 'is available!</h4>' in r or 'is available!</h2>' in r:
            print(f'"{self.nick}" está disponível!')
        elif f'is probably available!</h4>' in r:
            print(f'"{self.nick}" provavelmente está disponível!')
        else:
            self.daysLeft()

    