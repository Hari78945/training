A = "hari"
print(A)


i = 0
while True:
   print(i)
   i = i + 1
   if i >5:
      break

a=int(input("enter a passanger age :"))
i=4
while a<i:
    i=i+1
    if a>i:
        continue
    print("no cost")


a=2
i=4
while a<i:
    i=i+1
    print(i)
    # if a>i:
        # continue
        # print("no cost")


i=0
while True:
    i+=1
    if i == 2:
        continue
    if i == 5:
        break
    
#     print(i)
l1= ["apple", "banana", "cherry"]
l.append("hari")
l.insert(1,"grape")
l="gape,jan"
a= l.split(",")
print(a)

# a = "Hello, World!"
b = a.split(",")
print(b)
thistuple = ("apple", "banana", "cherry")
for i in range(len(thistuple)):
  print(thistuple[i])

def bubble_sort(lst):
    n = len(lst)
    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already in place
        for j in range(0, n-i-1):
            # Traverse the list from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if lst[j] > lst[j+1] :
                lst[j], lst[j+1] = lst[j+1], lst[j]

# Example usage:
my_list = [3, 7, 1, 9, 2]
bubble_sort(my_list)
print(my_list)
l=[12, 35, 9, 56, 24, 65, 33]
l1=l[0]
l[0]=l[-1]
l[-1]=l1
print(l)
l1=l[0:2]
l3=l[-2:]
l2=l1[::-1]
l4=l3[::-1]
l[0:2]=l4
l[-2:]=l2
print(l)
   temp = newList[0]
l=[24,56,9,35,12]
    newList[0] = newList[size - 1]
    newList[size - 1] = temp
     

a=int(input("enter a number: "))
f=1
for i in range (1,a+1):
    f=f*i
print(f)

c=0
l=[1,2,3,4,5]
for i in l:
    c+=1
print(c)

a=int(input("enter a  number:"))
f=1
for i in range(1,a+1):
    f=f*i
print(f)
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
if 2==c or 1==c:
    print("it is prime number")
else:
    print("it is not a prime number")
    
   
def cal():    
    op=input("enter a operator:")
    a=int(input("enter a number:"))
    b=int(input("enter a second number:"))
    if op=="+":
        a=a+b
        print(a)
    else:
        print("please check the operator")

cal()
print("hi")

l.sort()
a=l[-2:]
print(a)
for i in range(len(a)):
    
    if i<=a:
        print(a)

for i in l:
    if a>i:
        print(a)

lst=[3,4,2,1,7,8]
def sort_list(lst):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] > lst[j]:
                print(lst[i],lst[j])
                lst[i], lst[j] = lst[j], lst[i]
    return lst
               
sort_list(lst)


class l:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def hari(self):
        return "iam {} iam {}yesrs old".format(self.name,self.age)
        
l1=l("hari",18)
print(l1.hari)
print(l1.self("hari","18"))

for i in range(1,5):
    print(i)
    for j in range(1,5):
        print(j,end=": ")
        for k in range(1,5):
            print(k,end=" ")
        print()
        
class att:
    def __init__ (self, name, age=8):
        self.name = name
        self.age=age
    def person(self): 
        return "my name is {}\niam {} old" .format(self.name,self.age)
p1=att("hari")
p2=att("vicky",19)
print(p1.person())   
print(p2.person())

class att1:
    def person:
        self.name=name

a={0:"apple",1:"cake",2:"chok"}
b={4:"cricket",5:"slice"}
print(a[0])
for i in a:
    print(i,":",a[i])
for key,value in  a.items():
    print(key,":",value)
a[3]="hari"
a.update(b)
del a [1]
a.pop(5)
print(a)
a={1,2,3,4,5}
b={1,2,3,6}
for i in a:
a.add("hari")
a.pop()
a.remove("hari")
a.update(b)
print(a)
a.add("hari")
a.remove("hari")
print(a)

a=12>>1
print(a)

class att:
    # def __init__(self,name) :
    #     self.name=name
        
    def person(self):
        self.name=name
        return "my name is {}".format(self.name)
        
