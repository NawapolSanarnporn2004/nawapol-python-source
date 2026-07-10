print("1. Circle Calculator:")
print("   - Ask user for radius")
print("   - Calculate area (π * r²)")
print("   - Calculate circumference (2 * π * r)")
print("   - Use 3.14159 for π")
print()

# input
radius = float(input("Enter radius: "))

# process
area = 3.14159 * radius ** 2
circumference = 2 * 3.14159 * radius

# output
print("Area:", area)
print("Circumference: " + str(circumference))