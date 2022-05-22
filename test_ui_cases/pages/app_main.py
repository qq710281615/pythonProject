import time
import uuid
from datetime import datetime

from appium import webdriver
from appium.webdriver.extensions.android.gsm import GsmCallActions

from test_tool import read_yaml_file
from test_tool import my_log
from test_ui_cases.pages.base_page import BasePage


logging = my_log.MyLog()


class App(BasePage):

    def start(self):
        try:
            caps = read_yaml_file.YamlDo("../test_case/app_info.yml").read_yaml()["info"]
        except Exception as e:
            logging.info(e)
            return
        else:
            logging.info("获取到的设备信息是:{0}".format(caps))

        self._driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self._driver.implicitly_wait(10)
        print("app 启动成功")
        print(self._driver)
        time.sleep(10)
        return self

    def homepage(self):
        # 设置网络
        self._driver.set_network_connection(4)
        time.sleep(3)
        self.save_picture()
        self._driver.start_recording_screen()
        self.steps("../test_case/test_tep.yml")
        time.sleep(3)
        self._driver.set_network_connection(1)
        time.sleep(3)
        self.save_picture()
        self._driver.set_network_connection(0)
        time.sleep(3)
        self.save_picture()
        self._driver.set_network_connection(4)
        time.sleep(3)
        self.save_picture()
        self._driver.set_network_connection(6)
        time.sleep(3)
        self.save_picture()

    def save_picture(self):
        today = datetime.today().date()
        filename = str(uuid.uuid4()) + str(today) + ".png"

        self._driver.get_screenshot_as_file(filename)



