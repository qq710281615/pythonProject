# import os
from datetime import datetime

import pytest

from test_tool.send_email import send_email


@pytest.fixture(scope="module", autouse=True)
def c():
    print("开始测试模块")
    yield
    print("模块测试结束")
    # 发送测试报告到有想
    content = r"http://127.0.0.1:5000/report/{0}/index.html".format(datetime.today().date())
    send_email(content)



