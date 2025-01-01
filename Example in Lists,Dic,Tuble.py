# Example In List:
  #Task 1
list1=[2,33,222,14,25]
print(list1)
print(list1[::-1])

#2nd
names=['Amir','Bear','charlton','daman']
print(names[-1][-1])

#3rd
list1=[1,3]
list2=list1
list1[0]=4
print(list2)

#4th
dic={1:'A',2:'B'}
print(dic)

dict([[1,"A"],[2,"B"]])
print(dict)

a={1,"A",2,"B"}
print(a)

#5th
a={1:5,2:2,3:4}
a.pop(3)  # pop means delete the positional values.
print(a)

#6th
nums=set([1,1,2,3,3,3,4,4])
print(len(nums))

#7th
a={1,2,3}
b=a
a.remove(3)
print(a)

#8th
a=[3,4,[7,5]]
print(a[2][0])

#9th
a={4,5,6}
b={2,8,6}
print(a|b)

#10th
d={'john':40,'peter':45}
print(d['john'])

#11th
example=list("snow world")
example[3]='s'
print("".join(example))

#12th
print("xyyzxyzxzxyy".count('yy',1))

#13th
print("abcdef".find("cd"))

#14th
t=(1,2,4,3)
print(len(t))
print(max(t))
print(t[3])

#15th
a=("check")*3
print(a)

#16th
my_tuble=(1,2,3,4)
my_tuble=my_tuble+(5,6,7) #tuble couldn't be used in append keyword
print(my_tuble)
print(len(my_tuble))

#17th
a=[1,2,3,4]
del a[2]   # this is list format
print(a)

a=(1,2,3,4)
a=a[:2]+a[3:]   # this is tuble format
print(a)


