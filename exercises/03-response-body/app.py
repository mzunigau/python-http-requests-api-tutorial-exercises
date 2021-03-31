import requests

url = "https://assets.breatheco.de/apis/fake/sample/random-status.php"

reponse= requests.get(url)

if reponse.status_code == 200:
    print(reponse.text)
else:
    print("Something went wrong")