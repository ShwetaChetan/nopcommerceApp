import configparser

config=configparser.RawConfigParser()
config.read(".\\Configuration\\config.ini")


class ReadConfig:
    @staticmethod
    def ApplicationUrl():
        url = config.get("common info","baseURL")
        return url

    @staticmethod
    def UserName():
        userEmail = config.get("common info","username")
        return userEmail

    @staticmethod
    def GetPassword():
        userPassword = config.get("common info","password")
        return userPassword

