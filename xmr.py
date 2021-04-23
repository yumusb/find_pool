import requests
import re
import json

def c3pool(address):
    url = "https://api.c3pool.com/miner/{0}/stats".format(address)
    res = requests.get(url,timeout=5).json()
    if(res['lastHash'] == None):
        return False
    else:
        print(res)
        return True
def supportxmr(address):
    url = "https://supportxmr.com/api/miner/{0}/stats".format(address)
    res = requests.get(url,timeout=5).json()
    if(float(res['validShares']) == 0):
        return False
    else:
        print(res)
        return True
def f2pool(address):
    url = "https://www.f2pool.com/xmr/{0}".format(address)
    res = re.findall('<div class="line">[.\n]?(.*)[.\n]?</div>',requests.get(url,timeout=5).text)
    for x in res:
        if(float(x)>0):
            print(x)
            return True
    return False
def minexmr(address):
    url = "https://minexmr.com/api/main/user/stats?address={0}".format(address)
    res = requests.get(url,timeout=5).content.strip()
    res = json.loads(res)
    if('error' in res.keys()):
        print(res['error'])
        return False
    else:
        if(res['balance'] != None or res['paid'] != None):
            print(res)
            return True
        else:
            return False
def nanopool(address):
    url = "https://xmr.nanopool.org/api/v1/user/{0}".format(address)
    res = requests.get(url,timeout=5).json()
    if(res['status']==False):
        return False
    else:
        print(res)
        return True
def main():
    address = '43ZBkWEBNvSYQDsEMMCktSFHrQZTDwwyZfPp43FQknuy4UD3qhozWMtM4kKRyrr2Nk66JEiTypfvPbkFd5fGXbA1LxwhFZf'
    pools = ['f2pool','c3pool','minexmr','supportxmr','nanopool']
    for f in pools:
        try:
            if(eval('{0}("{1}")'.format(f,address))):
                print("[+] {0} found !".format(f))
            else:
                print("[-] {0} not found !".format(f))
        except:
            print("[*] {0} is error".format(f))
if __name__ == '__main__':
    main()
