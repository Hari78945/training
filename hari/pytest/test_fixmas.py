import pytest
@pytest.mark.usefixtures("add")
class Test_att:
    def test_add(self):
        print("hi")
    def test_add1(self):
        print("hellow")
    def test_add2(self):
        print("who")
