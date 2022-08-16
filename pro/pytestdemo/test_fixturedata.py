import pytest

from pytestdemo.baseclass import logtest


@pytest.mark.usefixtures("dataload")
class Testdata(logtest):

    def test_fixturedata(self, dataload):
        log = self.getlogger()
        log.info(dataload[0])
        log.info(dataload[1])


