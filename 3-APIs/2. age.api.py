# age predictor using agify api

import requests
name = input("enter a name")

url = f"https://api.agify.io?name={name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    print(f"predicted age fo r '{data['name']}' is: {data['age']} years old (based on {data['count']} records)")
else:
    print("failed to fetch data from api")