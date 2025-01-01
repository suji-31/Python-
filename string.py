#strings in python

x="Aruvi institue"
print(x)
print(len(x))
print(type(x))
print(x.title())
print(x.capitalize())
print(x.lower())
print(x.upper())
print(x.casefold())
print(x.swapcase())
print(x.find('i'))
print(x.find('u',1))
print(x.startswith('A'))
print(x.startswith('vi',2,11))
print(x.startswith('vi',1,10))
print(x.endswith('e'))
print(x.endswith('tu'))
print(x.isupper())
print(x.islower())

#Alphanumeric

s1="31suji2004"
print(s1.isalpha())
print(s1.isalnum())
print(s1.isnumeric())

s2="9876"
print(s2.isdigit())
print(s2.isnumeric())
print(x.center(25,'*'))

s3={'hello','world'}
s3=['hello','world']
x='$'.join(s3)
print(x)

#SORTS:(asending order)

data=[11,12,23,34,44,36,78,53,88]
data.sort()
print(data)
print('--'*15)
#reverse:
data.reverse()
print(data)
print('--'*15)
#sort
data.sort()
print(data)
print('--'*15)
#descending
data.sort(reverse=True)
print(data)
print('--'*15)
#program:
x=['suji','raj','siva','anu']
x.sort()
print(x)
x.reverse()
print(x)


# SETS OPERATIONS: used only cruly brakets
s1={12,34,56,'suji',78,'anu',90,45}
s2={22,34,65,'suji',78,'jpr',91,20}
#union:
print(s1.union(s2))
print(s1|s2)
print(s2|s1)
print('*'*15)
#intersection:
print(s1.intersection(s2))
print(s1&s2)
print(s2&s1)
print('*'*15)
# differences:
print(s1.difference(s2))
print(s2-s1)
print(s1-s2)
print('*'*15)
#symmetric differences: spacekey are not use value compare in cap symbol
print(s1.symmetric_difference(s2))
print(s1^s2)
print(s2^s1)

