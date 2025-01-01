# DATA TYPES IN PYTHON:

#LIST VALUES
li=[1,5.0,2,3,4]
print(li)
print(type(li))
print('number of elements is',len(li))
print(li[2])
print(li[-4])

#APPEND VALUES:
li.append(45.0)
print(li)

#MULTIPLE VALUES:
li.extend([2,30,10])
print(li)

#INSERT VALUES:
li.insert(9,88)
print(li)

#ELEMENTS
li=[1,3,6,7,4,5]
print(li)
print(type(li))
print('number of elements is',len(li))

#POP
li.pop()
print(li)
#REMOVEs
li.remove(4)
print(li)
#SUM
print(sum(li))
print(max(li))
print(min(li))
#del
del li[1]
print(li)
#CLEAR
li.clear()
print(li)

print("--"*25)
x={'apple':450,'orange':300,'banana':100,'gova':250}
print(x.keys())
print(x.values())
print(x.items())
print(x.get('orange'))
print(x['banana'])

#COPY:
w=x.copy()
print(x)

#UPDATE
w.update({'pineapple':150})
print(w)

#LIST
list=[2,4,6,8,10]
list1=dict.fromkeys(list)
print(list1)
