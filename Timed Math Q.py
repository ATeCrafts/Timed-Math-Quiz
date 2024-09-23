import random
import time

operators = ["+", "-", "*", "/"]

def generateOperator():
    operatorNum = random.randint(0, 3)
    return operators[operatorNum]
operator = generateOperator()

num1 = random.randint(-100, 100)
num2 = random.randint(-100, 100)

while operator == "/" and num2 == 0:
    operator = generateOperator()

start = input("Would you like to answer a math question (y/n)?: ")

while start != "y" and start != "n":
    print("Invalid input!")
    start = input("Would you like to answer a math question (y/n)?: ")

startTime = time.time()

if start == "y":
    print("Q.", num1, operator, num2)
    if operator == "/":
        print("Round to the nearest integer")
    while True:
        try:
            answer = int(input("Answer: "))
            break
        except ValueError:
            print("Invalid input!")
else:
    quit()


if operator == "+":
    if answer == (num1 + num2):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", num1 + num2)

elif operator == "-":
    if answer == (num1 - num2):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", num1 - num2)

elif operator == "*":
    if answer == (num1 * num2):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", num1 * num2)

else:
    if answer == round(num1 / num2):
        print("Correct!")
    else:
        print("Incorrect! The correct answer was", round(num1 / num2))

endTime = time.time()

print("You took", endTime-startTime, "seconds")