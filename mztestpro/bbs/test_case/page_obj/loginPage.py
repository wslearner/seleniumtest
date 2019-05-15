from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from .base import Page
from time import sleep


class login(Page):
    """用户登录页面"""
    url = '/'

    bbs_login_user_loc = (By.XPATH,'//div[@id="mzCust"]/div/img')
    bbs_login_button_loc = (By.ID, 'mzLogin')

    def bbs_login(self):
        self.find_element(*self.bbs_login_user_loc).click()
        sleep(1)
        self.find_element(*self.bbs_login_button_loc).click()

        login_username_loc = (By.ID, 'account')
        login_password_loc = (By.ID, 'password')
        login_button_loc = (By.ID, 'login')