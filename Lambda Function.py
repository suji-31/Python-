#LAMBDA FUNCTION:-
    #Syntax:
            #Lambda arguments_list:expresion.(its a one line arguments)

f=lambda x,y:x+y
print("addition result is",f(10,15))

M=lambda a,b:a if a>b else b
print("max value is",M(20,25))

B=lambda a,b,c:a+b+c
print(B(5,6,8))

#TASK 1
F=lambda x:x*x
print("square is",F(2*7))

#Task-2
string=lambda s:len(s)
print("string",string("Aruvi institute"))

#Task-3
A=lambda a,b:a+b
print("sum of",A(40,50))

#Task-4
average=lambda num:sum(num)/len(num)
print('average number of list',average([1,5,6,8,7]))

#task-5
upper=lambda s:s.upper()
print("uppercase:",upper('hello world'))

lower=lambda s:s.lower()
print("lowercase:",lower('hello world'))

#Task-6
largest=lambda s:s.max()
print("largest string:",max(['Apple','pineapple','bus stand']))

#Task-7
even_number=lambda num:num %2==0
print("even number is:",even_number(4))
print("even number is:",even_number(3))

#Task-8
largest=lambda num:num.max()
print("largest value:",max([30,40,22,65,87]))
      
# 9
lowercase=lambda s:s.lowercase()
print("lowercase:",lower("Hi Greek World"))

#10
shortest=lambda s:s.min()
print("shortest strings:",min(["airport","transport","post office","school"]))

 #Lambda are divided in 3 types,they are:- Filter,Map,Reduce.
#FILTER :
x=[12,13,14,15,16]
f=list(filter(lambda x1:(x1%2!=0),x))
print(f)

#Task-11
z=[22,33,44,55,66]
f1=list(filter(lambda z1:(z1%2==0),z))
print(f1)

#Task-12
string=['apple','pineapple','orange','egg']
vowel=list(filter(lambda s:s[0].upper()in "AEIOU",string))
print(vowel)
                               
#Task-13
y=[3,-4,8,-2,-6,5,-9]
B=list(filter(lambda x:x<0,y))
print(B)
                            
#Map example:
s=list(map(lambda x2:(x2**2),x))
print(s)

#Task-14
A=[2,3,5,7,8,10]
s=list(map(lambda A2:(A2**2),A))
print(s)       
#15
S=['suzi','raj','mano','sri']
s=list(map(lambda s:s.upper(),S))
print(upper)      
#
S1=['suzi','raj','mano','sri']
s=list(map(lambda s:s.lower(),S1))
print(lower)

#Task-16
x=[2,3,4,5,6]
increment=list(map(lambda f:(f+2),x))
print(increment)

#Reduce example:
from functools import reduce
val=[12,14,15,16]
r=reduce(lambda x,y:x+y,val)
print(r)

#tassk-17
from functools import reduce
val=[22,44,55,66]
r=reduce(lambda x,y:x+y,val)
print(r)

#Task 18
from functools import reduce
num=[2,4,5,6]
r=reduce(lambda x,y:x*y,num)
print(r)

#task 19
from functools import reduce
values=[12,14,15,16]
r=reduce(lambda x,y:x if x>y else y,values)
print(r)

#task20
val=[2,3,4,5,6,7,8]
f1=list(filter(lambda x1:(x1%2==0),x))      
s=list(map(lambda x2:(x2**2),f1))
print(s)

#task 21
from functools import reduce
x=[2,3,4,5,6]
F1=list(map(lambda x2:(x2**2),x))       
s=reduce(lambda x,y:x+y,F1)
print(s)

from functools import reduce
z=['apple','banana','orange','plum']
f1=list(filter(lambda s:s[0] in "aeiou",z))
length=map(len,vowel)
max_length=reduce(lambda x,y:x if x>y else y,length)
print(max_length)       
       
