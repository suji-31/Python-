""" # PATTERNS IN PYTHON:

 #Reverse pattern:

print("reverse half pattern")
row=5
int(input("enter the rows:"))
for i in range(row+1,0,-1):
    for j in range(0,i-1):
        print("*",end=" ")
    print()

r=5
for i in range(0,r):
    for j in range(0,i-1):
        print("&",end=" ")
    print()
    
#Half pattern:

print("half pattern")
rows=5
int(input('enter the rows:'))
for i in range(0,rows):
    for j in range(0,i+1):
        print("*",end=" ")
    print()
print('--'*25)

#Full pattern:-
for rows in range(5):
    for col in range(5):
        print('*',end=' ')
    print()
#Character pattern:

print("character pattern")
for row in range(4):
      for col in range(4):
          print("TJ",end=' ')
      print()

#Number pattern:
print("number pattern")
for row in range(6):
      for col in range(6):
          print("40",end=' ')
      print()

#Right to left pattern:
n=5
for i in range(n,0):
    for j in range(i):
        print('*',end=' ')
    print()
print('--'*15)
for i in range(n,0,-1):
    for j in range(i):
        print('*',end=' ')
    print()
print('--'*15)
#Diamond pattern:
n=5
for i in range(n):
    for j in range(n-i-1):
        print('',end=' ')
    for j in range(2*i-1):
        print('*',end=' ')
    print()
print('--'*15)
for i in range(n-2,-1,-1):
    for j in range(n-i-1):
        print('',end=' ')
    for j in range(i*2+1):
        print('*',end=' ')
    print()
print('--'*25)
def diamond(rows):
    n=1
    for i in range(1,rows+1):
        for j in range(1,(rows-i)+1):
            print(end='')
        while n!=(i+1):
            print("*",end=' ')
            n=n+1
        n=1
        print()
    k=0
    n=0
    for i in range(1,rows+1):
        for j in range(1,k+1):
            print(end='')
        k=k+1
        while n<=(rows-i):
            print('*',end='')
            n=n+1
        n=0
        print()
rows=5
diamond(rows)"""
n=4
for p in range(0,n):
    print(" "*(n-1-p)+"*"*(p+1))
for rp in range(n-1,0,-1):
    print(""*(n-rp)+"*"*(rp))
    