a=att("hari")
print(a.person())
# class att:
    def __init__ (self, name, age=8):
        self.name = name
        self.age=age
    def person(self): 
        return "my name is {}\niam {} old" .format(self.name,self.age)
p1=att("hari")
p2=att("vicky",19)
print(p1.person())   
print(p2.person())



d=17
c=d<<2
print(c)
L=[]
for i in range(1,6):
    if i%2==0:
        L.append(i)
        print(L)
        
a=[1,2,3,4,5,"hari","else"]
l=[]
l1=[]
for i in a:
    if i==str(i):
        l.append(i)
        # pass
    else:
        l1.append(i)
print(l)
print(l1)
lst=[8,7,5,4,2,1,3]  
for i in range(len(lst)):
    for j in range(i+1, len(lst)):
        if lst[i] > lst[j]:
        #    print(lst[i],lst[j])
           lst[i], lst[j] = lst[j], lst[i] 
           print(lst)  

b=int(input("enter a number to find count of value:"))
c=0
for i in a:
    if i== b:
        c=c+1
print(c)
a=int(input("enter a number:"))
f=1
for i in range(1,a+1):
    f=f*i
print(f)

l=[5,5,5]
f=1
for i in l:
    f=i*f
print(f)
    
l=[1,2,3,-4,-9,9,-8]
n=0
l1=[]
l2=[]
for i in l:
    if i>n:
        l1.append(i)

    else:
        l2.append(i)
print(l1)
print(l2)
        (l1.append(i))
        print(l1)
    else:
        print("hi")
l=["apple","babana"] 
l1=[]
for i in l:
    if i==" ,":
        continue   
    l1.append(i)
    print(l1)
l=[1,2,3,4,5,6,6,7,8,9,7,6,4,2,1]
temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
        print(temp)
        
def att(a):
    return 1 if a==0 or  a==1 else a*att(a-1)
out=5
print(att(out))

for i in l:
    for j in l:
        if i==j:
            l.remove(i)
print(temp)
            l.remove(i)
print(l)
    if i==i:
        temp.append(i)
    for j in temp:
        
    
        
        if i==j:
          l.remove(i)
          l1.append(i)
print(l1)
    if i==6:
        l.remove(6)
        print(l)
    
word=["apple","banana","grape","root"]
# v=["aeiou"]
# for i in a:
#     if i in v:
#         print(i)
# if any(a in 'aeiouAEIOU' for i in a):
#     print(i)
if any(char in 'aeiouAEIOU' for char in word):
    print(char)
a=("this the world apple in list ae")
w=["aeiouAEIOU"]
for i in a:
    if i in w:
        print(i)
Letter = ("check whether the left element is identical to the right element")
vowels = "aeiouAEIOU"
for words in Letter:
    if words in vowels:
     print (words)


def att(a):
    return 1 if a==0 or a==1 else a*(att(a-1))
out=5
print(att(out))
a=int(input())
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
if 2==c or 1==c:
    print("its is prime")
else:
    print("not a prime")

maximum second element in list
temp=[1,2,3,4,5,4,2,4,4,4,4]
l1=[]
for i in temp:
    if i not in l1:
        l1.append(i)
l1=set(temp)
l1=list(l1)
l=[]
b=len(l1)
b=b-1
# print(b)
for i in l1:
    if b>i:
        pass
    else:
        l.append(i)
        c=l[0:1]    
print(l)  
a=len(l1)
for i in l1:
    if a>i:
        print(i)
    
  
a=[1,2,3,4,5,6,7]
b=len(a)
for i in a:
    if i<b:
        print(i)
b=min(a)
print(b)


f=open("file.txt","w")
f.write()
print("written sucessfull")
f.close()


a=7
l=[x if x>5 else -x for x in range(a)]
print(l)

l="GF"
dic = { x: x + 2 for x in l}
print(dic)

l=[1,2,3,4,84,6,7]
l1=[]
while 84 in l:
    l1.append(l.pop())
    if l1[-1]==84:
        l1.pop()
        break
