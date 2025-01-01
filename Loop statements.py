# Loop statements:
#example
  #{for item in iterable
     #code}
  #for i in range(1,21):
    #print(i)

x=[12,56,89,90,67,45,90]
for i in x:
    print(i)

name={"suji","raj","suki","kanna"}
for i in name:
    print(i)

for i in range(0,21):
    print(i)

for i in range(1,21):
    if i%2==0:
        print(f'{i}is an even number.')
    else:
        print(f'{i}is an odd number.')

for i in range(-10,10):
              print(i)
    
#While Loop:
i=1
while i>=-10:
    print(i)
    i-=1
#even number
i=2
while i<=10:
    print(i)
    i+=2

#while
count=0
while(count<10):
    count=count+1
    print("Hello world")

#String:
list="Sujitha"
i=0
while i<len(list):
    print(list[i])
    i+=1
#Odd even
i=1
while i<=20:
    if i%2==0:
        print("even:",i)
    else:
        print("odd:",i)
    i+=1
#String and number:
x=[40,50,60,"hello",70,80]
i=0
while i<len(x):
    print(x[i])
    i+=1

#While are subdivided 3 types BREAK,PASS,COUTINUE STATEMENTS.
