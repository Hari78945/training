import pytest
@pytest.mark.smoke
def test_add():
    a=19
    b=1
    a=a+b
    print(b)
    assert a==20,"contion fail"
    
def test_sep():
    a=40
    b=20
    a=a-b
    assert a==20
#regression are same