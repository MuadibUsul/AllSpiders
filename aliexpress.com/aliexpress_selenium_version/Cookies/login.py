from selenium import webdriver


class Login:
    """
    登录类模块
    """
    def __init__(self, browser):
        # self.browser = webdriver.Chrome()
        self.browser = browser
        self.browser.maximize_window()

    def login(self, username, password):
        """
        使用selenium登录aliexpress
        :param username:
        :param password:
        :return:
        """
        self.browser.get("https://login.aliexpress.com/")
        self.browser.switch_to.frame("alibaba-login-box")
        username_input = self.browser.find_element_by_xpath('//*[@id="fm-login-id"]')
        password_input = self.browser.find_element_by_xpath('//*[@id="fm-login-password"]')
        username_input.send_keys(username)
        password_input.send_keys(password)
        login_button = self.browser.find_element_by_xpath('//*[@id="login-form"]/div[5]/button')
        login_button.click()
        Cookies = self.browser.get_cookies()
        return Cookies


# if __name__ == '__main__':
#     browser = webdriver.Chrome()
#     username = "3044856199@qq.com"
#     password = "123456789"
#     cookie = Login(browser).login(username, password)
#     print(cookie)

