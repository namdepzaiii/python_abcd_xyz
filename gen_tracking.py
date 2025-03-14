with open('proxy_nam.txt','r') as f:
    lst_proxy = f.read().splitlines()
lst_proxy1 = lst_proxy[:]

def getproxy():
    global lst_proxy1
    if not lst_proxy1:
        lst_proxy1 = lst_proxy[:]
    prox = lst_proxy1[0]
    lst_proxy1.pop(0)
    return prox


def browse_websitess():
    global global_header_s
    while 1:
        try:
            if len(global_header_s)> int(thread_rq/2+thread_rq+1):
                time.sleep(2)
            else:
                browse_websites()
        except Exception as e :
            print(e)
            time.sleep(3)
   
def browse_websites():
    global global_header_s
    proxy1 = getproxy()
    uuid = CreateProfileByCustomize(proxy1)
    ws = OpenProfile(uuid)
    if ws:
        with sync_playwright() as plr:
            browser = plr.chromium.connect_over_cdp(ws)
            context = browser.new_context()
            page = context.new_page()
            def handle_request(request):
                global global_header_s
                if 'https://webapis.ups.com/track/api/Track/GetStatus' in str(request.url):
                    cookie0 = {}
                    for c in context.cookies():
                        cookie0.update({c['name'] : c['value']})
                    with lock2:
                        global_header_s.append({
                            'proxy':proxy1,
                            'cookie':cookie0,
                            'headers':request.headers})
                    local.flag = True
                    
            local.flag = 0
            page.on('request', handle_request)
            page.goto(f'https://www.ups.com/track?track=yes&trackNums=1Z487A970351632{random.randint(100,999)}&loc=en_US&requester=ST/trackdetails')
            for i in range(30):
                if local.flag:
                        break
                else:
                    page.wait_for_timeout(1000)
                    
            browser.close()
            CloseProfile(uuid)
            CloseProfile(uuid)
            DeleteProfile(uuid)
            return uuid
    
from api_automation import *
import threading, requests
from pystyle import Colors
import time, random
from playwright.sync_api import sync_playwright
from datetime import datetime
from pymongo.mongo_client import MongoClient
with open('config.txt','r') as f:
    configs = f.read().split('"')
    thread_rq= int(configs[1])
    thread_hide= int(configs[3])
    uri= configs[5]
    dtb= configs[7]
    clt= configs[9]

with open('track_lst.txt','r') as f:
    track_lst = f.read().splitlines()
TrackingNumber = track_lst[0]
track_lst.pop(0)
    
local = threading.local()
client = MongoClient(uri)
db = client[dtb]
collection = db[clt]
g = Colors.light_green
b = Colors.light_blue
y = Colors.yellow
r = Colors.red
o = Colors.orange


lock = threading.Lock()
lock2 = threading.Lock()
sothutu = 1000
semaphore = threading.Semaphore(7)

def save(data):
    try :
        collection.insert_one(data)
    except Exception as e:
        print(f'{r}error mongodb: {y}{e}')
        
def kiemtra(track):
    global lst_data_tracking
    if track in lst_data_tracking:
        return False
    else :
        return True
    

lst_data_tracking = []
data1 = collection.find()
for dt in data1:
    if 'track_number' in dt:
        lst_data_tracking.append(dt['track_number'])
        
def gen(index):
    global global_header_s, sothutu
    global TrackingNumber, track_lst
    while True:
        datas = ''
        with lock:
            if global_header_s:
                datas = global_header_s[0]
                global_header_s.pop(0)
        if not datas:
            time.sleep(3)
            continue
        while True:
                with lock:
                    sothutu += 1
                    if sothutu > 9999:
                        TrackingNumber = track_lst[0]
                        track_lst.pop(0)
                        sothutu = 1000
                TrackingNumber123 = TrackingNumber[:-4]+str(sothutu)
                json_data = {
                    'Locale': 'en_US',
                    'TrackingNumber': [
                        TrackingNumber123,
                    ],
                    'Requester': 'st/trackdetails',
                    'returnToValue': '',
                }
                prox = datas['proxy'].split('|')
                proxy_url = f'http://{prox[3]}:{prox[4]}@{prox[1]}:{prox[2]}'
                proxies = {'https': proxy_url}
                try:
                        response = requests.post('https://webapis.ups.com/track/api/Track/GetStatus',timeout=10, proxies=proxies,params={'loc': 'en_US'},cookies=datas['cookie'],headers=datas['headers'],json=json_data)
                        response = response.json()
                        if response['trackDetails'] and not response['trackDetails'][0]['errorCode'] :#and response['trackDetails'][0]['progressBarType']=='InTransit':
                                if kiemtra(TrackingNumber123):
                                    colo = g
                                    data = [miles for miles in response["trackDetails"][0]["milestones"] if miles["isCurrent"]][0]
                                    current_time = datetime.now()
                                    formatted_time = current_time.strftime("%m/%d/%Y, %H:%M %p")
                                    time_t = f'{formatted_time} (Label Created)'
                                    if data['name'] != 'Label Created':
                                        if 'date' in data and 'time' in data:
                                            time_t = f"{data['date']}, {data['time']} (.)"
                                        else :
                                            time_t = f'{formatted_time} (..)'
                                                    
                                    json_data = {"track_number" : TrackingNumber123,
                                                "start" : data['name'],
                                                "ship_date" : time_t,
                                                "now" : data['name']}
                                    threading.Thread(target=save, args=(json_data,)).start()
                                else :
                                    colo = y                            
                                print(f'{colo}{index} | Success : {y}{TrackingNumber123} | {o}{data["name"]} | {b}{time_t}')
                                                        
                        else :
                            print(f'{y}{index} | {TrackingNumber123} | {sothutu}')
                            
                except Exception as e :
                            if 'referenced before assignment' in str(e):
                                pass
                            else :
                                if 'Expecting value' in str(e):
                                    print(f'{r}Die cookie{g} >> get new cookie')
                                else:
                                    print(f'{r}ERROR : {e}{g} >> get new cookie')
                                break
                    

global_header_s = []
for i in range(thread_rq):
    threading.Thread(target=gen, args=(i,)).start()
    
for i in range(thread_hide):
    threading.Thread(target=browse_websitess).start()
