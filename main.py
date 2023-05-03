import os
import time
import sys
from study import study

ua = os.getenv('UA','Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36 Edg/106.0.1370.42')
# accounts = getAccounts()

username = sys.argv[1]
password = sys.argv[2]

successful = 0
if study(username, password, ua):
    successful += 1
if successful != 0:
    print('success')
else:
    print('fail')