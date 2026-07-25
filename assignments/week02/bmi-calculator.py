# BMI Calculator (20 points) [by Nawapol Sanarnporn 6830252229]

# input
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (m): "))

# process
bmi = weight / (height ** 2)

# output: แสดงค่า BMI ด้วย 1 ตำแหน่งทศนิยม
print("Your BMI is:", round(bmi, 1))

# BMI Categories
if bmi < 18.5:
    print("Underweight !?  <:(      ==  Moderate to High Risk")
elif bmi >= 18.5 and bmi <= 24.9:
    print("Normal weight  :D      ==  No Risk: ระดับปกติ")
elif bmi >= 25.0 and bmi <= 29.9:
    print("Overweight  :/      ==  Low to Moderate Risk")
else:
    print("Obese !  >:(      ==  High Risk")


