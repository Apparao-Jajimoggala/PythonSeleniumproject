
from selenium.webdriver.common.by import By

class LoginPage():
    def __init__(self, driver):
        self.driver = driver

# Locators
        self.email_field = 'email'
        self.password_field = 'password'
        self.submit_button = 'input[type="submit"]'

    def enterEmail(self, userName):
        self.driver.find_element('id', self.email_field).send_keys(userName)

    def enterPassword(self, password):
        self.driver.find_element('id', self.password_field).send_keys(password)

    def loginButton(self):
        self.driver.find_element('css selector', self.submit_button).click()

    '''def login(self, userName, password):
        self.enterEmail(userName)
        self.enterPassword(password)
        self.loginButton()'''

''' 
# Define methods to expose these locators into elements
    def getEmailField(self):
        return self.driver.find_element(by=By.ID, value=self.email_field)

    def getPasswordField(self):
        return self.driver.find_element(by=By.ID, value=self.password_field)

    def getSubmitButton(self):
        return self.driver.find_element(by=By.CSS_SELECTOR, value=self.submit_button)

    def enterEmail(self, email1):
        self.getEmailField().send_keys(email1)

    def enterPassword(self, password):
        self.getPasswordField().send_keys(password)

    def loginButton(self):
        self.getSubmitButton().click()


    def login(self, email, password):
        self.enterEmail(email)
        self.enterPassword(password)
        self.loginButton()'''