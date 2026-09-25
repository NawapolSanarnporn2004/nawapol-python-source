# Deposit Money [by Nawapol Sanarnporn 6830252229]

def deposit(money=1000):
    print(f"ยอดเงินเริ่มต้น: {money} บาท")
    try:
        amount_input = input("กรอกจำนวนเงินที่ต้องการฝาก: ")
        amount = float(amount_input)
        
        if amount <= 0:
            raise ValueError("จำนวนเงินฝากต้องมากกว่า 0")
            
    except ValueError as e:
        if str(e).startswith("could not convert"):
            print("\nเกิดข้อผิดพลาด: กรุณากรอกข้อมูลเป็นตัวเลขเท่านั้น")
        else:
            print(f"\nเกิดข้อผิดพลาด: {e}")
            
    else:
        money += amount
        print("\nฝากเงินสำเร็จ")
        print(f"ยอดเงินคงเหลือ: {money:.2f} บาท")
        
    finally:
        print("สิ้นสุดรายการฝากเงิน")

deposit()

