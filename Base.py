import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
from TrelloPages.LoginPage import LoginPage
from TrelloPages.UserHomePage import UserHomePage
from TrelloPages.BoardPage import BoardPage
from TrelloPages.CardPage import CardPage

class sampleTest(unittest.TestCase):

    @classmethod
    def setUpClass(self):
        self.driver = webdriver.Chrome('C:/Users/savya/PycharmProjects/Trello/chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get("http://www.trello.com")

    def test_loginTrello(self):
        login = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((LoginPage.loginLink)))
        login.click()
        print("Clicked login button")

        username = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable((LoginPage.username)))
        username.click()
        username.send_keys("saividya.sv@gmail.com")
        print("Entered username")

        try:
            atlassian = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((LoginPage.atlassian)))
            atlassian.click()
            print("Confirming login with Atlassian")
        except:
            print("Atlassian element not found")

        try:
            WebDriverWait(self.driver, 20).until(ec.url_contains("id.atlassian.com"))
            if "id.atlassian.com" in self.driver.current_url:
                password = WebDriverWait(self.driver, 20).until(ec.element_to_be_clickable((LoginPage.password)))
                password.click()
                password.send_keys("D@k!Put58619")
                print("Entered password")
                completeLogin = WebDriverWait(self.driver, 5).until(ec.element_to_be_clickable((LoginPage.performLogin)))
                completeLogin.click()
                print("Clicked final login button")
        except:
            print("Issue with entering password and finishing login")

        boards = WebDriverWait(self.driver, 50).until(ec.element_to_be_clickable((UserHomePage.boardsTab)))
        boards.click()

    def test_newBoard(self):
        newBoard = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((UserHomePage.newBoard)))
        newBoard.click()
        print("Clicked create new board")
        boardTitle = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((UserHomePage.boardTitle)))
        boardTitle.click()
        boardTitle.send_keys("Project")
        createBoard = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((UserHomePage.createBoard)))
        createBoard.click()
        createdBoard = WebDriverWait(self.driver, 30).until(ec.presence_of_element_located((UserHomePage.createdBoard)))
        if createdBoard.is_displayed():
            print("Successfully created the board 'Project'")
            try:
                createdBoard.click()
            except:
                pass

    def test_newLists(self):
        listNames = ['Not Started', 'In Progress', 'QA', 'Done']
        for i in listNames:
            try:
                newList = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.newList)))
                addlList = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.addlList)))
                if newList.is_displayed():
                    newList.click()
                elif addlList.is_displayed():
                    addlList.click()
                self.createList(i)
            except:
                print("Creating list '" + i + "' in the board")
                self.createList(i)

    def createList(self, listName):
        listNameBox = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((BoardPage.listNameBox)))
        listNameBox.click()
        listNameBox.send_keys(listName)
        addListBtn = WebDriverWait(self.driver, 30).until(ec.element_to_be_clickable((BoardPage.addListBtn)))
        addListBtn.click()
        print("List '" + listName + "' has been created successfully")

    def test_taskCards(self):
        listName = 'Not Started'
        cardNames = ['Card 1', 'Card 2', 'Card 3', 'Card 4']
        for i in cardNames:
            try:
                newCardNotStarted = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.newCardNotStarted)))
                if newCardNotStarted.is_displayed():
                    newCardNotStarted.click()
                self.createCard(i, listName)
            except:
                print("Proceeding to create new card " + i)
                self.createCard(i, listName)

    def createCard(self, cardName, listName):
        card = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.nextCardNotStarted)))
        card.click()
        card.send_keys(cardName)
        addCard = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.addCardBtn)))
        addCard.click()
        print("Card '" + cardName + "' has been successfully added under list '" + listName + "'")

    def test_verifyCardOps(self):
        cardsNotStarted = WebDriverWait(self.driver, 2).until(
            ec.presence_of_all_elements_located((BoardPage.cardListNotStarted)))
        qaCardArea = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((BoardPage.qaCardArea)))
        inProgressArea = WebDriverWait(self.driver, 2).until(
            ec.element_to_be_clickable((BoardPage.inProgressCardArea)))
        # for card in cards:
        #     print(str(card))
        ActionChains(self.driver).drag_and_drop(cardsNotStarted[1], inProgressArea).perform()
        ActionChains(self.driver).drag_and_drop(cardsNotStarted[2], qaCardArea).perform()
        cardsInProgress = WebDriverWait(self.driver, 2).until(
            ec.presence_of_all_elements_located((BoardPage.cardListInProgress)))
        ActionChains(self.driver).drag_and_drop(cardsInProgress[0], qaCardArea).perform()
        print("Done moving cards as required")

    def test_verifyEditCard(self):
        cardToEdit = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.card1)))
        cardToEdit.click()
        addMember = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.addMember)))
        addMember.click()
        currentUser = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.currentUser)))
        currentUser.click()
        commentBox = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.commentBox)))
        commentBox.click()
        comment = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.commentText)))
        comment.click()
        comment.send_keys("I am done")
        saveComment = WebDriverWait(self.driver, 2).until(ec.element_to_be_clickable((CardPage.saveComment)))
        saveComment.click()
        print("Card details edited as required")

    @classmethod
    def tearDownClass(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()
