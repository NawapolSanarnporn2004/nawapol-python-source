class ClassName:
    """Class docstring"""

    def __init__(self, value1, value2, value3):
        # Constructor method
        self.attribute = value1
        self.attribute2 = value2
        self.attribute3 = value3

    def method_name(self):
        # Instance method
        return self.attribute

    def method_name2(self):
        return f"{self.attribute2} - {self.attribute3}"


# เรียกใช้งานด้วยการสร้าง Object และส่งค่าจริงเข้าไป
my_obj = ClassName("Val1", "Val2", "Val3")

print(my_obj.attribute)
result_from_method = my_obj.method_name()
print(result_from_method)