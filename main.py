import random
from Question import Question
from Student import Student
from Utils import Methods_Utils
from time import *






def user_signup():

    name = input("\nEnter student fill name: ").split(" ")
    age = input("Enter student age: ")
    address = input("Enter student address: ")
    phone_number = input("Enter student phone_number: ")
    user_name = input("\nEnter Username:  ")
    password = input("Enter Password:  ")

    name = age.join(name)
    if not age.isdigit():
        print("Invalid Age")
        return

    if Methods_Utils.check_value_is_empty(name, age, address, phone_number):
        print("Invalid inputs")
        return
    std = None
    std = Student(name=name, age=age, address=address, phone_number=phone_number, user_name=user_name, password=password)
    return std


print("Welcome, Please Sign Up your info")

std = None

while True:
    std = user_signup()
    if std == None:
        print("Please Sign Up again")
        continue
    break



print("\nWelcome again, please add your credential: ")

while True:
    user_name = input("Username: ")
    password = input("Password: ")

    if Methods_Utils.check_value_is_empty(user_name, password):
        print("Empty fields")
        continue
    elif user_name != std.get_username() or password != std.get_password():
        print("Username and password do not match, Please try again\n")
        continue
    break



sleep(2)


def run_test(questions):
    questions = questions.questions
    score = 0
    print("\n\nYou have 20 multiple choice questions which you must answer: \n\n")
    sleep(5)
    questions = random.sample(questions, 20)
    for question in questions:
        answer = input(question[0])
        if answer == question[1]:
            score += 1
    print("\nYou have reached the end of the quiz\n")
    sleep(2)
    print(f"\n\nYou got {score} / " + str(len(questions)) + " Correct")
questions = Question

run_test(questions)
