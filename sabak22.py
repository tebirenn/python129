

# class Human:   # класс
#     number_of_eyes = 2   # атрибут/поля

#     def __init__(self, name, age):   # self - оз озине силтеме
#         self.name = name             # универсальный объект
#         self.age = age

#     def show_info(self): # метод
#         print(f"Name: {self.name}")
#         print(f"Age: {self.age}")
#         print(f"Eyes: {self.number_of_eyes}")
#         print(f"Is elder: {self.is_elder()}\n")

#     def is_elder(self):
#         return self.age >= 18

# human1 = Human("Alan", 21)  # объект
# human2 = Human("Erlan", 17)  # объект
# human3 = Human("Abay", 21)

# human2.age = 20
# # del human2.age

# human1.show_info()
# human2.show_info()
# human3.show_info()



#### is instance
# x = 5
# arr = []

# print(isinstance(human1, Human))
# print(isinstance(x, int))
# print(isinstance(arr, list))

# print(type(human1))
# print(type(5))
# print(type(print))




########################################## cw22

# easy A

# class Point:
#     x = 5
#     y = 10

# pp = Point()

# letter = input()

# if letter == 'x':
#     print(pp.x)
# elif letter == 'y':
#     print(pp.y)
# else:
#     print('Error')


# easy B

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

# x = int(input())
# y = int(input())
# pp = Point(x, y)

# letter = input()

# if letter == 'x':
#     print(pp.x)
# elif letter == 'y':
#     print(pp.y)
# else:
#     print('Error')


# Easy C


# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def dist(self, point):
#         return ((point.x - self.x)**2 + (point.y - self.y)**2)**0.5

# x = int(input())
# y = int(input())
# p1 = Point(x, y)

# x = int(input())
# y = int(input())
# p2 = Point(x, y)

# print(p1.dist(p2))
# print(p2.dist(p1))



# Medium A

# class Rect:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def is_square(self):
#         return self.a == self.b


# a = int(input())
# b = int(input())

# rect1 = Rect(a, b)

# print(rect1.is_square())



# Medum B

# class Rect:
#     def __init__(self, a, b):
#         self.a = a
#         self.b = b

#     def is_square(self):
#         return self.a == self.b

#     def get_perimeter(self):
#         return (self.a + self.b) * 2

#     def get_area(self):
#         return self.a * self.b

#     def get_diagonal(self):
#         return (self.a**2 + self.b**2)**0.5


# a = int(input())
# b = int(input())

# rect1 = Rect(a, b)

# print(rect1.is_square())
# print(rect1.get_perimeter())
# print(rect1.get_area())
# print(rect1.get_diagonal())





# Hard 

# class Shop:

#     phones = {
#         'iphone': 1000,
#         'samsung': 900,
#         'nokia': 500,
#         'xiaomi': 800
#     }

#     busket = {}

#     def get_phone(self, phone):
#         if phone not in self.phones.keys():
#             print("У нас нет такого смартфона!!!")
#         elif phone not in self.busket.keys():
#             self.busket[phone] = 1
#         else:
#             self.busket[phone] += 1

#     def remove_phone(self, phone):
#         if phone in self.busket.keys():
#             if self.busket[phone] == 1:
#                 del self.busket[phone]
#             else:
#                 self.busket[phone] -= 1
#         else:
#             print("Такого товара нет в корзине!!!")

#     def show_busket(self):
#         for phone, cnt in self.busket.items():
#             print(f"Смартфон: {phone}, Количество: {cnt}, Цена за один: {self.phones[phone]}$")
#         print()
    

# shop = Shop()

# shop.get_phone('iphone')
# shop.get_phone('iphone')
# shop.get_phone('iphone')
# shop.get_phone('abc')
# shop.get_phone('samsung')
# shop.get_phone('xiaomi')

# shop.remove_phone('xiaomi')
# shop.remove_phone('iphone')

# shop.show_busket()



############# medium A
# class Soda:
#     def __init__(self, dobavka = ""):
#         self.d = dobavka

#     def show_my_drink(self):
#         if self.d == "":
#             print("Обычная газировка")
#         else:
#             print(f"Газировка и {self.d}")


# s1 = Soda("малина")
# s2 = Soda()

# s1.show_my_drink()
# s2.show_my_drink()

############### Hard 
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a = a
#         self.b = b
#         self.c = c

#     def is_it_triangle(self):
#         try:
#             self.a = float(self.a)
#             self.b = float(self.b)
#             self.c = float(self.c)
#         except:
#             print("Нужно вводить только числа!")
#             return

#         if self.a < 0 or self.b < 0 or self.c < 0:
#             print("С отрицательными числами ничего не выйдет!")
#         elif self.a + self.b > self.c and self.a + self.c > self.b and self.b + self.c > self.a:
#             print("Ура, можно построить треугольник!")
#         else:
#             print("Жаль, но из этого треугольник не сделать.")

# a, b, c = input().split()
# tri = Triangle(a, b, c)
# tri.is_it_triangle()