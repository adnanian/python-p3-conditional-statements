#!/usr/bin/env python3

# import ipdb


def admin_login(username, password):
    # your code here
    pass
    if username == "admin" or username == "ADMIN":
        if password == "12345":
            return "Access granted"
    return "Access denied"


def hows_the_weather(temperature):
    # your code here
    pass
    if temperature < 40:
        return "It's brisk out there!"
    elif temperature >= 40 and temperature <= 65:
        return "It's a little chilly out there!"
    elif temperature > 85:
        return "It's too dang hot out there!"
    else:
        return "It's perfect out there!"


def fizzbuzz(num):
    # your code here
    pass
    is_multiple_of_3 = "Fizz" if num % 3 == 0 else ""
    is_multiple_of_5 = "Buzz" if num % 5 == 0 else ""
    
    output = (
        num
        if not (is_multiple_of_3 or is_multiple_of_5)
        else str(is_multiple_of_3 + is_multiple_of_5)
    )
    # ipdb.set_trace()
    return output


def calculator(operation, num1, num2):
    # your code here
    pass
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        return num1 / num2
    else:
        print("Invalid operation!")
        return None
