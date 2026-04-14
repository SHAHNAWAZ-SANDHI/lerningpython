def main():
    #the for loop here is used to print a pattern of # in the form of a square
    brik(4)
    print("another")
    #the for loop here is used to print a pattern of # in the form of a square but this time we are using string multiplication to print the # instead of using nested for loops
    brik2(4)


#the for loop here is used to iterate through a dictionary of students and their colleges and print them in a formatted way
def brik(num):
    for i in range(num):
        for j in range(num):
            print("#" ,end="")

        print()

#the for loop here is used to print a pattern of # in the form of a square but this time we are using string multiplication to print the # instead of using nested for loops
def brik2(num):
    for i in range(num):
        print("#"*num)
    
#the for loop here is used to iterate through a list of students and print their names along with their index in the list
def collage():
    students = {"sahil":"ssctm", "sarbaj":"hk","mihir":"ssctm","juned":"hk","jainul":"hk","rohan":"ssctm"}
    for s in students:
        print (s, students[s], sep=", ")

#the for loop here is used to iterate through a list of students and print their names along with their index in the list
def students():
    students =["sahil","mihir","atul","kahan","yash","rohan"]

    for i in range(len(students)):
        print(i+1,students[i])

#the for loop here is used to iterate through a list of students and print their names along with their index in the list
def for_loop():
    while True:
        i = int(input("whats the number:"))
        if i>0:
            break

    for _ in range(i):
        print("meow")


#the for loop here is used to iterate through a list of students and print their names along with their index in the list
def while_loop():
    i=0
    while i<3:
        print("meow")
        i+=1


#the for loop here is used to iterate through a list of students and print their names along with their index in the list
main()