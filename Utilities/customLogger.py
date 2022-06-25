import logging
import os


class LogGen:
    @staticmethod
    def loggen():
        thisfolder = os.path.dirname(os.path.abspath(__file__))
        filepath = os.path.join(thisfolder, 'LogFile')
        logging.basicConfig(filename=filepath)
        logger=logging.getLogger()
        logger.setLevel(logging.INFO)
        return logger
