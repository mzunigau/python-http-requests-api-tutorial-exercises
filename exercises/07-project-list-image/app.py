import requests

# your code here
response = requests.get('https://assets.breatheco.de/apis/fake/sample/project_list.php')

project = response.json()

print(project[-1]["images"][-1])