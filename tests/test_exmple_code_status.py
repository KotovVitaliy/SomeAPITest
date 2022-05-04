import requests


def test_200():
    r = requests.get("https://playground.learnqa.ru/api/hello")
    assert r.status_code == 200, "Wrong status code"


def test_500():
    r = requests.get("https://playground.learnqa.ru/api/get_500")
    assert r.status_code == 200, "Wrong status code"


def test_404():
    r = requests.get("https://playground.learnqa.ru/fwefew")
    assert r.status_code == 404


def test_304():
    ololo(4, a=7)


def ololo(b, a=4):
    print(b)
    print(a)
