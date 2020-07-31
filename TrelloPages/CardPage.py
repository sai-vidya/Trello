from selenium.webdriver.common.by import By

class CardPage(object):
    card1 = (By.XPATH, "//div[contains(@class,'list-cards')]//a[contains(@href,'card-1')]")
    addMember = (By.XPATH, "//span[contains(text(),'Members')]")
    currentUser = (By.XPATH, "(//div[contains(@class,'board-members')]//ul[contains(@class,'member-list')]//a)[1]")
    descriptionArea = (By.XPATH, "//div[contains(@class,'description-title')]")
    commentBox = (By.XPATH, "//div[@class='comment-box']")
    commentText = (By.XPATH, "//textarea[contains(@placeholder,'Write a comment')]")
    saveComment = (By.XPATH, "//input[@value='Save']")
