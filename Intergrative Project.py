def helloWorld():
    print("This code demonstrates the how to use a print statement.")
    print("Hello World!")
    print("")
    
def inputVariables():
    print("This code shows how to use inputs and variables.")
    name1 = input("What is your name? ")
    print("")
    print("Your name is",name1)
    print("")
    name2 = input("Enter your name: ")
    ID = input("Enter your student ID number: ")
    course = input("Enter your course name and number: ")
    print(name2 + "'s ID is " + ID +"\nand is enrolled in " + course)
    print("")
    
def arithmetic():
    print("This shows how to use different arithmetic operations and assignment statements")
    firstNumber = int(input("Enter a number: "))
    secondNumber = int(input("Enter another number: "))
    sumAnswer = firstNumber + secondNumber
    difference = firstNumber - secondNumber
    product = firstNumber * secondNumber
    quotient = firstNumber / secondNumber
    power = firstNumber ** secondNumber
    print(firstNumber,"+",secondNumber,"=",sumAnswer)
    print(firstNumber,"-",secondNumber,"=",difference)
    print(firstNumber,"*",secondNumber,"=",product)
    print(firstNumber,"\ ",secondNumber,"=",quotient)
    print(firstNumber,"**",secondNumber,"=",power)
    print("")

def formattingOutput():
    print("This section shows how to use the format and float functions.\nThis allows you to format your code in spefic ways.")
    itemName = input("Enter the name of the item: ")
    numItems = int(input("Enter the number of items: "))
    itemCost =float(input("Enter the cost of one item: "))
    totalCost = numItems * itemCost
    print("Item name: ", itemName)
    print("Cost of one item: ", itemCost)
    print("Number of items purchased: ", numItems)
    print("Total cost: $", format(totalCost, "0.2f"), sep='')
    print("")
    
def boolean():
    print("Boolean Expressions are true or false statements.\nThe conditional operators are used to compare the relationship\nbetween two operands.")
    x = 42
    y = 13
    print("")
    print("x=42 and y=13")
    print(x, ">", y, "=", x>y)
    print(x, "<", y, "=", x<y)
    print("")
    print("Next I will show how the and/ or conditions work")
    numBooks=40
    print("There is 40 books")
    print("(numBooks > 5) and (numBooks < 100)",(numBooks > 5) and (numBooks < 100))
    print("(numBooks < 5) or (numBooks > 100)", (numBooks < 5) or (numBooks > 100))
    print("")

def ifElse():
    print("This code shows how if and else loops work")
    grade = 95
    if grade >= 94:
        print("Excellent!")
          
def nestedIfElse():
    print("This sections shows how to use a nested loop.")
    grade = int(input("Enter your grade: "))
    if grade >= 90:
        print("Very Good!")
    else:
        if grade >= 60:
        print("Satisfactory.")
    else:
        print("Poor")

def whileLoops():
    print("While loops are really important in programming, let's see how they work!")
    number = 1
	while number <= 10:
	  if number % 2 == 0:
	     print(number, end= "  ")
  		  number = number + 1
def forLoops():
    print("For loops are used when a condition needs to be checked each iteration.")
    numIterations = 6	
		for x in range(numIterations):
	 	   print(x, end=" ")
    for x in range(5):
		   print(x, end=" ")

def nestedLoops():
    print("This shows how nested loops work")
    height = int(input("Enter height: ")
    for row in range(1, height+1):
        for column in range(row):
            print(row, end=" ")

def main():
    print("Hello! Welcome to my integration project")
    continueProgram = True
    while continueProgram:
        print("Enter choice")
        print("1.Hello World")
        print("2.Input and Variables")
        print("3.Arithmetic Operations")
        print("4.Formatting Output")
        print("5. Boolean Expressions")
        print("6. IF ELSE Statements")
        print("7.Nested IF-ELSE Statements")
        print("8.While Loops")     
        print("9.FOR Loops")
        print("10.Nested Loops")   
        print("11.Quit")
        selection = int(input())
        if selection == 1:
            helloWorld()
        if selection == 2:
            inputVariables()
        if selection == 3:
            arithmetic()
        if selection == 4:
            formattingOutput()
        if selection == 5:
            boolean()
        if selection ==6:
            ifElse()
        if selection ==7:
            nestedIfElse()
        if selection ==8:
            whileLoops()
        if selection ==9:
            forLoops()
        if selection ==10:
            nestedLoops()
        elif selection == 11:
            continueProgram = False
        else:
            print("Try again")
              
    
main()
            
            

