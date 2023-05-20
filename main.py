import sys
from study import study

username = sys.argv[1]
password = sys.argv[2]

successful = 0
if study(username, password):
    successful += 1
if successful != 0:
    print('success')
else:
    print('fail')