for i in l1[::-1]:
    l.append(i)
    print(l)

while 84 in l:
    l1.append(l.pop())
    if l1[-1]==84:
        l1.pop()
        break
for i in l1[::-1]:
    l.append(i)
    print(l)
while 84 in l:
    l1.append(l.pop(0))
    if l1[-1]==84:
        l1.pop()
        break
for i in l:
    l1.append(i)
    l=l1
print(l)
        
    
for i in l:
    if i not in temp:
        temp.append(i)
print(temp)
    
l={0:1,1:"a",2:"b"}
l[0]="hari"
l[3]="k"
l.pop(3)
print(l)
for i in range()

def att(a):
    return 1 if a==0 or a==1 else a*(att(a-1))
out=5
print(att(out))
a=5
f=1
for i in range(1,a+1):
    f=f*i
print(f)

a={1:2,2:8,3:7,4:5,5:3,6:7,7:5}
del a[1]
a[2]=1
print(a)

a=int(input("enter a number:"))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
if 2==c:
    print("it is a prime number")
else:
    print("it is not aprime number")

def isPowerOfTwo(n):
    if (n == 0):
        return False
    while (n != 1): 
        if (n % 3 != 0): 
            return False
        n = n // 3 
        return True 
    if (isPowerOfTwo(9)):
            print('Yes') 
        else:
            print('No')
            if (isPowerOfTwo(3)):
                print('Yes') 
            else:
                print('No')
def my_function(**kid):
  print("His last name is " + kid["lname"])
my_function()
def person(a):
    print("my name is",a)
person("hari")
f=open("D:/testing/output/bgn-cli", "r+")
print(f.read())
l=[5,6,7,3,1,2,4]
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]

print(l)
l=[3,2,1,6,7,5]
a=len(l)
print(a)
for i in l:
    if i

print("h")
def fact(i):
    if i > 1:
        return i+fact(i-1)
    else:
        return 1

n=int(input(":"))
a=-1
b=1
i=0
while (i < n):
    print(a+b)
    a,b=b,a+b
    i+=1
# for i in range(1,a+1):
#     f=f+i

class att():
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def person (self):
        return " name is {} iam {} years old".format(self.name,self.age)
    
att1=att("hari",18)
att2=att("vicky",19)
print(att1.person())
print(att2.person())

class student:
    def __init__(self,name,company):
        self.name=name
        self.company=company
    def hari(self):
        print("my name is {} iam working in{}".format(self.name,self.company))
    def vicky(self):
        print("my name is {} iam working in {}".format(self.name,self.company))
att=student("hari","jasmin")
att1=student("vicky","jasmin")
att.vicky()
att1.hari()
l=[1,5,3,2,4,6] 
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)    
l=[3,4,"k",2,6,7,"h"]
l1=[]
# for i in l:
    if i==str(i):
        print(i)
    
l=[3,4,11,2,6,7,9,10]
def MAX(l):
    temp=0
    for i in l:
        if i>temp:
            temp=i
    return temp
print(MAX(l))

l=[3,4,11,2,1,6,7,9,10]
temp=l[0]
for i in l:
    if i<temp:
        temp=i
print(temp)

a="this the world"
b=a.replace("e","opp")
print(b)
l=[1,2,3,84,4]
l1=[]
while 84 in l:
    l.append(l.pop())
    if l1=[-1]==84:
        l1.pop()
        break
for i in l1[::-1]:
    l.append(i)
print(l)
        
l=(1,2,3)
print(l)
print(reversed(l))
x = int(input())

if x > 5:

    if x < 8:

        print(x+1)

    else:

        print(x-1)
else:
    print(x)
weight=int(input("enter a weight of person: "))
height=float(input("enter a height of person: "))
print(height)
a=weight/(height**2)
print(a)
if a<18.5:
    print("underweight")
elif a<=25:
    print("Normal")
elif a<=30:
    print("over weight")
else:
    print("obsity")

things = ["text", 0, [1, 2, 8], 4.56]
print(things[2][2])
str = "Hello world!"
print(str[7])

nums = [1, 2, 3, 4, 5]

