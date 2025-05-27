# Write a program that takes a string input and prints whether it’s numeric or not.
user_input = input("Enter a String: ")
messages = ["The input is not numeric.", "The input is numeric."]
print(messages[user_input.isnumeric()])


# .isnumeric(): checks if the input has only digits.
# user_input.isnumeric() returns True or False
# In Python, True == 1 and False == 0
# So it prints:
#   -> messages[0] → "The input is not numeric."
#   -> messages[1] → "The input is numeric."