import ssl
import json
from urllib import request, parse

API = "https://api.seniverse.com/v3/weather/now.json"
KEY = "jcpe3hhnjnnvml7t"
LANGUAGE = "zh-Hans"
UNIT = "c"

context = ssl.SSLContext(ssl.PROTOCOL_TLSv1)


def query_weather(city):
    params = parse.urlencode({
        'key': KEY,
        'location': city,
        'language': LANGUAGE,
        'unit': UNIT
    })
    req = request.Request('{api}?{params}'.format(api=API, params=params))
    response = request.urlopen(req, context=context).read().decode('UTF-8')
    return response


if __name__ == "__main__":
    query_response = query_weather("wuhan")
    query_result = json.loads(query_response)
    weather_dict = query_result['results'][0]
    print("位置: %s\t 时区: %s\t 天气: %s\t 温度: %s\t" % (weather_dict['location']['name'],
                                                   weather_dict['location']["timezone_offset"],
                                                   weather_dict['now']['text'],
                                                   weather_dict['now']['temperature'],
                                                   ))
