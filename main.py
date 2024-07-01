import string
import random

length = int(input("Enter password length: "))

print('''Choose character set for password from these: 
      1. Digits
      2. Letters
      3. Special Characters
      4. exit''')

characterList = ""

while (True):
    choice = int(input("Pick a number: "))

    if (choice == 1):
        characterList += string.ascii_letters
    elif (choice == 2):
        characterList += string.digits
    elif(choice == 3):
        characterList += string.punctuation
    elif (choice == 4):
        break
    else:
        print("Invalid choice!")

password = ""

for x in range (length):
    password += random.choice(characterList)


print(f"Your new password is: {password}")


