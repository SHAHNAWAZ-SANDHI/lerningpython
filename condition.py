def main():
    x = int(input("enter the number:"))
    if is_even(x):
        print("the nember is even")
    else:
        print("the number is odd")





def num():
    x = int(input("whats the number:"))
    y = int(input("whats the number:"))
    if x < y:
        print("x is less than y")
    elif x > y:
        print("x is greater than y")
    else:
        print("x is equal to y")

def score():
    score = int(input("enter your score:"))
    if score >=90:
        print("score is A")
    elif score>=80:
        print("score is B")
    elif score>=70:
        print("score is c")
    elif score >= 60:
        print("score is D")
    else:
        print("score is F")


def is_even(n):
    if n % 2 ==0:
        return True
    else :
        return False










main()