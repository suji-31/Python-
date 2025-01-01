#Dictionary :
# (KEY:VALUES)

dic={'student name':'suji','Age':20,'address':'kovil street','phone no':'xxxxx'}
print(dic)
print(type(dic))
print(len(dic))

dic={'student name':'suji','Age':20,'address':'kovil street','phone no':979005}
print(dic)

#UPDATE(add)VALUES:
dic.update({'blood group':'A2+ve'})
print(dic)
print('--'*15)
#Change Key Values:
dic['Age']=21
print(dic)

#Remove Items:
dic.pop('phone no')
print(dic)

#Last Values Remove:
dic.popitem()
print()

#Del Values:
del dic['address']
print(dic)

#Clear
dic.clear()
print(dic)
