# Task 1: Create a Dictionary of Student Marks

stu_marks ={
    "Alice": 85,
    "Mike": 82,
    "Nike": 87
}
user_input = str(input("Enter the student's name: "))
user_input_Captalize = user_input.capitalize()

if user_input_Captalize in stu_marks:
    print("{}'s marks: {}".format(user_input_Captalize,stu_marks[user_input_Captalize]))
else:
    print("student not found")