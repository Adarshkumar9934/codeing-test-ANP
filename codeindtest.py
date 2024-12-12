# write a python program to validata if  a string is  a valid palindrome igroning space punctatuation
import re

def is_palindrome(s):
    # Remove spaces and punctuation using re.sub, and convert to lowercase
    cleaned = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
    # Check if the cleaned string is the same as its reverse
    return cleaned == cleaned[::-1]

# Get user input
user_input = input("Enter a string to check if it is a palindrome: ")

if is_palindrome(user_input):
    print("The string is a valid palindrome.")
else:
    print("The string is not a palindrome.")
