# Michael Jivan
# 3/29/22
# Simple script to get you a simple password with phrases, numbers and special characters

import random 

def generatePassword():
    password = ""
    words = ["Cat", "Dog", "RandomWord", "Castle", "Computers"]
    numbers = "1234567890"
    special_chars ="!@#$%^&*"
    
    password += words[random.randrange(0, len(words))]
    password += numbers[random.randrange(0, len(numbers))]
    password += special_chars[random.randrange(0, len(special_chars))]
    
    return password

print(generatePassword())
