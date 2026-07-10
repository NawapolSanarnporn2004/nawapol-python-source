print("2. Time Converter:")
print("   - Ask user for seconds")
print("   - Convert to hours, minutes, and remaining seconds")
print("   - Example: 3661 seconds = 1 hour, 1 minute, 1 second")
print()

# input
second = int(input("Insert second: "))

# process
hour = second // 3600
second_remain = second % 3600

minute = second_remain // 60
second_remain = second % 60

# output
print(second, "seconds =", hour, "hour,", minute, "minute,", second_remain, "second")
print(f"{second} seconds = {hour} hour, {minute} minute, {second_remain} second")