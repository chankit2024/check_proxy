import requests
import sys

sys.stdout.reconfigure(encoding='utf-8')

proxies = {
    'http': 'http://your_proxy_address:your_proxy_port',
    'https': 'https://your_proxy_address:your_proxy_port',
}

url = 'http://www.google.com'

try:
    response = requests.get(url, proxies=proxies, timeout=10)
    
    if response.status_code == 200:
        print("Proxy ทำงานได้")
    else:
        print(f"Proxy ไม่สามารถเข้าถึงได้, สถานะ: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"เกิดข้อผิดพลาดในการเชื่อมต่อ: {e}")
