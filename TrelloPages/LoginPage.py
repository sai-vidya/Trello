from selenium.webdriver.common.by import By

class LoginPage(object):

    loginLink = (By.LINK_TEXT, "Log In")
    username = (By.ID, "user")
    atlassian = (By.XPATH, "//input[@type='submit']")
    password = (By.ID, "password")
    performLogin = (By.ID, "login-submit")

