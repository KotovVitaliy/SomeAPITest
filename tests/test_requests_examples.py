import requests


# def test_get_request():
#     r = requests.get("https://playground.learnqa.ru/api/hello")
#     print(r.text)

def test_auth_request_negative():
    r = requests.post(
        "https://playground.learnqa.ru/ajax/chrome/pass/",
        headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        },
        data={"login": "ololo@mail.ru", "pass": "3a876"}
    )
    encoded_response = r.json()
    assert "error" in encoded_response, "Expected to see 'error' in the message"
    assert encoded_response["error"] == "Неправильный пароль"


def test_auth_request_positive():
    response = requests.post(
        "https://playground.learnqa.ru/ajax/chrome/pass/",
        headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        },
        data={"login": "ololo@mail.ru", "pass": "3a876b"}
    )
    encoded_response = response.json()
    key = "success"
    assert key in encoded_response, "Expected to see 'success' in the message"
    assert encoded_response[key] == "!"
    assert "chrome_auth_cookie" in response.cookies, "Cannot find auth cookie"

    cookie_value = response.cookies["chrome_auth_cookie"]

    response2 = requests.get(
        "https://playground.learnqa.ru/ajax/chrome/need_say_hello",
        headers={
            "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.127 Safari/537.36"
        },
        cookies={"chrome_auth_cookie": cookie_value}
    )

    print(response2.text)


# ?? -> login / pass => user_id 1 | wef34r34cw
# ?? -> login / pass => user_id 2 | wef34f3fqq => content
# ?? -> login / pass => ?? | wef34f3fgg