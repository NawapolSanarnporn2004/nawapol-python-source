print("=== PERSONAL INFORMATION VALIDATOR===")
name = input("Enter your name: ")
age = int(input("Enter your age: "))
phone = input("Enter your phone number: ")

print("Validation Results: ")

check_name = False
for char in name:
    if char.isalpha() or char.isspace():
        check_name = True
    else:
        check_name = False
        break

check_age = False
if age >= 18 and age <= 65:
    check_age = True

check_phone = False
if phone.isdigit() and len(phone) == 10:
    check_phone = True

if check_name:
    print("Name: Valid (contains only letters and spaces)")
else:
    print("Name: Invalid")

if check_age:
    print(f"Age: Valid ({age} years old)")
else:
    print("Age: Invalid")

if check_phone:
    print("Phone: Valid (10-digit number)")
else:
    print("Phone: Invalid")


print("Formatted Information:")
print(f"Name: {name.upper()}")
if 18 <= age <= 30:
    print("Age Group: Yound Adult (18-30)")
elif 31 <= age <= 60:
    print("Age Group: Adult (31-60)")
else:
    print("Age Group: Senior")
print(f"Phone: +91-{phone}")
