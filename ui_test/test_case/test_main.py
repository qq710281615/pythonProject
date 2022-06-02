import os
from datetime import datetime

import pytest

from ui_test.pages.app_main import App


class TestMain:

    def teardown_class(self):
        self.today = datetime.today().date()
        self.report_path = r"C:\Users\ssbai\PycharmProjects\pythonProject\ui_test\report\{0}".format(self.today)
        if os.path.exists(self.report_path) is False:
            os.makedirs(self.report_path)
        cmd_str = "allure generate ../allure_temp -o {0} --clean".format(self.report_path)
        os.system(cmd_str)
        print("报告生成完成")

    # @pytest.mark.skip()
    def test_login(self, c):
        app = App()
        app.start().main().mime().login().login()

    def test_tyq(self):
        app = App()
        app.start().main().mime().tqy_main()
