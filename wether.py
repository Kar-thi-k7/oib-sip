import requests
city_name ='srikakulam'
Api_key ='83a01b4e0387b7abcb922609836d4079'
url =f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={Api_key}&units=metric'
response=requests.get(url)
if response.status_code==200:
    data=response.json()
    print('weather is',data['weather'][0]['description'])
    print('current temperature is',data['main']['temp'])
    print('current temperature  feels like is',data['main']['feels_like'])
    print('humidity is',data['main']['humidity'])