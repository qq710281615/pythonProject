import unittest
from test_tool.read_xlex_file import ReadData
from test_tool.test_dome import TestDome
from ddt import ddt

d = ReadData().read_data(r"/data/test_data.xlsx", "Sheet1")
print(d)


@ddt
class TestAdd(unittest.TestCase):
    #
    # def setUp(self):
    #     d = ReadData().read_data(r"C:\Users\ssbai\PycharmProjects\pythonProject\data\test_data.xlsx", "Sheet1")
    #     return self.d
    # # @data(*d)
    # def test_add(self, m):
    #     print(m)
    #     r = TestDome(m["a"], m["b"]).add()
    #     self.assertEqual(m["c"], r)
    def setUpClass(cls) -> None:
        pass

    def setUp(self):
        pass

    def test_add(self):
        r = TestDome(1, 1).add()
        self.assertEqual(2, r)

    def tearDown(self) -> None:
        pass

    def tearDownClass(cls) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
