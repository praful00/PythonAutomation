import inspect
import logging


class logtest:
        def getlogger(self):

            loggerName = inspect.stack()[1][3]
            logger = logging.getLogger(loggerName)

            filehandler = logging.FileHandler('loger.log')
            formatter = logging.Formatter("%(asctime)s :%(levelname)s : %(name)s :%(message)s")
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)

            logger.setLevel(logging.DEBUG)
            return  logger