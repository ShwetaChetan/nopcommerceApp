# from selenium.webdriver.common.by import By
#
#
# class AddCustomer:
#
#     def __init__(self,driver):
#         self.driver = driver
#         self.lnkCustomers_menu_xpath = By.XPATH, "/html/body/div[3]/aside/div/div[4]/div/div/nav/ul/li[4]/a/p/text()"
#         self.lnkCustomers_menuitem_xpath = By.XPATH, "//a[@href='/Admin/Customer/List']//p[contains(text(),'Customers')]"
#         self.btnAddNew_xpath = By.XPATH, "//a[normalize-space()='Add new']"
#
#
#     def ClickCustomer(self):
#         self.driver.find_element(*self.lnkCustomers_menu_xpath).click()
#
#     def clickSubCusromer(self):
#         self.driver.find_element(*self.lnkCustomers_menuitem_xpath).click()
#
#     def ClickAddnew(self):
#         self.driver.find_element(*self.btnAddNew_xpath).click()
#
