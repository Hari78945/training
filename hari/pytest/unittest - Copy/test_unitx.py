import unittest
class sam(unittest.TestCase):
    def test_fun(self):
        a=2
        b=5
        a=a+b
        assert a!=7,"its is not equal"
        print(a)
    def test_fun1(self):
        a=[1,2,3,4,5]
        b=[1,2,3,4,5,6]
        self.assertNotEqual(a, b), "Failed Successfully"
    def test_add(self):
        a=3+6
        assert a!=10, "condition fails"
        print(a)
        

#if any case fail to stop there 
# pytest -v -x --capture=no  test_unit.py 
# for ingonoring a error message   
#  pytest -v -x  --tb=no  test_unitx.py
# choose a maximum failcases
# pytest -v -x --maxfail=2  test_unitx.py      
        
