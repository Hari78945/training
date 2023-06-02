import unittest


def setUpModule(self):
    a = 2
    b = 3
    print(a + b)
    # self.assertNotEqual(a,b)


def tearDownModule(self):
    print("code sucessfully excuted outside class")


class TestSet(unittest.TestCase):
    def setUp(self):
        # a = 2
        # b = 3
        print("inside class")
        # self.assertNotEqual(a,b)

    def tearDown(self):
        print("code sucessfully excuted")

    def test_sam1(self):
        l = [1, 2, 3, 4, 5, 6]
        for i in l:
            if i % 2 == 0:
                print(i)

    def test_sa1(self):
        print("hi")
