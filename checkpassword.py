#!/usr/bin/python3
import requests
import re
import hashlib

password = hashlib.sha1(bytes(input('Enter your password to check: '), encoding='utf-8')).hexdigest().upper()
hashResult = requests.get(f"https://api.pwnedpasswords.com/range/{password[:5]}")
result = re.sub('^[a-zA-Z0-9]{5}', '', password) in [re.sub(':[0-9]*', '', k) for k in hashResult.text.split('\r\n') ]
if result:
    print("\x1b[91mCOMPROMISED")
else:
    print('\x1b[92mSAFE')
