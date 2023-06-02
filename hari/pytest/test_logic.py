# import pytest
# class att():
#     def add(self,x,y):
#         return(x+y)
# att1=att()
# @pytest.mark.parametrize("x,y,result",
#     [
#         (1,2,3),
#         (2,1,3),
#     ]
# )
# def test_add(x,y,result):
#     assert att1.add(x,y)==result
class person():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def att(self,place):
        print("my name is {}\niam {} years world \ncome from {}" .format(self.name,self.age,place))
    
person1=person("hari",19)
person2=person("vicky",19)
person1.att("avadi")
person2.att("avadi")
    