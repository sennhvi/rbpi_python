import urllib.request
import json

# Chinese Edition
# Using urllib.request and json library
key = "jcpe3hhnjnnvml7t"

query_city = input("Enter City location: ")
query_url = "https://api.seniverse.com/v3/weather/now.json?key=%s&location=%s&language=zh-Hans&unit=c"


def get_forecast(city):
    url = query_url % (key, city)
    print(url)
    req = urllib.request.Request(url)
    response = urllib.request.urlopen(req)
    return json.loads(response.read().decode("UTF-8"))


forecast = get_forecast(query_city)
print(forecast)
weather_dict = forecast['results'][0]
print("位置: %s\t 时区: %s\t 天气: %s\t 温度: %s\t" % (weather_dict['location']['name'],
                                               weather_dict['location']["timezone_offset"],
                                               weather_dict['now']['text'],
                                               weather_dict['now']['temperature'],
                                               ))
