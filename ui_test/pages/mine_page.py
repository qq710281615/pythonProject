import time
from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.wait import WebDriverWait
from ui_test.pages.base_page import BasePage
from ui_test.pages.login_page import LoginPage


class Mine(BasePage):

    def login(self):
        time.sleep(1)
        ele = WebDriverWait(self._driver, 5).until(lambda x: x.find_element(MobileBy.ID, "tv_mine_nick_name"))
        ele.click()
        return LoginPage(self._driver)

    def tqy_main(self):
        time.sleep(3)
        self.steps(r"..\process_config\page.yml")
        self.logging.info("首页加载完成，即将跳转【提钱游】页面")
        # return Mine(self._driver)
