import inspect
import os
import time
import uuid
from datetime import datetime
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver
from test_tool.my_log import MyLog
from test_tool import read_yaml_file


class BasePage:

    black_list_data = read_yaml_file.YamlDo(r"..\process_config\back_lists.yml").read_yaml()
    _driver: WebDriver = None
    _black_list = black_list_data

    def __init__(self, driver: WebDriver = None):
        self._driver = driver
        self.logging = MyLog()

    def save_picture(self):
        today = datetime.today().date()
        filepath = r"..\picture\{0}".format(today)
        if os.path.exists(filepath) is False:
            os.makedirs(filepath)
        filename = os.path.join(filepath, str(uuid.uuid4()) + str(today) + ".png")
        self._driver.get_screenshot_as_file(filename)
        return filename

    def find(self, location_method, locator):
        ele = None
        try:
            ele = self._driver.find_element(location_method, locator)
        except Exception as e:
            for black in self._black_list:
                ele_list = self._driver.find_elements(black["By"], black["locator"])
                ele_list[0].click()
                break
        else:
            ele = self._driver.find_element(location_method, locator)
        finally:
            return ele

    def steps(self, filename):
        data = read_yaml_file.YamlDo(filename).read_yaml()
        self.logging.info("{}内容加载完成".format(filename))
        self.logging.info("文件内容是{0}".format(data))
        module = str(inspect.stack()[1].function)
        self.logging.info("即将进入的页面是{0}".format(module))
        print(type(module))
        for i in data[module]:
            self.save_picture()
            self.logging.info("定位的条件是:{}".format(i))
            if "By" in i.keys():
                self.logging.info(self._driver)
                self.logging.info("开始定位")
                if i["By"] == "coordinates":
                    self.logging.info(i)
                    w, h = eval(i["x"]), eval(i["y"])
                    wide = float(self._driver.get_window_size()["width"])
                    height = float(self._driver.get_window_size()["height"])
                    self.logging.info("宽度是：{0},高度是：{1}".format(wide, height))
                    x = int(wide * w)
                    y = int(height * h)
                    self._driver.swipe(x, y, x, y, 2)
                    self.logging.info("元素找到了，条件是:{}".format(i))
                    time.sleep(1)
                # 通过xpth定位元素
                elif i["By"] == "xpath":
                    # ele = self._driver.find_element(MobileBy.XPATH, i["locator"])
                    ele = self.find(MobileBy.XPATH, i["locator"])
                    self.logging.info("元素找到了，条件是:{}".format(i))
                    if i["move"] == "click":
                        ele.click()
                    elif i["move"] == "send_keys":
                        # 先清空，在输入
                        ele.clear()
                        ele.send_keys(i["content"])
                # 通过id定位元素
                elif i["By"] == "id":
                    # ele = self._driver.find_element(i["By"], str(i["locator"]))
                    ele = self.find(MobileBy.ID, i["locator"])
                    self.logging.info("元素找到了，条件是:{}".format(i))
                    if i["move"] == "click":
                        ele.click()
                    elif i["move"] == "send_keys":
                        # 先清空，在输入
                        ele.clear()
                        ele.send_keys(i["content"])
            self.save_picture()

