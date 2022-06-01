# -*- coding: utf-8 -*-
import time
import pytest
from appium import webdriver
from selenium.webdriver.common.by import By
from test_tool import read_yaml_file
from test_tool.my_log import MyLog
logging = MyLog()


@pytest.fixture(scope="function")
def setup_function():
    try:
        caps = read_yaml_file.YamlDo("../ui_test/test_case/app_info.yml").read_yaml()["info"]
    except Exception as e:
        logging.info(e)
        return
    else:
        logging.info("获取到的设备信息是:{0}".format(caps))
        return caps


def test_open(setup_function):
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', setup_function)
    # driver.implicitly_wait(15)
    #
    driver.find_element(By.ID, 'tv.danmaku.bili:id/expand_search').click()
    time.sleep(1)
    driver.find_element(By.ID, 'tv.danmaku.bili:id/search_src_text').send_keys("霞姐")
    time.sleep(2)
    driver.find_element(By.XPATH, "//*[@resource-id='tv.danmaku.bili:id/title' and @text='陕北霞姐美食']").click()
    time.sleep(5)
    # driver.quit()
    # logging.info("end")


if __name__ == '__main__':
    pytest.main()

