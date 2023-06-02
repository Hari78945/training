import pytest
@pytest.mark.usefixtures("call")
class Test_Samp:
    def test_sam1(self):
        print("hellow")
    def test_sam2(self):
        print("hi")
        
    