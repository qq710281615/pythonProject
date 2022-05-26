import os
from datetime import datetime
import pytest
from ui_test.test_ui_cases.pages.app_main import App


class TestMain:

    def setup_class(self):
        print("setup_class开始测试")

    @pytest.mark.skip()
    def test_login(self):
        app = App()
        app.start().main().mime().login().login()

    def test_add(self):
        assert 1 == 1

    def test_add_1(self):
        assert 1 == 2

    def teardown_class(self):
        self.today = datetime.today().date()
        self.report_path = r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\report\{0}".format(self.today)
        if os.path.exists(self.report_path) is False:
            os.makedirs(self.report_path)
        cmd_str = "allure generate ../../allure_temp -o {0} --clean".format(self.report_path)
        os.system(cmd_str)
        print("报告生成完成")
