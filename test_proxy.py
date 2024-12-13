import requests
from pystyle import Colors

g = Colors.light_green
b = Colors.light_blue
y = Colors.yellow
r = Colors.red



with open('proxy_nam.txt','r') as f:
    lst = f.read().splitlines()
    
for pr in lst:
    try:
        proxy1 = pr.split('|')
        proxy ={'https': f'http://{proxy1[3]}:{proxy1[4]}@{proxy1[1]}:{proxy1[2]}'}
        response = requests.get('https://icanhazip.com/', proxies=proxy)
        print(f'{g}success: {response.text}')
    except Exception as e:
        print(f'{r}error: {pr} | {y}{e}')
