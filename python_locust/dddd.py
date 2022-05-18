from locust import task, TaskSet, HttpUser


class TestCases(TaskSet):

    @task(1)
    def test(self):
        self.client.get(url="https://www.uc123.com/", catch_response=True)


class MyLocust(HttpUser):
    test_set = TestCases
    min_wait = 1
    max_wait = 2

