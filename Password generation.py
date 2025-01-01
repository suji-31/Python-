import string
import random
length=int(input("enter the password length:"))
print("""choose character set for the password from these:
      1.digits
      2.letters
      3.special characters
      4.exits""")
characterlist=" "
while(True):
    choice=int(input("enter the number"))
    if(choice==1):
        characterlist+=string.ascii_letters
    elif(choice==2):
        characterlist+=string.digits
    elif(choice==3):
        characterlist+=string.punctuation
    elif(choice==4):
        break
    else:
        print("please pick the valid answer")
password=[]
for i in range(length):
#piciking a random character from our character list
    randomchar = random.choice(characterlist)
#appending a random charater to password
    password.append(randomchar)
#printing password as a string
print("the random password is"+"".join(password))
           
