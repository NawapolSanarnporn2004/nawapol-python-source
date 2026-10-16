def get_temperatures():
    temps = [31, 30, 29, 32, 30, 31, 28]
    return temps

def analyze_temps (temp_list):
    average = sum(temp_list) / 7
    high = max(temp_list)
    low = min(temp_list)
    return (average, high, low)

def display_analysis(avg, high, low):
    print("Temperature Analysis for the Week:")
    print(f"Average: %.1f C" % avg)
    print("Highest:", high, "C")
    print("Lowest:", low, "C")

input = get_temperatures()
result = analyze_temps(input)
display_analysis(result[0], result[1], result[2])


"""
    sum = 0
    high = -99
    low = 99

    for temp in temp_list:
        sum += temp

        if temp > high:
            high = temp

        if temp < low:
            low = temp

    average = sum / 7
"""