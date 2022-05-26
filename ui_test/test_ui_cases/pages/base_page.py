import inspect
import os
import time
import uuid
from datetime import datetime

import allure

from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from test_tool.my_log import MyLog


from test_tool import read_yaml_file
logging = MyLog()


class BasePage:

    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    def save_picture(self):
        today = datetime.today().date()

        filepath = r"C:\Users\ssbai\PycharmProjects\pythonProject\picture\{0}".format(today)
        if os.path.exists(filepath) is False:
            os.makedirs(filepath)
        filename = os.path.join(filepath, str(uuid.uuid4()) + str(today) + ".png")
        self._driver.get_screenshot_as_file(filename)
        return filename

    def steps(self, filename):
        data = read_yaml_file.YamlDo(filename).read_yaml()
        logging.info("{}内容加载完成".format(filename))
        logging.info("文件内容是{0}".format(data))
        module = inspect.stack()[1].function
        logging.info("即将进入的页面是{0}".format(module))
        for i in data[module]:
            logging.info(i)
            if "By" in i.keys():
                logging.info(self._driver)
                logging.info("开始定位")
                # filename_p = self.save_picture()

                # with open(filename_p, "rb") as f:
                #     o = f.read()
                # allure.attach(o, attachment_type=allure.attachment_type.PNG)
                # 通过xpth定位元素
                if i["By"] == "xpath":
                    ele = self._driver.find_element(MobileBy.XPATH, i["locator"])
                    if i["move"] == "click":
                        ele.click()
                    elif i["move"] == "send_keys":
                        ele.send_keys(i["content"])
                # 通过id定位元素
                elif i["By"] == "id":
                    ele = self._driver.find_element(i["By"], str(i["locator"]))
                    if i["move"] == "click":
                        ele.click()
                    elif i["move"] == "send_keys":

                        ele.send_keys(i["content"])
                # 通过坐标定位元素
                elif i["By"] == "coordinates":
                    logging.info(i)
                    w, h = eval(i["x"]), eval(i["y"])
                    wide = float(self._driver.get_window_size()["width"])
                    height = float(self._driver.get_window_size()["height"])
                    logging.info("宽度是：{0},高度是：{1}".format(wide, height))
                    x = int(wide * w)
                    y = int(height * h)
                    self._driver.swipe(x, y, x, y, 2)
                    time.sleep(1)


