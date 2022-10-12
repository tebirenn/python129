

# print('START')

# try:
#     print('abc')
# except:
#     print('Ошибка!')


# print('STOP')
# print('STOP')
# print('STOP')
# print('STOP')
# print('STOP')

# try:
#     age = int(input('Введите свой возраст: '))
# except:
#     age = int(input('Введите цифрами: '))


# print('Ваш возраст:', age)




# try:
#     age = int(input('Введите свой возраст: '))
# except:
#     age = int(input('Введите цифрами: '))


# if age < 0:
#     raise ValueError('Некорреткный возраст!')
# else:
#     print('Ваш возраст:', age)



# try:
#     div = int(input())

#     print(100 / div)

#     d = {}
#     d['qwerty']
# except ZeroDivisionError:
#     print('На ноль делить нельзя!')
# except NameError:
#     print('То что вы используете нет в нашом языке!')
# except ValueError:
#     print('Введите только целое число!')
# except:
#     print('Какая то другая ошибка!')





# try:
#     a = float(input('ребро a = '))
#     b = float(input('ребро b = '))
# except ValueError:
#     print('Вы ввели не цифру!!!')
# except:
#     print('Некая ошибка!')
# else:
#     print(f'Площадь прямоугольника: {a*b}см^2')
# finally:
#     print('Конец')



# age = int(input())

# print('добро пожаловать!' if age >= 21 else 'вам сюда нельзя!')

# def abs(num):
#     return num if num > 0 else -num

# n = float(input())
# print(abs(n))



# s = sum([int(el) for el in input().split()])
# print(['Less', 'Equal', 'More'][s := sum([int(el) for el in input().split()]) // 10 if s <= 10 else 2])


# print(x := 5)
# print(x**2)




######## cw 17

# Easy B

# try:
#     num = int(input())
# except:
#     print('srsly?')
# else:
#     print(num)

# Easy C

# name = input()

# if not name[0].isupper():
#     raise NameError('Ошибка!')

# print('welcome')


# Medium A












#1
# input:   25
# output:  odd

#2
# input:   48
# output:  even

# print('even' if int(input()) % 2 == 0 else 'odd')

# arr = list(map(int, input().split()))
# try: 
#     a, b = arr
# except:
#     a = arr[0]
#     b = int(input())

# print(a + b) 



# input:
# 20 15
# output:
# 35

# input:
# 25
# 15
# output
# 40

# Medium B
# email = input()

# if email.count('@') == 1:
#     print('ok')
# else:
#     raise Exception('ошибка')