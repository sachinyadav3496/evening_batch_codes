import time
import requests
import random

token = "EAAHUUCoZApSUBADTjiOyz1ZASjxc19omfrSYlZBAMLZAZCPYzZBmZAnfJGtBqoF7yiZB0Kcj9ZBzsSTAADb1mquaC8pb3ucWaiZBU47Bokp4Ho5wv1jFL3fHTbwJj3BVFbvxLUxvLViR5ZBNcIC7uY1MRbeVWtHDfI1ukYUSrVOMhUnLT3XeZAfKL9Llckq4kZC4quEZBN07oLV5yl0gZDZD"


req = 'pepsi?fields=posts'


#print("Request url = https://graph.facebook.com/v2.10/"+req,{'acess_token' : token})


url = "https://graph.facebook.com/v2.10/"+req+',acess_token = '+token

def req_facebook(req) :

    r = requests.get(url)

    return r

results = req_facebook(req).json()



print(results)
"""

data = []

results = results['posts']

i = 0

while True:
    try :
        
        time.sleep(random(2,5))
        
        data.extend(results['data'])
        
        r = requests.get(results['paging']['next'])
        results = r.json()

        i += 1
        if i > 10 :
            break

    except :
        print("done")
        break

print(data)
"""
