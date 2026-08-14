# Example 1: Function with default parameter
def greet_with_title(name, title="Mr./Ms."):
    """Greets person with optional title"""
    print(f"Hello, {title} {name}!")

print("Using default parameters:")
greet_with_title("Smith")  # Uses default title
greet_with_title("Johnson", "Dr.")  # Custom title
greet_with_title("Brown", "Prof.")  # Custom title
print()

# สกุลเงินเปลี่ยนแปลง 1 USB = 33 THB
def convert_currency(value, currency):
    result = 0
    if currency == "USD":
        result = value / 33.0
        print(f"{value} THB = {result} USD")
    else:
        result = value * 33.0
        print(f"{value} USD = {result} THB")

convert_currency(100, "USD")
convert_currency(100, "THB")