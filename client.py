# client.py
import requests

#url = 'http://localhost:8000/test'
url = 'https://rcw-main-gzdya8fncpafgfdg.canadaeast-01.azurewebsites.net/'

response = requests.get(url)
response = response.json()
print(response['message'])

