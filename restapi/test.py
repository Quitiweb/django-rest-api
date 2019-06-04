import os
import requests

# url = 'http://127.0.0.1:8000/api/v1/1/'
url = 'http://127.0.0.1:8000/snippets/api/1/'
resp = requests.get(url)
assert resp.status_code == 403

# api_key = 'xbgLK0wM.NE4gL4BLFBRX7ZUkhCH0ziMT1lK6R3m5'
# auth = f"Api-Key {api_key}"
api_key = '2c27630c9bdf50f037344100788c433ea243f314'
auth = f"Token {api_key}"

resp = requests.get(url, headers={"Authorization": auth})
assert resp.status_code == 200

print(resp.json())
