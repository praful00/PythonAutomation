import pytest
@pytest.mark.usefixtures("setup")
class Testpro:
    def test_firstdemo(self):
        print("Hello Akash")

    def test_seconddemo(self):
        print("Hello Shubham")

    def test_thirddemo(self):
        print("Hello kunal")

    def test_fourthdemo(self):
        print("Hello pranay")