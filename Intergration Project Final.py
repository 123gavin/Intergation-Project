"""This is my final file for my Intergration Project
___author___ = Gavin Carr
"""


def hello_world():
    """hello_World is used to show how print statements work
    """
    print("This code demonstrates the how to use a print statement.")
    print("Hello World!")
    print("")


def input_variables():
    """input_variable is used to show how inputs are used in python
    """
    print("This code shows how to use inputs and variables.")
    name1 = input("What is your name? ")
    print("")
    print("Your name is", name1)
    print("")
    card_number = input("Enter your student ID number: ")
    course = input("Enter your course name and number: ")
    print(name1 + "'s ID is " + card_number + "\nand is enrolled in " + course)
    print("")


def arithmetic():
    """arithmetic is used to show the basic functions you can use in python
    """
    print("This shows how to use different arithmetic operations "
          "and assignment statements")
    first_number = int(input("Enter a number: "))
    second_number = int(input("Enter another number: "))
    sum_answer = first_number + second_number
    difference = first_number - second_number
    product = first_number * second_number
    quotient = first_number / second_number
    power = first_number ** second_number
    print(first_number, "+", second_number, "=", sum_answer)
    print(first_number, "-", second_number, "=", difference)
    print(first_number, "*", second_number, "=", product)
    print(first_number, "\\ ", second_number, "=", quotient)
    print(first_number, "**", second_number, "=", power)
    print("")


def formatting_output():
    """This is the area of the course where we learned how to properly format
    outputs
    """
    print("This section shows how to use the format and float functions."
          "\nThis allows you to format your code in spefic ways.")
    item_name = input("Enter the name of the item: ")
    num_items = int(input("Enter the number of items: "))
    item_cost = float(input("Enter the cost of one item: "))
    total_cost = numItems * itemCost
    print("Item name: ", item_name)
    print("Cost of one item: ", itemCost)
    print("Number of items purchased: ", num_items)
    print("Total cost: $", format(total_cost, "0.2f"), sep='')
    print("")


def boolean():
    """Boolean loop here shows how conditions work. The fist example just
    compares two numbers and the second is the number of books someone has.
    """
    print("Boolean Expressions are true or false statements."
          "\nThe conditional operators are used to compare the relationship\n"
          "between two operands.")
    x = 42
    y = 13
    print("")
    print("x=42 and y=13")
    print(x, ">", y, "=", x > y)
    print(x, "<", y, "=", x < y)
    print("")
    print("Next I will show how the and/ or conditions work")
    num_books = 40
    print("There is 40 books")
    print("(num_books > 5) and (num_books < 100)",
          (num_books > 5) and (num_books < 100))
    print("(num_books < 5) or (num_books > 100)",
          (num_books < 5) or (num_books > 100))
    print("")


def if_else():
    """This shows if_else when it comes to grades in a class.
    """
    print("This code shows how if and else loops work")
    print("Jerry's grade is a 95")
    grade = 95
    if grade >= 94:
        print("Excellent!")


def nested_if_else():
    """This is a nested if else that gives the user a comment depending on
    how well they are doing in the class.
    """
    print("This sections shows how to use a nested loop.")
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Very Good!")
    else:
        if grade >= 70:
            print("Satisfactory.")
        else:
            print("Poor")


def while_loops():
    """While loops are used to for while the loops are happening.
    """
    print("While loops are really important in programming, "
          "let's see how they work!")
    number = 1
    while number <= 10:
        if number % 2 == 0:
            print(number, end="  ")
        number += 1


def for_loops():
    """For loops are showed to use number iterations in a loop before
    entering the loop
    """
    print("For loops are used when a condition needs to be "
          "checked each iteration.")
    num_iterations = 6
    for x in range(num_iterations):
        print(x, end=" ")
        for x in range(5):
            print(x, end=" ")


def nested_loops():
    """The nested loop here shows a persons height and loops it.
    """
    print("This shows how nested loops work")
    height = int(input("Enter height in inches: "))
    for row in range(1, height + 1):
        for column in range(row):
            print(row, end=" ")


def main():
    """The "main" function is what calls the all of the functions from the
    list up so the program can run.
    """
    print("Hello! Welcome to my integration project. "
          "Let's run through some programming skills I learned")
    continue_program = True
    while continue_program:
        print("Enter choice")
        print("1.Hello World")
        print("2.Input and Variables")
        print("3.Arithmetic Operations")
        print("4.Formatting Output")
        print("5.Boolean Expressions")
        print("6.IF ELSE Statements")
        print("7.Nested IF-ELSE Statements")
        print("8.While Loops")
        print("9.FOR Loops")
        print("10.Nested Loops")
        print("11.Quit")
        selection = int(input())
        if selection == 1:
            hello_world()
        if selection == 2:
            input_variables()
        if selection == 3:
            arithmetic()
        if selection == 4:
            formatting_output()
        if selection == 5:
            boolean()
        if selection == 6:
            if_else()
        if selection == 7:
            nested_if_else()
        if selection == 8:
            while_loops()
        if selection == 9:
            for_loops()
        if selection == 10:
            nested_loops()
        elif selection == 11:
            continue_program = False
        else:
            print("Try again. Your options are 1-11.")


main()
"""My project demonstrates all of the elements of coding in python that I 
learned in COP1500
"""
