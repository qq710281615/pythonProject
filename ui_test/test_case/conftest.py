# import os

import pytest


@pytest.fixture(scope="module", autouse=True)
def c():
    print("开始测试模块")
    yield
    print("模块测试结束")
    # report_path = r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\report\{0}".format(20220547)
    # if os.path.exists(report_path) is False:
    #     os.makedirs(report_path)
    #     cmd_str = "allure generate ../allure_temp -o {0} --clean".format(report_path)
    #     os.system(cmd_str)
    #     print("报告生成完成")


