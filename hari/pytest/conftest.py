import pytest
@pytest.fixture(scope="class")
def call():
    a=5+3
    print(a)
    yield
    print("code excuted sucessfully")
    