import pytest
from core.request import request
from core.asserts import asserts


data = [
    ("GET", {"a": "b", "g": "ololo"}),
    ("POST", {"a": "b"}),
    ("DELETE", {"a": "b"}),
    ("PUT", {"a": "b"}),
    ("PATCH", {"a": "b"}),
    ("PATCH", {}),
    ("DELETE", {}),
]


@pytest.mark.parametrize('method, request_data', data)
def test_check_request_data(method, request_data):
    r = request.do(method=method, uri="/check_type", data=request_data)
    asserts.assert_status_code(r=r, expected=200)

    for key in request_data:
        value = request_data[key]
        expected_text = f"{key} = {value}"
        assert expected_text in r.text, f"Cannot find {expected_text} in {r.text}"
