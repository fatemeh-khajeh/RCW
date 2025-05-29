# client.py
import requests

url = 'http://localhost:8000/test'
data = {'value': ''}
response = requests.get(url,data)
response = response.json()
print(response['message'])

