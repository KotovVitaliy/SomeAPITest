from requests import Response


class Asserts:
    def assert_status_code(self, r: Response, expected: int):
        assert r.status_code == expected, "Status code not equals expected."


asserts = Asserts()