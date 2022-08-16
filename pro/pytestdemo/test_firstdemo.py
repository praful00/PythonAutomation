#pytest file should start with the name test_ or end with _test
#pytest method name should start with test
#Any code should be wrapped in method only
import pytest


@pytest.mark.usefixtures("setup")
class Testdemo:

     def test_firstprogram(self):
          print("Hello Praful shinde")

