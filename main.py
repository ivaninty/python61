class Student:
    def __init__(self, name="none", mark=10):
        self.name = name
        self.mark = mark



    def doHomework(self):
        self.mark += 2


    def playgames(self):
        self.mark -= 3

stud = Student(name="max")
print(stud)

print(stud.mark)
stud.doHomework()
print(stud.mark)



stud.playgames()
print(stud.mark)







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