nums[3] = nums[1]

print(nums[3])



x = [2, 4]

x = x * 3

print(x[3])

x = [2, 4]
       
x += [6, 8]

print(x[2]//x[0])

nums = [10, 9, 8, 7, 6, 5]
nums[0] = nums[1] - 5
print(nums)
if 4 in nums:
  print(nums[3])
else:
  print(nums[5])

How many numbers will this code output?

nums = [4, 7, 3, 1]

for x in nums:

    print(x*2)


list = [2, 3, 4, 5, 6, 7]
for x in list:
   if(x%2==1 and x>4):
      print(x)
      break
nums = [1, 2, 3, 4]

res = 0

for x in nums:

    if x%2==0:

        continue

    else:

        res += x
        print(res)
nums = list(range(5))
print(nums[4])
print(range(20) == range(0, 20))
x = range(5)
print(x)
nums = list(range(3, 15, 2))
print(nums[2])
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
print(sqs[1::4])

list = ["a", "b", "c", "d"]
a = list[0:2]
print(a)
sqs = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]

print(sqs[7:5:-1])

nums = [1, 2, 3, 4, 5, 6]

res = nums[::-1]

print(res[2])
names="names"
a=names[1:-1]
print(a)
n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)
n = [2, 4, 6, 8]
res = 1
for x in n[1:3]:
  res *= x

print(res)

list = [1, 1, 2, 3, 5, 8, 13]
print(list[list[4]])
for i in range(10):
    
  if not i % 2 == 0:

    print(i+1)


3
43 Comments
How many arguments are in this function call?

range(0, 100, 5)

nums = [9, 8, 7, 6, 5]
nums[0]=3
nums.insert(2, 11)
print(nums)
nums.append(4)

nums.insert(2, 11)

print(len(nums))
nums = [1, 3, 5, 2, 4]
a=max(nums)+min(nums)
print(a)
res = min(nums) + max(nums)

print(res)
nums = [2,4,8,9,5]


nums.insert(1, 3)

nums.remove(9)

nums.insert(0, nums.count(8))
print(nums)
print(nums[3])

with open("test.txt","r") as file:
    data = file.read()
    list = data.split(" ")
    str=str(list)
    with open("new.txt","w") as file1:
        file1.write(" ".join(list))

print("{0}{1}{0}".format("abra", "cad"))
l=[]
import re
with open ("D\bgn-cli.log") as f:
    a=f.read()
b="DEBUG","ERROR"
c={}.fromkeys(b,0)
l = re.split('\s|.:',a)
for i in l:
    if 'DEBUG' in i or 'ERROR' in i:
        c[i]+=1
print(c)

print(c)
for i in a:
    #print(i,b[0],b[0] in i)
    if b[0] in i:
        c[b[0]]+=1
    elif b[1] in i:
        c[b[1]]+=1
print(c)

print("DEBUG" in l)

    print(i)
  
    print(i)
    
    # print(i)
    # print(i)
 
a="there is skyeeeeeeeeeeeeeeeeeeeeeeeeee  in a"
b="eis","th"
c={}.fromkeys(b,0)
print(c)
for i in a:
    if i in c:
        c[i]+=1
print(c)
    
b=["DEBUG","ERROR"]
c={}.fromkeys(b,0)
l1=list(a,a.sp)
print(l1)
for i in l1:
    print(i)
c=list(a)
v="".join(a)
for i in v:
    l.append(i)
print(l)
# k="".join(l)
# print((type(k)))
# print(type(c))
print(typ)
v=list(a)
print(v)
b=["DEBUG","ERROR"]
c={}.fromkeys(b,0)
for i in v:
    print(i)
    if i in c:
        c[i]+=1
print(c)      
txt = "hello"
print(max(txt))
def foo():
    
   print(1)

   print(2)


foo()

foo()
print(a)


l=[1,2,3,4,5,6]
for i in l:
    if i%2==0:
        print(i)
a=int(input(":"))
b=int(input(":"))
for i in range(a,b+1):
    if i>1:
        for j in range(2,i+1):
            if i%j==0:
                break
            else:
                print(i)
