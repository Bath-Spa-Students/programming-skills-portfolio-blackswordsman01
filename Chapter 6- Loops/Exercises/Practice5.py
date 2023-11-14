# 0 while loop
largest_number = float('-inf')  

while True:
    user_input = input("Enter a number (enter '0' to exit): ")

    if user_input == '0':
        break

    current_number = float(user_input)

    if current_number > largest_number:
        largest_number = current_number
print("The largest number entered is:", largest_number)