import pytest
@pytest.mark.usefixtures("setup")
class Testpro:
    def test_firstdemo(self):
        print("Hello Akash")

    def test_seconddemo(self):
        print("Hello Shubham")