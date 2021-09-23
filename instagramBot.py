from selenium import webdriver
from pages import LoginPage
from time import sleep
class InstagramBot:
    def __init__(self, login, password):
        opts = webdriver.FirefoxOptions()
        opts.headless = True
        self.browser = webdriver.Firefox(options = opts)
        self.browser.implicitly_wait(5)
        login_page = LoginPage(self.browser)
        login_page.login(login, password)
        
    def putLike(self, link):
        self.browser.get(link)
        self.browser.implicitly_wait(2)
        like = self.browser.find_element_by_css_selector('.fr66n')
        sleep(2)
        like.click()

    def close(self):
        self.browser.close()
