def check_number(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0


user_input = int(input("Enter a number: "))  

result = check_number(user_input)

if result == 1:
    print("The number is positive.")
elif result == -1:
    print("The number is negative.")
else:
    print("The number is zero.")

