#!/usr/bin/python3
import requests
import re
import hashlib

password = hashlib.sha1(bytes(input('Enter your password to check: '), encoding='utf-8')).hexdigest().upper()
hashResult = requests.get(f"https://api.pwnedpasswords.com/range/{password[:5]}")
result = [k for k in hashResult.text.split('\r\n') if  re.sub('^[a-zA-Z0-9]{5}', '', password) in k ]
if result:
    print(f"\x1b[91mCOMPROMISED {result[0].split(':')[1]} times")
else:
    print('\x1b[92mSAFE!!!')
