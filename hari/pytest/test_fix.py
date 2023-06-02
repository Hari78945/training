import Nom
import pytest
# import Nom.py
@pytest.fixture()
def fun():
    print("started")
def test_sam(fun):
    if Nom.add(2,3)==5:
        print(Nom.add(2,3))
        assert True
    else:
        Nom.add(2,3)==5
        assert False 
