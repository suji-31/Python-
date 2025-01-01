#Function:
   #Syntax:-
        #Def function_name:
            #Code

def display():
    print("hello world")
display()

display()
for i in range(5):
    display()

def total(x,y):
    z=x+y
    print(x)
    print(y)
    print(z)
total(12,13)

#Types of arguments:
     #4 types of arguments.
       # 1.positional - normal fun method.
       # 2.keyword - value is mentioned.
       # 3.default - only one value will be mention anthor value auto calculate.
       # 4. variable length - one single variable,another one multi variable can
# handled it.

#keyword Arguments:
def total(x,y):
    z=x+y
    print("value of x is",x)
    print("value of y is",y)
    print(z)
total(y=56,x=10)
    #First x or y value will be mention to accept for the keyword argument.

#Default Arguments:
def total(x,y=567):
    z=x+y
    print(x)
    print(y)
    print(z)
print(total(156))

#Variable length:
def total(x,*y):
    print("value of x is",x)
    print("value of y is",y)  #first value will be captured first value only.
    #second values its taken the last 3 positional num
    result=x+sum(y)
    print("total value is",result)
total(10,36,78)

