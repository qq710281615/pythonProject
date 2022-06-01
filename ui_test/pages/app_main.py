import time
from appium import webdriver
from test_tool import read_yaml_file
from test_tool import my_log
from ui_test.pages.base_page import BasePage
from ui_test.pages.home_page import HomePage

logging = my_log.MyLog()


class App(BasePage):

    def start(self):
        try:
            caps = read_yaml_file.YamlDo("../test_case/tongcheng.yml").read_yaml()["info"]
        except Exception as e:
            logging.info(e)
            return
        else:
            logging.info("获取到的设备信息是:{0}".format(caps))

        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(10)
        logging.info("app 启动成功")
        time.sleep(8)
        return self

    def main(self):
        return HomePage(self._driver)


