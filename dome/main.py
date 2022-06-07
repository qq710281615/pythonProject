from locust import task, TaskSet, HttpUser
from test_tool.read_xlex_file import ReadData
import os
from test_tool import test_dome
from random import randint

class TestCases(TaskSet):

    def on_stop(self):
        print("测试结束.")

    def on_start(self):
        self.d = ReadData().read_data(r"/data/test_data.xlsx", "Sheet1")
        return self.d

    @task(1)
    def test(self):
        r = randint(len(self.d))
        rest = test_dome().add(self.d[r][0], self.d[r][1])
        self.client.get(url="https://www.uc123.com/", catch_response=True)
        if rest == self.d[r][2]:
            print("测试通过")
        else:
            print("测试失败")


class MyLocust(HttpUser):
    test_set = TestCases
    min_wait = 1
    max_wait = 2


if __name__ == '__main__':
    print(__file__)
    print(" locust -f  {0} --host=https://www.baidu.com/".format(__file__))
    os.system(" locust -f  {0} --host=https://www.uc123.com/".format(__file__))