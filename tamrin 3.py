name = input("Please rnter your first name: ")
family = input("Please enter your last name: ")
lesson1 = float(input("Please enter your grade N.1: "))
lesson2 = float(input("Please enter your grade N.2: "))
lesson3 = float(input("Please enter your grade N.3: "))
average = (lesson1 + lesson2 + lesson3) / 3

if average >= 17:
    result = ("great")
if 12 <= average and average < 17:
    result = ("normal")
if average < 12:
    result = ("fail")

    print("Student's Name", name, family, "their grade's status", result)

