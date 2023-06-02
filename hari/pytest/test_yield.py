import pytest
import Nom
@pytest.fixture()
def fix():
    print("hi")
    c=3
    d=5
    s= c+d
    print(s)
    yield
    print("ended")
    return s

    
def test_yield(fix):
    assert Nom.add(2,3)==5,"condition is not equal"
    print(Nom.add(2,3))
