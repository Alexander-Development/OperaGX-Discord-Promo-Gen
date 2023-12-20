import requests
import random
import threading
import colorama
import time
import os

class counter:
    count = 0

def generate_string():
    string = ''
    for i in range(64):
        string += random.choice('0123456789abcdef')
    return string

def code():
    headers = {
        'authority': 'api.discord.gx.games',
        'accept': '*/*',
        'accept-language': 'de-DE,de;q=0.9,en-US;q=0.8,en;q=0.7',
        'content-type': 'application/json',
        'origin': 'https://www.opera.com',
        'referer': 'https://www.opera.com/',
        'sec-ch-ua': '"Opera GX";v="105", "Chromium";v="119", "Not?A_Brand";v="24"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'cross-site',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36 OPR/105.0.0.0 (Edition std-1)',
    }

    json_data = {
        'partnerUserId': generate_string(),
    }

    response = requests.post('https://api.discord.gx.games/v1/direct-fulfillment', headers=headers, json=json_data)
    if response.status_code == 200:
        promo = response.json()['token']
        promo = f'discord.com/billing/partner-promotions/1180231712274387115/{promo}\n'
        counter.count += 1
        print(colorama.Fore.GREEN + promo[:117] + ".. " + colorama.Fore.YELLOW + "Generated:" + colorama.Fore.RESET + f" [{counter.count}]")
        # add promo to file
        with open('promos.txt', 'a') as f:
            f.write(promo)
    else:
        print(colorama.Fore.RED + "Ratelimited, sleeping for 5 minutes...")
        time.sleep(300)

def worker():
    while True:
        try:
            code()
        except:
            pass


os.system('mode con: cols=140 lines=30')

threads = []
for i in range(1000):
    t = threading.Thread(target=worker)
    threads.append(t)
    t.start()