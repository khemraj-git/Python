import requests

name = input("Enter your name: ").strip()

url = f"https://api.genderize.io?name={name}"
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data["gender"]:
        print(f"\n Predicted Gender: {data['gender'].capitalize()}")
        print(f"Probability: {data['probability']} (based on {data['count']} records)")
    else:
        print(f"\n Gender could not be predicted for '{name}'. Try a more common name.")
else:
    print("Failed to fetch data from API.")
