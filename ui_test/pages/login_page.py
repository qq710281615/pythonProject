import logging

from ui_test.pages.base_page import BasePage


class LoginPage(BasePage):
    def login(self):
        self.steps(r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\pages\page.yml")
        logging.info("登录成功")

        # self._driver.find_element(MobileBy.ID, "cb_privacy_agree").click()
        # self._driver.find_element(MobileBy.ID, "tv_mobile_login").click()
        # self._driver.find_element(MobileBy.ID, "tv_login_tab_second").click()
        # self._driver.find_element(MobileBy.ID, "et_login_static_account_input").send_keys("15518907583")
        # self._driver.find_element(MobileBy.ID, "et_login_static_password_input").send_keys("ssbai521..")
        # self._driver.find_element(MobileBy.ID, "btn_login_static_commit").click()
