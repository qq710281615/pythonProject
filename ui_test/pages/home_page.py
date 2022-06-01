import logging
import time
from ui_test.pages.base_page import BasePage
from ui_test.pages.mine_page import Mine


class HomePage(BasePage):

    def mime(self):
        time.sleep(5)
        self.steps(r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\process_config\page.yml")
        logging.info("首页加载完成，即将跳转【我的】页面")
        return Mine(self._driver)