l=[]
c=0
for i in range(a,b+1):
    print(i)
for j in range(1,5):
    print(j)
             l.append(j)
print(l)
        print(j,end="")
        if i%j==0:
       
            
            c=c+1
            # print(i)
            if 2==c:
                
def func(**kwargs):
  print(kwargs["zero"])

func(a = 0, zero = 8)
    

class att:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def person(self,place):
        return "my name is {}\niam years {} old my {}".format(self.name,self.age,place)
att1=att("hari",18,"han")
att2=att("vicky",19,"han")
print(att1.person("han"))
print(att2.person("han"))

class sub:
    def __init__ (self,name,):
        self.name=name        
    


Python code to demonstrate how parent constructors
are called.

parent class
class Person(object):

	# __init__ is known as the constructor
	def __init__(self, name, idnumber):
		self.name = name
		self.idnumber = idnumber

	def display(self):
		print(self.name)
		print(self.idnumber)

# child class


class Employee(Person):
	def __init__(self, name, idnumber, salary, post):
		self.salary = salary
		self.post = post

		# invoking the __init__ of the parent class
		Person.__init__(self, name, idnumber)


# creation of an object variable or an instance
a = Employee('Rahul', 886012, 200000, "Intern")

# calling a function of the class Person using its instance
a.display()

class att:
    def __init__(self,name,idnumber):
        self.name=name
        self.idnumber=idnumber
    def display(self):
        print(self.name)
        print(self.idnumber)
class att1(att):
    def __init__(self, salary, post):
        self.salary=salary
        self.post=post
        att.__init__(self,name,idnumber)
a=att1("hari",1547,14000,"test")
a.display()

task

multulyping list
l=[1,2,4,5,6]
f=1
for i in l:
    f=f*i
    print(f)

find factorela number
a=int(input())       
f=1
for i in range(1,a+1):
    f=f*i
print(f)

printing prime numbers given range
a=int(input("eneter a number:"))
b=int(input(":"))
l=[]
for i in range(a,b+1):
    if i>1:
        for j in range(2,b):
            if i%j==0:
                break
            else:
                l.append(i)
# temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
print(temp)
                
   
sorting is list 
for i in range(len(l)):
    for j in range(i+1,len(l)):
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]
print(l)

checking a prime number bu the user
a=int(input("enter a prime numbers :"))
c=0
for i in range(1,a+1):
    if a%i==0:
        c=c+1
if 2==c:
    print("it is prime")
else:
    print("not a prime")  


set methods
l={1,2,3,4,5,65}
l1={1,2,7}
l.update("hari")
print(l)
l.update("hari","han")
print(l)
l.add("join")
print(l)
l.remove(1)
l.clear()
print(l)


list methods
l+=["hari"]
l.append("vicky")
l.remove("hari")
l.pop(-1)
l.insert(1,"hari")
print(l)
l[1]="vicky"
print(max(l))
print(min(l))


dict practice

l={1:2,3:4,5:6,7:8}
a=int(input("enter a key in dict:"))
b=int(input("enter a value in dict "))
for i in l:
    if l[i]==b:
        print("value already exists")
        break
    else:
        l[a]=b
        print(l)
        print("its is new  dict as created")
        break
       
l1={"game":"kan"}
l[1]="hari"
l[9]="vicky"
print(l[3])
l.pop(1)
l.update(l1)
del l["game"]
print(l)
for i in l:
    print(l[i])
 
 
 
 common practice
l = ["M", "na", "i", "Ke"]
l1 = ["y", "me", "s", "lly"]
l2=[i+j for i,j  in zip(l,l1)]
print(l2)

l = [1, 2, 3, 4, 5, 6, 7]
l1=[]
c=0
for i in l:
    c=i**3
    l1.append(c)
print(l1)  


l = [10, 20, 30, 40]
l1 = [100, 200, 300, 400]
a=(l1[::-1])
for i,j in zip(l,a):
    print(i,j)

