def calculate_electricity_cost(units):

    if units > 200:
        cost = 125.00 + 150.00 + 350.00 + ((units - 200) * 4.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print("101-200 หน่วย: 350.00 บาท")
        print(f"201-{units} หน่วย: {(units - 200) * 4.00:.2f} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} บาท")
        print()

    elif units > 100:
        cost = (50 * 2.50) + (50 * 3.00) + ((units - 100) * 3.50) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print("51-100 หน่วย: 150.00 บาท")
        print(f"101-{units} หน่วย: {(units - 100) * 3.50:.2f} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} บาท")
        print()

    elif units > 50:
        cost = 125.0 + ((units - 50) * 3.00) + 25
        print("1-50 หน่วย: 125.00 บาท")
        print(f"51-{units} หน่วย: {(units - 50) * 3.00:.2f} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} บาท")
        print()

    elif units > 1:
        cost = units * 2.50 + 25
        print(f"1-{units} หน่วย: {units * 2.50:.2f} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} บาท")
        print()

    elif units > 0:
        cost = units * 2.50 + 25
        print(f"1 หน่วย: {units * 2.50:.2f} บาท")
        print("ค่าบริการ: 25.00 บาท")
        print(f"รวมค่าไฟทั้งสิ้น: {cost:.2f} บาท")
        print()

    elif units == 0:
        print("ค่าบริการ: 25.00 บาท")
        print("รวมค่าไฟทั้งสิ้น: 25.00 บาท")
        print()

    else:
        print("จำนวนหน่วยไฟฟ้าต้องไม่ติดลบ")
        print()

while(True):
    print("===== โปรแกรมคำนวณค่าไฟฟ้า =====")
    print("1. คำนวณค่าไฟ")
    print("2. ออกจากโปรแกรม")
    choice = input("เลือกเมนู: ")
    if choice == "1":
        print()
        units = int(input("กรอกจำนวนหน่วยไฟฟ้า:"))
        calculate_electricity_cost(units)
    elif choice == "2":
        break
    else:
        print()
        print("หากเลือกเมนูอื่น ให้แจ้งว่าเลือกเมนูไม่ถูกต้อง")