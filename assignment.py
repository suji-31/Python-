# Task 1
mark = int(input("enter the mark:"))
if mark>90:
    print(mark,"A Grade:")
elif mark > 80:
    print(mark,"B Grade:")
elif mark > 70:
    print(mark,"C Grade:")
elif mark > 60:
    print(mark,"D Grade:")
else:
    print("Grade F:")

# task 2
#define the price rules for weekdays and weekends:
age=int(input("enter the age:"))
day=str(input("enter the day:"))
weekdays=["Monday","Tuesday","wednesday","Thursday","Friday"]
weekends=["Saturday","Sunday"]

#check if the day is a weekday or weekend
if day in weekdays:
    if age<18:
        print("ticket price:$12")
    else:
        print("ticket price:$15")
elif day in weekends:
    if age < 18:
        print("ticket price:$15")
    else:
        print("ticket price:$20")
else:
    print("None")

# Task 3
purchase=int(input("enter the total purchase amt:"))
permim=input("enter yes or no:")
if permim:
    print("delivery and total charge:")
elif >$50:
    print("total amt paid:")
elif <$50:
    print("total amt paid:")
else:
    print("amt")
