import configparser
import os

config = configparser.RawConfigParser()


initfile = 'D:\Learnings\Selenium\python\SystemTest\Configuration\config.ini'
config.read(initfile)


class ReadConfig:
    @staticmethod
    def getURL():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def getUsername():
        username = config.get('common info', 'username')
        return username

    @staticmethod
    def getPassword():
        password = config.get('common info', 'password')
        return password
