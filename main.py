class Student:
    def __init__(self, name="none"):
        self.name = name

    def __str__(self):
        return f"Hello, my name is {self.name}"

    def __del__(self):
        print("i am graduated))))")


stud1 = Student("Maria")
stud = Student("Andriy")
print(stud)
print(stud1)












# class Student:
#     amount_of_students = 0
#
#     def  __init__(self, height=0, name="noname", mark=0):
#         self.name = name
#         self.height = height
#         self.mark = mark
#         print("Зріст:",self.name, self.height)
#         Student.amount_of_students += 1
#     def growUp(self):
#         self.height += 10
#
#     def growMark(self, mark=0):
#         self.mark += mark
#
#
#
# stepan = Student()
# maxym = Student(height=180, name="Максим", mark= 12)
# kate = Student(height=170, name="Катя", mark= 2)
#
# print(maxym.mark)
# maxym.growMark(2)
# print(maxym.mark)
#
# print(kate.mark)
# kate.growMark()
# print(kate.mark)
#
#
#
#
# print(maxym.height)
# maxym.growUp()
# print(maxym.height)
#
# print(Student.amount_of_students)


# print("Зріст Макса:", maxym.height)
# print("Зріст Макса:", kate.height)
# print("Зріст Макса:", stepan.height)
