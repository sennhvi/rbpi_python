import requests
import json

API = "https://api.seniverse.com/v3/weather/now.json"
KEY = "jcpe3hhnjnnvml7t"
LANGUAGE = "zh-Hans"
UNIT = "c"


def query_weather(city):
    result = requests.get(API, params={
        'key': KEY,
        'location': city,
        'language': LANGUAGE,
        'unit': UNIT
    })
    return result.text


if __name__ == "__main__":
    response = query_weather("wuhan")
    query_result = json.loads(response)
    weather_dict = query_result['results'][0]
    print("位置: %s\t 时区: %s\t 天气: %s\t 温度: %s\t" % (weather_dict['location']['name'],
                                                   weather_dict['location']["timezone_offset"],
                                                   weather_dict['now']['text'],
                                                   weather_dict['now']['temperature'],
                                                   ))
