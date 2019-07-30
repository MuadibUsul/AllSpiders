import pickle
from selenium import webdriver

from Cookies.login import Login


class Cookies:
    def __init__(self):
        self.browser = webdriver.Chrome()

    def get_cookies(self, username, password):
        """
        :param username:
        :param password:
        :return: NULL
        """
        LOGIN = Login(self.browser)
        cookies = LOGIN.login(username, password)
        for cookie in list(cookies):
            print(cookie)

    def set_cookies(self):
        """
        :return: NULL
        """
        self.browser.get("https://aliexpress.com")
        cookies = pickle.load(open("cookies.pickle", "rb"))
        for cookie in cookies:
            self.browser.add_cookie(cookie)
        self.browser.get("https://bestselling.aliexpress.com/en")


if __name__ == '__main__':
        username = "3044856199@qq.com"
        password = "123456789"
        Cookies().get_cookies(username, password)
    # Cookies().set_cookies()
