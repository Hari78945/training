import unittest
@unittest.skip
class ski(unittest.TestCase):
    def test_add(self):
        a=10
        b=12
        assert a+b==22
        print(a+b)
        
class ski(unittest.TestCase):
    def test_add(self):
        a=10
        b=12
        assert a+b==23    
        print(a+b)
