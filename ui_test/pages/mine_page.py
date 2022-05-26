import time

from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait

from ui_test.test_ui_cases.pages.base_page import BasePage
from ui_test.test_ui_cases.pages.login_page import LoginPage


class Mine(BasePage):

    def login(self):
        time.sleep(1)
        ele = WebDriverWait(self._driver, 5).until(lambda x: x.find_element(MobileBy.ID, "tv_mine_nick_name"))
        ele.click()
        return LoginPage(self._driver)
