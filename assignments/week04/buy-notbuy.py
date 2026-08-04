# Budget Purchase Decision Program (by Nawapol Sanarnporn 6830252229)

# input
prices = []  # สร้าง List เปล่าสำหรับเก็บราคาสินค้า 6 รายการ

print("Enter prices of 6 items:")
for i in range(1, 7):  # วนลูปจำนวนราคาสินค้า 6 รายการ แล้วเก็บลง List
    while True:
        try:
            price = float(input(f"Item {i}: "))

            if price >= 0:  # ตรวจสอบว่าราคาต้องไม่ติดลบ
                prices.append(int(price) if price.is_integer() else price)  # ถ้าใส่เลขจำนวนเต็ม เช่น 20.0 ให้แปลงเป็น int
                break  # ข้อมูลถูกต้อง ให้ออกจาก while loop เพื่อไปรับสินค้าถัดไป
            else:
                print("Error: Price cannot be negative!")

        except ValueError:
            print("Error: Invalid input! Please enter a numeric price.")

print()  # รับงบประมาณรวม
while True:
    try:
        budget = float(input("Enter total budget: "))
        if budget >= 0:  # ตรวจสอบว่าราคาต้องไม่ติดลบ
            budget = int(budget) if budget.is_integer() else budget
            break  # ข้อมูลถูกต้อง ไปขั้นตอนแสดงผล
        else:
            print("Error: Budget cannot be negative!")
    except ValueError:
        print("Error: Invalid input! Please enter a numeric budget.")

# process
total_spent = 0  # ตัวแปรเก็บยอดใช้จ่ายสะสม
bought_items = []  # List สำหรับเก็บราคาสินค้าที่ซื้อได้
results = []  # List สำหรับเก็บผลการตัดสินใจของแต่ละชิ้น ( status, current_total )

for price in prices:
    if total_spent + price <= budget:  # ตรวจสอบว่า ถ้ารวมราคาสินค้าชิ้นนี้แล้ว ยังอยู่ในงบหรือไม่
        status = "buy"
        total_spent += price
        bought_items.append(price)
    else:
        status = "cannot buy"

    results.append((price, status, total_spent))  # เก็บข้อมูลสำหรับนำไปแสดงผล (ราคา, สถานะ, ยอดรวมขณะนั้น)

remaining_budget = budget - total_spent

# output
print()  # เว้นบรรทัดก่อนเริ่มแสดงผล

for i in range(len(results)):
    price = results[i][0]
    status = results[i][1]
    current_total = results[i][2]
    
    print(f"Item {i+1} = {price} -> {status}")
    print(f"Current total = {current_total}")
    print()

print(f"Bought items: {bought_items}")
print(f"Total spent: {total_spent}")
print(f"Remaining budget: {remaining_budget}")

