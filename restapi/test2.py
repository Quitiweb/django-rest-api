import requests

url = 'http://127.0.0.1:8000/snippets/api/1/'

api_key = '2c27630c9bdf50f037344100788c433ea243f314'
auth = f"Token {api_key}"
headers = {"Authorization": auth}

resp = requests.get(url, headers=headers)

print(resp.json())
