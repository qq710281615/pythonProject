import time


class TestDome:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def add(self):
        time.sleep(0.5)
        return self.a + self.b

