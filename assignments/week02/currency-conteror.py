# Currency Converter (20 points) [by Nawapol Sanarnporn 6830252229]

# Exchange rate
rate = 35.5  # 1 USD = 35.5 THB

# Ask user for conversion direction
print("Choose conversion direction:")
print("1. THB to USD")
print("2. USD to THB")

choice = input("Please enter 1 or 2: ")

# Conversion logic
if choice == "1":  # THB to USD
    amount = float(input("Enter amount in THB: "))
    usd = amount / rate
    print(f"{amount:.2f} THB = '' {usd:.2f} USD ''    //  Formula: USD = THB / {rate}")
    print("Have a good day!")
elif choice == "2":  # USD to THB
    amount = float(input("Enter amount in USD: "))
    thb = amount * rate
    print(f"{amount:.2f} USD = '' {thb:.2f} THB ''    //  Formula: THB = USD * {rate}")
    print("Have a good day!")
else:
    print("Invalid choice! Try again.")


