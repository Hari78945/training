import pytest
import call
@pytest.mark.parametrize("x,y,result",
        [ 
         (10,20,30),
         (3,2,5),
         (4,5,9),
         ])
def test_add(x,y,result):
    assert call.add(x,y)==result
