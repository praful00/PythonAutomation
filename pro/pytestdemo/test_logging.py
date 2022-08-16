import logging

def test_loggingDemo():

    logger = logging.getLogger(__name__)

    filehandler = logging.FileHandler('logfile.log')
    formatter = logging.Formatter("%(asctime)s :%(levelname)s :%(name)s :%(message)s")
    filehandler.setFormatter(formatter)
    logger.addHandler(filehandler)

    logger.setLevel(logging.DEBUG)
    logger.debug("test")
    logger.info("test")
    logger.warning("test")
    logger.error("test")
    logger.critical("test")


