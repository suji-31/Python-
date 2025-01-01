#LIST COMPREHENSION:
#Task 1
    #even number:
print("even number 1 to 10".center(25,"*"))
x=[i for i in range(1,11)if i%2==0]
print(x)
#Odd number:
print("even number 1 to 20".center(25,"*"))
x=[i for i in range(1,21)if i%2!=0]
print(x)

#Task 2
  #vowel string
print("vowel".center(25,"*"))
string='Good Evening'
vowel=[char for char in string if char.lower()in"aeiou"]
print(vowel)

#Task 3
  #multiple by 3
print("multiple of 3 1 to 50".center(25,"*"))
num=[x*3 for x in range(1,51)if x%2!=0]
print(num)

#Task4
  #List of words
print("length of the word".center(25,"*"))
word=["hello","word","pyhon","is","awesome"]
lenght=[len(word)for word in word]
print(word)

#Task5
  #Remove a string
print('remove space'.center(25,"*"))
string=["Hi Buddy Welcome To India"]
No_Space=[char for char in string if char!=" "]
print(No_Space)

#Task 6
   #even number 1 to 20
print("even number 1 to 20".center(25,"*"))
number=[x for x in range(1,21)if x%2==0]
print(x)

#Task 7
  #Palindrome
print("palindrome".center(16,"*"))
string=["hello","madam","gear","level","noon","python","radar"]
palindrome=[char for char in string if char==char[::-1]]
print(palindrome)

#Task 8
   #list a word uppercase
print("uppercase".center(10,"*"))
string=['apple','banana','cherry','DATE']
uppercase=[string.lower() for string in string]
print(string)

print("lowercase".center(10,"*"))
string=['APPLE','banana','CHERRY','date']
lowercase=[string.lower() for string in string]
print(string)

#Pattern
for row in range(8):
    for col in range(5):
        print("suja",end=" ")
    print()           
                
