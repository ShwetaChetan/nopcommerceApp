# import time
#
# from testCases.conftest import setup
# from utilities.readProperties import ReadConfig
# from utilities.customLogger import LogGen
# from pageObjects.LoginPage import Login
# from pageObjects.AddcustomerPage import AddCustomer
# from selenium import webdriver
#
# import string
# import random
#
# class Test_003_AddCustomer:
#     baseURL = ReadConfig.ApplicationUrl()
#     username = ReadConfig.UserName()
#     password = ReadConfig.GetPassword()
#     logger = LogGen.loggen()
#
#     def test_addCustomer(self,setup):
#         self.logger.info("*************Test_003_AddCustomer***************")
#         self.driver = setup
#         self.driver.get(self.baseURL)
#         self.driver.maximize_window()
#
#         self.lp = Login(self.driver)
#         self.lp.setUserName(self.username)
#         self.lp.setPassword(self.password)
#         self.lp.clickLogin()
#         self.logger.info("#################Login successfull############")
#
#         self.logger.info("***************Start adding Customer********")
#
#         self.ac = AddCustomer(self.driver)
#         self.ac.ClickCustomer()
#         self.ac.clickSubCusromer()
#         self.ac.ClickAddnew()
#         time.sleep(2)
#
# #         self.logger.info("***********providing customer info****************")
# #         self.email = random_generator() + "@gmail.com"
# #         self.ac.setEmail(self.email)
# #         self.ac.setpassword("test123")
# #         self.ac.setcustomerRoll("guest")
# #         self.ac.setmanagerofwendor("ven/dor 2")
# #         self.ac.setdob("1/1/25")
# #
#
# @staticmethod
# def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
#     return ''.join(random.choice(chars)for x in range(size))