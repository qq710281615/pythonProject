import os

import pytest


@pytest.fixture(scope="module")
def generate_report():
    print("开始测试")

