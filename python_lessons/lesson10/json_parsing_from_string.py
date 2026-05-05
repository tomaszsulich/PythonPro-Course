import requests
import json

dogapi_url = r"https://dogapi.dog/api/v2/breeds/2"
res = """{
  "data": [
    {
      "id": "f9643a80-af1d-422a-9f15-18d466822053",
      "type": "breed",
      "attributes": {
        "name": "Caucasian Shepherd Dog",
        "description": "The Caucasian Shepherd dog is a serious guardian breed and should never be taken lightly.",
        "hypoallergenic": false,
        "life": {
          "min": 15,
          "max": 20
        },
        "male_weight": {
          "min": 50,
          "max": 100
        },
        "female_weight": {
          "min": 50,
          "max": 100
        }
      }
    },
    {
      "id": "dc5e84f8-9151-4624-836c-25b4e313118b",
      "type": "breed",
      "attributes": {
        "name": "Bouvier des Flandres",
        "description": "They don't build 'em like this anymore.",
        "hypoallergenic": false,
        "life": {
          "min": 10,
          "max": 14
        },
        "male_weight": {
          "min": 30,
          "max": 40
        },
        "female_weight": {
          "min": 25,
          "max": 35
        }
      }
    }
  ],
  "meta": {
    "pagination": {
      "current": 1,
      "records": 9
    }
  },
  "links": {
    "self": "https://dogapi.dog/api/v2/breeds",
    "current": "https://dogapi.dog/api/v2/breeds?page[number]=1",
    "next": "https://dogapi.dog/api/v2/breeds?page[number]=2",
    "last": "https://dogapi.dog/api/v2/breeds?page[number]=2"
  }
}
No links
"""

decoded_json = json.loads(res)
# w konsoli się odpali, w Visual Studio Code nie
print(decoded_json, type(decoded_json))