l= ["Mike", "", "Emma", "Kelly", "", "Brad"]
for i in l:
    if i=="":
        l.remove("")
print(l)


l = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
a=(l[2])
b=(a[2])
b.insert(2,7000)
l[2][2].append(7000)
print(l)
    
    
l = ["a", "b", ["c", ["d", "e", ["f", "g"], "k"], "l"], "m", "n",["g","i"]]
l1 = ["h", "i", "j"]
l2=l[4][2][24]
print(l2)
l=[5,4,2,7,4,4]
b = {}
for i in range(0,len(l), 2):
    b[l[i]] = l[i+1]
print(b) 

l=[1,1,1,2,3,4,5]
temp=[]
for i in l:
    if i not in temp:
        temp.append(i)
print(temp)

l=[1,1,1,1,1,1,2,2,2,2,3,3,3,3]
import collections
a=collections.Counter(l)
a=dict(a)
print(a)

l=[1,1,1,1,1,1,2,2,2,2,3,3,3,3]
c=[1,2,3]
b={}.fromkeys(c,0)
for i in l:
    if i in b:
        b[i]+=1
print(b)

a=int(input(":"))
l=[1,2,3,4,5]
for i in range(a):
    if a in l:
        b=i
print(b)
l = ['p', 'q']
l1=
n=4
a=["{}{}".format(x,y) for y in range(1,n+1) for x in l ]
print(a)
a=["{}{}".format(x,y) for y in range(1,n+1) for x in l]
print(a)
l1=[]
l1=['{}{}'.format(x, y) for y in range(1, n+1) for x in l]
# print(l1)
for i in l:
    for j in range(1,n+1):
        # print(j) 
        print(i)    
        a=i+str(j)
        print(a)
        l1.append(a)
        n=(len(l1)//2)
        s=l1[1:n+1]
        o=l1[n+1:]
print(l1)
print(o)

# for i in (l):
    for j in range():
   l.apeend(i)
    for j in range(1,n)
     
['p1', 'q1', 'p2', 'q2', 'p3', 'q3', 'p4', 'q4'] 
l=[0,1,2,3,4,5]
l1=[]
l2=[]
l3=[]
c=0
for i in range(0,len(l),2):
    l1.append(i)
    for j in range(1,len(l),2):
        l2.append(j)
        l2=(set(l2))
        l2=list(l2)
for j in rNGEWE3-2F34DQ 233333333333333WP
l1[i]+=l2[i] 
print(l1) 
print(l2)   
for i in range(len(l)+1):
    for j in range(1,len(l)+1):
        if c<a:
            l[i],l[j]=l[j],l[i]
            c=c+i
            break
        else:
            break       
print(l)










for i in range(0,len(l)+1):
    # print(i)
    # l[i],l[i+1]=l[i+1],l[i]
    # print(l)
#     print(i)
    if a>c:
        l[i],l[i+1]=l[i+1],l[i]
        i=i+2
        print(l)
        c=c+i
    else:
        break 
print(l)



c= "Red", "Green", "Orange", "White"
c1 = "Black", "Green", "White", "Pink","Red"
for i in c:
    for j in c1:
        if i==j:
            print(i)
c=set(c).intersection(set(c1))
print(c)


l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14]
a=(len(l)//2)
b=l[0:a]
j=0
o=0
c=l[a::]
k=0
l1=[]
# print(c)
for i in range(len(l)+2):
    if o<=a:
        # print(k,end="")
        o=o+i-1
        u=b[k]
        h=b[k]=c[k]
        j=c[k]=u
        k=k+1
        l1.append(h)
        l1.append(j)
    else:
        break      
print(l1)
0,2,4,6
1,3,5,7






swap two number in list
l=[1,2,3,4,5,6,7,8,9,10,11,12,13,15,1,2,3,4,15]
a=0
b=1
n=1
try:
    for i in range(len(l)):
        c=l[a]
        l[a]=l[b]
        l[b]=c
        if a<(len(l)-2):
            a=a+2
            b=b+2
            n=n+1
        else:
            print(l)
            break
except:
    print("Given list out of index plz check input")

c = "Red", "Green", "Orange", "White"
c2 = "Black", "Green", "White", "Pink"
b=set(c).intersection(set(c2))
print(b)

l = [11, 33, 50]
s = ''
for i in l:
    s += str(i)
print(int(s))
l=[]
l1=[]
for i in range(1,22):
    l.append(i)
for j in range(len(l)):
    print(l)
    l[j]+=l1
    
a="dwbfweblhgfewlfbweufewufewufuuuuuuuu1234567" 
import collections
b=dict(collections.C(a))
print(b)
l= ['apple', 'banana', 'cherry', 'date', 'elderberry', 'fig', 'grapefruit', 'honeydew']
l1=[]
for i in range(len(l)):
    a=l[i][0]
    l1.append(a)
a=dict(zip(l1,l))
print(a)
    break
L = [11, 33, 50]
print("Original List: ",L)
x = ("".join (map(str,L)))
print("Single Integer: ",x)
x = int("".join(map(str, L)))


l = ['be','have','do','say','get','make','go','know','take','see','come','think','look','want','give','use','find','tell','ask','work','seem','feel','leave','call']
a=input("enter a word check in list already or not:")
for i in range(len(l)):
    if l[i][0]==a:
        print(l[i])
else:
    print("no letter found!!")
    break
obj={}
for i in range(1,21):
    obj[str(i)]=[]
print(obj)
l=[]
l1=[]
l2=[]
for i in range(1,21):
    l.append(i)
    l2.append(l1)
a=dict(zip(l,l2))
print(a)
l= ['a','b','c','d','e','f']
l1= ['d','e','f','g','h']
for i in l:
    for j in l1:
        if i==j:
            print(i,end="")

l= [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in l:
    if i%2!=0:
        print(i)
class att():
    def __init__(self,name,age) :
        self.name=name
        self.age=age
        # self.place=place
    def person1(self,place):
        return "my name is {} \niam {} years old{}".format(self.name,self.age,place)
att1=att("hari",18)
print(att1.person1("h"))
        
class att:
    def __init__(self,name,age,place):
        self.name=name
        self.age=age
        self.place=place
    def person(self,place):
        return "my name is {}\niam years {} old my {}".format(self.name,self.age,place)
att1=att("hari",18,"han")
att2=att("vicky",19,"han")
print(att1.person("han"))
print(att2.person("han"))

a="rfehgujvrhoenjhioj"
c=("rf")
b={}.fromkeys(c,0)
for i in a:
    if i in b:
        b[i]+=1
print(b)
print("hi")
l = ["Black", "Red", "Maroon", "Yellow"]
l1 = ["#000000", "#FF0000", "#800000", "#FFFF00"]
a=["color_name"]
for i in l:
    b=(a[0]+=i)
    print(b)

c = ["red", "orange", "green", "blue", "white"]
c2= ["black", "yellow", "green", "blue"]
c1=set(c)
b=set(c2)
a=list(c1.difference(b))
print(a)
color = ['red', 'green', 'orange']

a= "".join(color)
print (a) 

x = [(4, 1), (6, 2), (6, 0)]
l=[]
i=0
j=1
for i in range(len(x)):
    b=x[i][j]
    i=i+1
    l.append(b)
    a=min(l)

  
  
  
    if a in x:
        print(a)
    else:
        print("hi")
 
for i in x:
    print(i)
        
l=[3,2,1,4,5]   
for i in range(len(l)):
    for j in  range(i+1,len(l))   :
        if l[i]>l[j]:
            l[i],l[j]=l[j],l[i]   
print(l)          
        
l=['abcd', 'abc', 'bcd', 'akie', 'cder', 'cdsw', 'sdfsd', 'dagfa', 'acjd']
a=input("enter a first letter to find out:")
j=0
for i in l:
    if a in l[j][0]:
        print(i)
    j=j+1
else:
    print(" sorry word not found try agin ")

l=[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]
l=set(l)
l=list(l)
print(type(l))
# temp=[]
# for i in l:
#     if i not in temp:
#         temp.append (i)
print(temp)






