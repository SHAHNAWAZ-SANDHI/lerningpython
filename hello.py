print ("hello world from python")
# this is a single line comment
hello = input("what do you wanna print?:")
print (hello)
"""
this is multiline comment
you can write anything here and it will not be executed
we can use this to write notes for ourselves or for other people who will read our code
"""
hello = hello.strip() # this will remove any extra spaces from the beginning and end of the string

print ("hello!",hello)

hello = hello.upper() # this will convert the string to uppercase   
print ("hello!",hello)  

hello = hello.lower() # this will convert the string to lowercase
print ("hello!",hello)  

hello = hello.capitalize() # this will capitalize the first letter of the string
print ("hello!",hello)  

hello = hello.replace("hello","hi") # this will replace all occurrences of "hello" with "hi"
print ("hello!",hello)  

hello = hello.replace("hi","hello") # this will replace all occurrences of "hi" with "hello"
print ("hello!",hello)  

hello = hello.title() # this will capitalize the first letter of each word in the string
print ("hello!",hello)  



word = input("enter a word to check if it's a palindrome: ").title().strip() # this will capitalize the first letter of each word and remove any extra spaces from the beginning and end of the string

print ("you entered:",word)

first, second = word.split(" ") # this will split the string into two parts based on the space character and assign them to the variables first and second

x=int(input("enter a number to check if it's even or odd: ")) # this will take input from the user and convert it to an integer
if x % 2 == 0: # this will check if the number is even
    print (x,"is even")
else: # this will execute if the number is odd
    print (x,"is odd")  

    