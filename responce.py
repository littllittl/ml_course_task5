import requests

file = open("text.txt", "rb")
data = file.read()
response = requests.post('http://0.0.0.0:8000/', data=data)
print(response.text)