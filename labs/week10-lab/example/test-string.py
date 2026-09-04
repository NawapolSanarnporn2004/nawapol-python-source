password = input("Insert your password")
length = len(password)
check = password.isalnum()

if length > 8 and check == False:
    print("Your password is strong!")
else:
    print("Your password isn't strong!")