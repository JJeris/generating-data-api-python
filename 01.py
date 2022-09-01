import requests

url = "https://simple-books-api.glitch.me/status"

payload = {}
headers = {}

response = requests.request("GET", url, headers=headers, data=payload)

print(response.text)
