import requests
import json

def OpenProfile(uuid):
    try:
        x = requests.get('http://127.0.0.1:2222/openProfile?uuid='+uuid)
        result =  x.json()
        print(result)
        return result['data']['web_socket']
    except Exception as e:
        print("error get data ==>  " ,result)
        return None
    
OpenProfile('2231aa38-4b44-4f29-82a5-d1345eab8d67')



def CloseProfile(uuid):
    try:
        x = requests.get('http://127.0.0.1:2222/closeProfile?uuid='+uuid)
        result =  x.json()
        return result['result']
    except Exception as e:
        return None


def CheckingProfile(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/authorize?uuid='+uuid,headers=headers)
        
        result =  x.json()
        return result['status']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListProfile(page,limit):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/v1/browser/list?is_local=false',headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListConfigDefault(page,limit):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/get-list-config-default?page='+str(page)+"&limit="+str(limit),headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListStatus():
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/get-list-status',headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ListTag():
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/get-list-tag',headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def GetProfileByUuid(uuid):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get('http://127.0.0.1:2222/browser/get-profile-by-uuid?uuid='+uuid,headers=headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CreateProfileByDefault():
    try:
        body = {"defaultConfigId": 7124 }
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.post('http://127.0.0.1:2222/create-profile-by-default?is_local=false',headers=headers,json=body)
        result =  x.json()
        return result['content']['uuid']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def CreateProfileByCustomize(proxy):
    try:
        body = {
                "os": "win", 
                "browser": "chromium", 
                "version": "129",
                "userAgent": "",
                "canvas": "noise-e",   
                "webGLImage": "true",   
                "audioContext": "false",   
                "webGLMetadata": "true",    
                "clientRectsEnable": "true",   
                "noiseFont": "true",     
                "language": "vi,en-US;p=0.9",
                "resolution": "1920x1080",
                "command":"--lang=vi",
                "name" : "new profile 123",
                "proxy" :proxy
            }
        x = requests.post('http://127.0.0.1:2222/create-profile-custom',json=body)
        result =  x.json()
        return result['content']['uuid']
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def UpdateNote(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:2222/update-note',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def UpdateName(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:2222/update-name',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def SyncTag(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:2222/sync-tags',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def ChangeStatus(body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put('http://127.0.0.1:2222/change-status',headers=headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def DeleteProfile(uuid):
    try:
        headers = {"uuid_browser":[uuid]}
        x = requests.delete('http://127.0.0.1:2222/v1/browser/destroy',json=headers)
        result =  x.json()
        return result
    except Exception as e:
        print("error DeleteProfile ==>  " ,e)
        return None

def UpdateProxy(uuid, proxy1):
    try:
        proxy = f'HTTP|{proxy1[0]}|{proxy1[1]}|{proxy1[2]}|{proxy1[3]}'
        body = {"browser_update": [{"uuid": uuid,"proxy": proxy}]}
        x = requests.put('http://127.0.0.1:2222/v2/browser/proxy/update',json=body)
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def GET_Custom(url):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.get(url,headers)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def POST_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.post(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def PUT_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.put(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None

def DELETE_Custom(url,body):
    try:
        headers = {
                'Content-Type': 'text/html',
                'Connection': 'keep-alive',
                'Accept': '*/*',
                'Content-Type': 'application/json',
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
            }
        x = requests.delete(url,headers,json=body)
        
        result =  x.json()
        return result
    except Exception as e:
        print("error get data ==>  " ,e)
        return None