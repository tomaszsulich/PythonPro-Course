import requests
import json

dogapi_url = r"https://dogapi.dog/api/v2/breeds/2"
res = requests.get(dogapi_url)
# w konsoli mamy response 404
print(res)
dir(res)
res.ok