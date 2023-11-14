# Using break statement
for number in range(1, 11):
    if number == 5:
        print("Condition met. Exiting loop.")
        break
    print("Current number:", number)
print("Loop finished.")