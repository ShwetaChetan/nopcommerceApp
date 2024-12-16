from selenium.webdriver.common.by import By

class Login:

  def __init__(self,driver):
    self.driver = driver
    self.textbox_email=(By.ID,"Email")
    self.textbox_password=(By.ID,"Password")
    self.button_login=(By.XPATH,"//button[normalize-space()='Log in']")
    self.link_logout=(By.LINK_TEXT,"Logout")

  def setUserName(self,email):
      email_field=self.driver.find_element(*self.textbox_email)
      email_field.clear()
      email_field.send_keys(email)

  def setPassword(self,password):
      password_field=self.driver.find_element(*self.textbox_password)
      password_field.clear()
      password_field.send_keys(password)

  def clickLogin(self):
      self.driver.find_element(*self.button_login).click()

  def clickLogout(self):
      self.driver.find_element(*self.link_logout).click()





