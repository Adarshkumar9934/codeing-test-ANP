
# write a python program to validata if  a string is  a valid palindrome igroning space punctatuation
import string

def is_palindrome(s):
    # Remove spaces and punctuation, and convert to lowercase
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    
    # Check if the cleaned string is equal to its reverse
    return cleaned == cleaned[::-1]

# Test the function
input_string = input("Enter a string: ")
if is_palindrome(input_string):
    print("The string is a valid palindrome.")
else:
    print("The string is not a valid palindrome.")
