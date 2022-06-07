import os
import time

import pytest


@pytest.fixture(scope="function", params=[1, 2, 3, 4])
def ssbai(request):
    # print("这是ssbai的测试")
    # # yield
    # print("测试完成")
    return request.param


class TestLogin:

    # def setup_class(self):
    #     print("开始测试")
    #
    # def teardown_class(self):
    #     print("结束测试")
    #
    # def setup(self):
    #     print("开始方法")
    #
    # def teardown(self):
    #     print("结束方法")


    @pytest.mark.a
    def test_1(self):
        print("1"*10)
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.skip
    def test_2(self):
        print("2"*10)
        time.sleep(1)
        assert 1 == 1

    @pytest.mark.run(order=1)
    def test_3(self, ssbai):
        print("3"*10)
        print(ssbai)
        time.sleep(1)
        assert 1 == 1


if __name__ == '__main__':
    pytest.main()

    os.system('allure generate ./ssbai_temp -o ./static --clean')
    print("end")
