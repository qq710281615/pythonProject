import logging
import time
from ui_test.test_ui_cases.pages.base_page import BasePage
from ui_test.test_ui_cases.pages.mine_page import Mine


class HomePage(BasePage):

    def mime(self):
        time.sleep(3)
        self.steps(r"/ui_test/test_ui_cases\pages\page.yml")
        logging.info("首页加载完成，即将跳转【我的】页面")
        return Mine(self._driver)
