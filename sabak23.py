
######################### наследование

class Human:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def get_info(self):
        print(f"Name: {self.name}")
        print(f"Surname: {self.surname}")

class Student(Human):
    def __init__(self, name, surname, university, course, gpa):
        super().__init__(name, surname)
        self.university = university
        self.course = course
        self.gpa = gpa

    def get_info(self):
        super().get_info()
        print(f"University: {self.university}")
        print(f"Course: {self.course}")
        print(f"GPA: {self.gpa}")

# print(issubclass(Student, Human))
# print(issubclass(int, Human))

# st = Student("Erlan", "Kassenov", "KBTU", 4, 3.76)
# st.get_info()




##### Мысал 1
# class Pervash(Student):
#     pass


# s1 = Student()
# print(s1.name)
# s1.test()
# p = Pervash()
# print(p.name)



######################### полиморфизм
# class Temperature:
#     def __init__(self, temp, scala):
#         self.temp = temp
#         self.scala = scala

#     def __init__(self, temp):
#         self.temp = temp
#         self.scala = "C"
    
#     def __init__(self, scala):
#         self.temp = 0
#         self.scala = scala

#     def __init__(self):
#         self.temp = 0
#         self.scala = "C"

# t = Temperature()




################################# андерметод
# class Human:
#     def __init__(self, name, surname, height):
#         self.name = name
#         self.surname = surname
#         self.height = height

#     def __str__(self):
#         return f"I am {self.name}"

#     def __len__(self):
#         return self.heightx

#     def __gt__(self, other_human):
#         return self.height > other_human.height


# human1 = Human("Erlan", "Khassenov", 176)
# human2 = Human("Almira", "Asanova", 168)

# print(human1 > human2)
# print(human2 > human1)
# print(human1) # __str__
# print(len(human1))


######################### инкапсуляция

# class Human:
#     def __init__(self, name, surname, height):
#         self.__name = name
#         self.surname = surname
#         self.height = height

#     def get_name(self):
#         return self.__name

#     def set_name(self, new_name):
#         self.__name = new_name

#     def __str__(self):
#         return f"I am {self.get_name()}"

# human1 = Human("Erlan", "Khassenov", 176)
# human1.set_name("Ernar")
# print(human1)

# print(human1.__get_name())
# print(human1)


###################### cw 23

class Country:
    def __init__(self, p):
        self.population = p

    def getPopulation(self):
        return self.population

    def setPopulation(self, newP):
        self.population = newP

class Canada(Country):
    pass
class Russia(Country):
    pass
class Germany(Country):
    pass