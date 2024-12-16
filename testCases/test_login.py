import pytest

from pageObjects.LoginPage import Login
from utilities.readProperties import ReadConfig
from utilities.customLogger import LogGen

class Test_001_Login:
    baseURL = ReadConfig.ApplicationUrl()
    username = ReadConfig.UserName()
    password = ReadConfig.GetPassword()
    logger = LogGen.loggen()

    @pytest.mark.sanity
    @pytest.mark.regression
    def test_homePageTitle(self,setup):
        self.logger.info("************ Test_001_Login*************")
        self.logger.info("************ verifying homepage title *************")
        self.driver = setup
        self.driver.get(self.baseURL)
        act_title=self.driver.title
        if act_title=="Your store. Login":
            assert True
            self.driver.close()
            self.logger.info("******** Home page title is passed*********")
        else:
            self.driver.save_screenshot(".\\Screenshoots\\"+"test_homepageTitle.png")
            self.driver.close()
            self.logger.error("********* Home page title is failed***********")
            assert False

    def test_Login(self,setup):
        self.logger.info("********* verifying login test***********")
        self.driver = setup
        self.driver.get(self.baseURL)
        self.lp=Login(self.driver)
        self.lp.setUserName(self.username)
        self.lp.setPassword(self.password)
        self.lp.clickLogin()
        # act_title=self.driver.title
        # if act_title=="Dashboard / nopCommerce administration":
        #     assert True
        #     self.logger.info("******** log in test is passed*********")
        #     self.driver.close()
        # else:
        #     self.driver.save_screenshot(".\\Screenshoots\\" + "test_homepageTitle.png")
        #     self.driver.close()
        #     self.logger.error("******** log in title is failed*********")
        #     assert False




