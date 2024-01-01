import requests
from colorama import Fore
import httpx
import string
import time
from os import system
import random
import threading

def check_username():  
  totalchecked = 0
  available = 0
  banned = 0
  invalid = 0
  ratelimits = 0
  claimed = 0
  ssid = input(f"SSID: ")
  target = input(f"Webhook: ")
  length = input(f"Length of users: ")
  gh = 'u have a small dick'
  gh2 = 'u still have a small dick'
  while True:

    while True:
      username = ''.join(random.choice(string.ascii_lowercase) for _ in range(int(length)))
      Headers = {
          "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63", #Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36 Edg/110.0.1587.63
      }
      message = f'@{username} is available'
      message2 =f'@{username} got claimed! Going to checker mode!'
      try:
          b=httpx.get(f'https://www.tiktok.com/@{username}', headers=Headers)
      except:
       pass
      system(f"title @{username} - Checked: {totalchecked} - Available: {available} - Claimed: {claimed} - Banned: {banned} - Invalid: {invalid} - Rate Limits: {ratelimits}")
      if b.status_code == 404:
          h = {
              "accept-encoding": "gzip",
              "connection": "Keep-Alive",
              "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
              "cookie": f"sessionid={ssid};",
              "host": "api16-normal-c-useast1a.tiktokv.com",
              "sdk-version": "2",
              "user-agent": "okhttp/3.10.0.1",
          }
          try:
           r = httpx.post('https://api16-normal-c-useast1a.tiktokv.com/passport/login_name/update/?iid=7212692500116604678&device_id=6659737520265856513&ac=wifi&channel=googleplay&aid=1233&app_name=musical_ly&version_code=280704&version_name=28.7.4&device_platform=android&ab_version=28.7.4&ssmix=a&device_type=SM-G988N&device_brand=samsung&language=en&os_api=28&os_version=9&openudid=71f0a684a6becf1a&manifest_version_code=2022807040&resolution=1280*720&dpi=240&update_version_code=2022807040&_rticket=1679431672953&app_type=normal&sys_region=US&mcc_mnc=46002&timezone_name=Africa%2FHarare&carrier_region_v2=310&app_language=en&carrier_region=GR&ac2=wifi5g&uoo=0&op_region=GR&timezone_offset=7200&build_number=28.7.4&host_abi=arm64-v8a&locale=en&region=US&ts=1679431675&cdid=fc306c3b-8e93-4988-a20b-27fc9fac77f4&support_webview=1&okhttp_version=4.1.120.12-tiktok&use_store_region_cookie=1',headers=h, data=f'login_name={username}', timeout=5000)
           print(r.text)
          except:
           pass
          if '1330' in r.text:
              available += 1
              totalchecked += 1
              print(f'{Fore.MAGENTA}@{username}{Fore.RESET} = {Fore.GREEN}available!{Fore.RESET}')

              url = target

              time.sleep(0.2)
              pyload = {"content": message, "username": gh}
              w = requests.post(url, data=pyload)
          elif 'success' in r.text:
              claimed += 1
              totalchecked += 1
              print(f'{Fore.MAGENTA}@{username}{Fore.RESET} = {Fore.GREEN}Claimed successfully! Going to checker mode!{Fore.RESET}')
              url = target
              pyload = {"content": message2, "username": gh2}
              w = requests.post(url, data=pyload)
          elif '1024' in r.text:
              banned += 1
              totalchecked += 1
          elif '1027' in r.text:
              invalid += 1
              totalchecked += 1
          elif 'Maximum number of attempts reached. Try again later.' in r.text:
              totalchecked += 1
              ratelimits += 1
              time.sleep(1500)

      elif b.status_code == 200:
          totalchecked += 1
          time.sleep(1)
      elif b.status_code == 302:
          totalchecked += 1
          ratelimits += 1
          time.sleep(120)

def main():
    num_threads = 100
    threads = []

    for i in range(num_threads):
        t = threading.Thread(target=check_username)
        threads.append(t)
        t.start()

    for t in threads:
        t.join()


if __name__ == '__main__':
    main()