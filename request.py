import requests
response = requests.get('http://api.open-notify.org/astros.json')
if response.status_code == 200:
    data = response.json()
    print("Number of people in space:", data['number'])
    print("People in space:")
    for person in data['people']:
        print(person['name'], "on the", person['craft'])
else:
    print("Failed to retrieve data:", response.status_code)