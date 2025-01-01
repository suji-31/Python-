# Conditional Statements:
#example:
x=int(input("enter the value:"))
if x>0:
    print("number is positive")
elif x>0:
    print("number is negative")
else:
    print("number is zero")

#task 1
x = int(input("enter the number:"))
if x%2==0:
    print("even")
else:
    print("odd")
    
#Task 2
days = int(input("enter the day:"))
if days == 1:
    print("monday")
elif days == 2:
    print("tuesday")
elif days == 3:
    print("Wednesday")
elif days == 4:
    print("thursday")
elif days == 5:
    print("friday")
elif days == 6:
    print("saturday")
elif days == 7:
    print("sunday")
else:
    print("invalid days")
    
#Task 3
x = int(input("enter the number"))
if x%2==0 and x%3==0:
    print("divisible by 2 and 3")
else:
    print("not divisible by 2&3")
    
# Task 4
ch=(input("enter the value"))
if ((ch>="A" and ch<="Z")or(ch>="a" and ch<="z")):
     print("iits a Alphabet.")
elif(ch>="0" and ch<="9"):
    print("its a number value.")
else:
    print("special character.")

# task 5
unit=int(input("enter the unit:"))
cost=float(input("enter the cost:"))
if unit<=100:
    cost=unit*5.0
    print(unit,cost,"EB BILL")
elif unit>=100:
    cost=(unit-100)*7.50
    print(unit,cost,"EB BILL")
elif unit>=200:
    cost=100*7.50+(unit-100)*10.0
    print(unit,cost,"EB BILL")
else:
    print("No BILL")
    
# Task 6&7
bmi=int(input("enter the Bmi:"))
if bmi<18.5:
    print("UnderWeight.")
elif 18.5<=bmi<24.9:
    print("Normal Weight.")
elif 25<=bmi<29.9:
    print("OverWeight")
elif bmi>=30:
    print("Obeise.")
else:
    print("None.")

# Task 8:
year = int(input("enter the year:"))
if((year%4==0 and year%100!=0)) or (year%400==0):
    print("its a leep year")
else:
    print("its a not leep year")

# Task 9:
string = input("enter the string:")
if(string == string[::-1]):
    print("its a palindrome")
else:
    print("its not a palindrome")

#task 10:
n=int(input("enter the number:"))
if n%2==0:
    print(n,"is not a prime number")
else:
    print(n,"is a prime number")

# Task 11:
num = int(input("enter - 3 digit number:"))
if num%2==0 and num%3==0:
    print("is a armstrong")
else:
    print("not armstrong")

# task 12
x = int(input("enter the number:"))
if x%3==0 and x%5==0:
    print("divisible by 3 and 5")
else:
    print("not divisible by 3&5")

#task 13
select = int(input("select operation 1,2,3,4,5:"))
x=int(input("enter the number:"))
y=int(input("enter the number:"))
if select == 1:
    print(x+y,"addition")
elif select==2:
    print(x-y,"subtraction")
elif select==3:
    print(x*y,"multiple")
elif select==4:
    print(x/y,"division")
else:
    print("none")



    
    
