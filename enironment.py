import os


class Environment:
    DOMAINS = {
        "dev": "https://playground.learnqa.ru/api_dev",
        "prod": "https://playground.learnqa.ru/api",
    }

    def get_domain(self):
        v = os.getenv("API_TESTS_ENV")
        assert v in self.DOMAINS.keys(), "API_TESTS_ENV value should be equal one of " + str(self.DOMAINS.keys())
        return self.DOMAINS[v]


environment = Environment()