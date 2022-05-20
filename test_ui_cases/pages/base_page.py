
from appium.webdriver.common.mobileby import MobileBy
from appium.webdriver.webdriver import WebDriver


from test_tool import read_yaml_file


class BasePage:

    _driver: WebDriver = None

    def __init__(self, driver: WebDriver = None):
        self._driver = driver

    # def find(self, locator, option):
    #     # locator = "BY." + str(locator)
    #     return self._driver.find_element(locator, option)

    def steps(self, filename):
        data = read_yaml_file.YamlDo(filename).read_yaml()
        print(data)
        for i in data:
            ele = None
            print(i)
            if "BY" in i.keys():
                print(self._driver)
                print(i["BY"], i["locator"])
                print("self._driver.find_element({0},{1})".format(i["BY"], i["locator"]))
                # locator = "'{0}'".format(i["locator"])
                if i["BY"] == "xpath":
                    ele = self._driver.find_element(MobileBy.XPATH, i["locator"])
                else:
                    ele = self._driver.find_element(i["BY"], str(i["locator"]))

            if i["move"] == "click":
                ele.click()
            if i["move"] == "send_keys":
                ele.send_keys(i["contxt"])

