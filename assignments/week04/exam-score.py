# Exam Score Checker Program (by Nawapol Sanarnporn 6830252229)

# input
scores = []  # สร้าง List เปล่าสำหรับเก็บคะแนน

for i in range(1, 6):  # วนลูปรับคะแนนนักเรียน 5 คน แล้วเก็บลง List
    while True:
        try:
            score_input = float(input(f"Enter score of student {i}: "))

            if 0 <= score_input <= 100:  # ตรวจสอบว่าคะแนนอยู่ในช่วง 0 ถึง 100 หรือไม่
                scores.append(score_input)
                break  # ข้อมูลถูกต้อง ให้ออกจาก while loop เพื่อไปรับคนถัดไป
            else:
                print("Error: Score must be between 0 and 100! Please try again.")

        except ValueError:
            print("Error: Invalid input! Please enter a numeric score.")

# process
processed_results = []  # List เก็บผลลัพธ์คะแนนและสถานะ

for score in scores:
    rounded_score = int(score + 0.5)  # ปัดเศษและแปลงเป็นจำนวนเต็ม โดยให้เลขตั้งแต่ .5 ขึ้นไป ปัดขึ้นเสมอ

    if rounded_score >= 50:  # ตรวจสอบเงื่อนไข ผ่าน/ไม่ผ่าน
        status = "ผ่าน"
    else:
        status = "ไม่ผ่าน"

    processed_results.append((rounded_score, status))  # เก็บผลลัพธ์ที่ประมวลผลแล้วลง List

# output
print()  # เว้นบรรทัดก่อนเริ่มแสดงผล

for i in range(5):
    score = processed_results[i][0]
    status = processed_results[i][1]
    print(f"Student {i+1}: {score} -> {status}")
