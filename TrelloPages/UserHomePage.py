from selenium.webdriver.common.by import By

class UserHomePage(object):

    boardsTab = (By.XPATH, "//a[contains(@href,'boards')]")
    newBoard = (By.XPATH, "//span[contains(text(),'Create new board')]")
    boardTitle = (By.XPATH, "//input[@placeholder='Add board title']")
    createBoard = (By.XPATH, "//span[text()='Create Board']")
    createdBoard = (By.XPATH, "//h3[contains(text(),'Personal Boards')]/ancestor::div[contains(@class,"
                              "'boards-page-board-section-header')]/following-sibling::div//div[@title='Project']")

