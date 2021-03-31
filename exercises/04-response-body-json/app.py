import requests
import json
time = {}
response = requests.get("https://assets.breatheco.de/apis/fake/sample/time.php")

time = response.json()
print(f"Current time: {time['hours']} hrs {time['minutes']} min and {time['seconds']} sec")