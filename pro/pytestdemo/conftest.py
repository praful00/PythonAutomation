import pytest


@pytest.fixture(scope="class")
def setup():
    print("I am execute first")
    yield
    print("I am execute last")


@pytest.fixture()
def dataload():

    return ["praful", "shinde", "gangadhar"]