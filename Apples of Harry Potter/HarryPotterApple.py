# Practical Problem 2
# Harry Potter have to divide apples within his minimum and maximum number of student.
# Prints weather the input number of apples is divisor or not between the range of min and max.


def harry_potter(number_of_apples, min_students, max_students):
    for num in range(min_students, max_students + 1):
        if number_of_apples % num == 0:
            print(f"  into {num} students equally.")
        else:
            print(f"  not equally into {num} students.")


def harry_input(msg):
    number = input(msg)
    if number.isnumeric():
        return int(number)
    else:
        print("Sorry, you've to input a valid numeric number.")
        harry_input(msg)


apples = harry_input("How many apple do you want to give your students, Harry? ")
min_std = harry_input("Now, what is the number of your minimum students? ")
max_std = harry_input("And how many of your students might be at most? ")

print(f"\nHarry, you can divide {apples} apples,")
harry_potter(apples, min_std, max_std)
