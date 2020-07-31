from selenium.webdriver.common.by import By

class BoardPage(object):

    newList = (By.XPATH, "//span[text()='Add a list']")
    addlList = (By.XPATH, "//span[text()='Add another list']")
    listNameBox = (By.CLASS_NAME, "list-name-input")
    addListBtn = (By.XPATH, "//input[@value='Add List']")

    newCardNotStarted = (By.XPATH, "//h2[contains(text(),'Not Started')]/ancestor::div[contains(@class,'list-header')]"
                         "/following-sibling::div//span[contains(@class,'add-a-card')]")
    addlCardNotStarted = (By.XPATH, "//h2[contains(text(),'Not Started')]/ancestor::div[contains(@class,'list-header')]"
                          "/following-sibling::div//span[contains(@class,'add-another-card')]")
    nextCardNotStarted = (By.XPATH, "//h2[contains(text(),'Not Started')]/ancestor::div[contains(@class,'list-header')]"
                         "/following-sibling::div//textarea[contains(@placeholder,'Enter a title for this card')]")
    cardListNotStarted = (By.XPATH, "//h2[contains(text(),'Not Started')]/ancestor::div[contains(@class,'list-header')]"
                                    "/following-sibling::div/a[contains(@href,'card-')]")
    cardListInProgress = (By.XPATH, "//h2[contains(text(),'In Progress')]/ancestor::div[contains(@class,'list-header')]"
                                    "/following-sibling::div/a[contains(@href,'card-')]")
    addCardBtn = (By.XPATH, "//input[@value='Add Card']")
    qaCardArea = (By.XPATH, "//h2[contains(text(),'QA')]/ancestor::div[contains(@class,'list-content')]")
    inProgressCardArea = (By.XPATH, "//h2[contains(text(),'In Progress')]/ancestor::div[contains(@class,'list-content')]")
