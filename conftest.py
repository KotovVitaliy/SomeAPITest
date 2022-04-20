import pytest


@pytest.fixture
def example_fixture_1():
    print("Fixture 1 works")
    yield
    print("After 1 test")


@pytest.fixture
def example_fixture_2():
    print("Fixture 2 works")
    yield
    print("After 2 test")


# @pytest.fixture(autouse=True)
def auto_fixture():
    print("I am an auto-fixture")

