

# from random import randint

# x = randint(1, 3)

# 1 - камень
# 2 - бумага
# 3 - ножницы

# 77021234567
# 702

# print(x)

#       5
# #1 Cан: 4
# Кате, тагы 2 мумкиндик бар.
# #2 Сан: 5
# Сиз таптыныз! 
# #3 Сан: 5
# Сиз таптыныз!

# a = int(input())
# b = int(input())
# c = int(input())

# print(a * b == c)
# # if a * b == c:
# #     print(True)
# # else:
# #     print(False)

# x = int(input())
# y = int(input())

# if x > 0 and y > 0:
#     print("Оба числа больше нуля")
# elif x > 0 or y > 0:
#     print("Одно из чисел больше нуля")
# else:
#     print("Ни один из чисел не больше нуля")


# x = int(input())
# y = int(input())
# z = int(input())

# if x < y and x < z:
#     print(x)
# elif y < x and y < z:
#     print(y)
# else:
#     print(z)



from random import randint

x = randint(1, 5)

print("1 мен 5 арасында сан жасырылган, тауып кориниз!")

a = int(input("№1 Бир сан енгизиниз: "))

if x == a:
    print("Сиз жендиниз!")
else:
    print("Кате, тагы 2 мумкиндик бар.")
    a = int(input("№2 Бир сан енгизиниз: "))

    if x == a:
        print("Сиз жендиниз!")
    else:
        print("Кате, тагы 1 мумкиндик бар.")
        a = int(input("№3 Бир сан енгизиниз: "))

        if x == a:
            print("Сиз жендиниз!")
        else:
            print("Сиз ултындыныз!")

#       5
# #1 Cан: 5
# Кате, тагы 2 мумкиндик бар.
# #2 Сан: 2
# Кате, тагы 1 мумкиндик бар.
# #3 Сан: 6
# Сиз ултындыныз!



# 1 - камень
# 2 - бумага
# 3 - ножницы

# 77021234567
# 702



# 1 cан: 5
# 2 cан: 6
# операция: +
# + - * /  **   //   %
# 5 + 6 = 11

# 1 cан: 2
# 2 cан: 10
# операция: *
# + - * /  **   //   %
# 2 * 10 = 20