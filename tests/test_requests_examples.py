import requests


def test_get_request():
    r = requests.get("https://playground.learnqa.ru/api/hello")
    print(r.text)
