


# n = 5

# while n < 10:
#     print('Good')
#     n += 2

# print(n)


# n = 13
# n //= 2
# print(n)

# break continue
# n = 1
# while True:
#     print('Good', n)
#     n += 1
#     if n > 15:
#         break
# # ctrl C
# print(n)



# n = 1
# while n < 10:
#     print('Good', n)
#     n += 1
#     if n == 6:
#         break



# n = 1
# while n <= 6:
#     if n == 3:
#         n += 1
#         continue

#     print('Good', n)
#     n += 1
    


# 555
# n = int(input())
# i = 0
# while i < n:
#     print(555)
#     i += 1

# 5
# 1
# 2
# 3
# 4
# 5


# n = int(input()) 
# summ = 0 
# i = 1 
# while i <= n:
#     summ += i
#     i += 1

# print(summ)


# n = int(input())
# cnt = 0
# while n >= 1:
#     n /= 2
#     cnt += 1

# print(cnt)

# n = int(input())
# x = 1
# while True:
#     if x == n:
#         print('yes')
#         break
#     elif x > n:
#         print('no')
#         break
#     x *= 2




# max1 = int(input())
# m2 = False
# while True:
#     x = int(input())

#     if x == 0:
#         break
#     elif x > max1:
#         m2 = True
#         max2 = max1
#         max1 = x
#     elif m2 and x > max2:
#         max2 = x

# print('max2', max2)

# 4
# 3
# 7   max2
# 9   max1
# 5
# 0



# from random import randint

# x = randint(1, 100)

# print('Сизге кездейсок 1-100 арасында сан жасырылды!')
# m = 0

# while True:
#     m += 1
#     a = int(input('Мумкиндик #' + str(m) + ': '))

#     if a == x:
#         print('Сиз жендиниз!')
#         print('Кажет болган мумкиндик сан:', m)
#         break
#     else:
#         print('Сиз дурыс тапкан жоксыз!')
#         if a > x:
#             print('Киширек алыныз!')
#         elif a < x:
#             print('Улкенирек алыныз!')

#     print()






# from random import randint
# print('\n    Шарик с предсказаниями!')
# print('    Каждый раз шарик будет выдавать случайное предсказание.')
# print('    А так же можете задать свой вопрос и получить ответ.\n')

# print('    Режимы:\n    1) Предсказание.\n    2) Задать вопрос.')

# while True:
#     x = int(input('    Выберите режим: '))
#     print()

#     if x == 1:
#         pred = randint(1, 5)
#         if pred == 1:
#             print('    У вас будет удачный день!')
#         elif pred == 2:
#             print('    У вас будет неудачный день!')
#         elif pred == 3:
#             print('    Вы сегодня найтеде 5 000тг на улице!')
#         elif pred == 4:
#             print('    У вас сегодня украдут 5 000тг! Будьте на чеку!')
#         elif pred == 5:
#             print('    Кажется вы сегодня заболеете! Крепитесь!')
#     elif x == 2:
#         q = input('    Вопрос: ')
#         pred = randint(1, 2)
#         if pred == 1:
#             print('    Ответ на ваш вопрос: Да!')
#         elif pred == 2:
#             print('    Ответ на ваш вопрос: Нет!')
#     else:
#         print('    Вы сделали некорректный выбор!')

#     ans = input('    Продолжаем(Да/Нет)? ')
#     if ans == 'Да':
#         print()
#         continue
#     elif ans == 'Нет':
#         print('    Good Bye')
#         break









# print('\n    Консольный калькулятор')
# print('    Здесь вы сможете делать простые математические вычисления!\n')

# while True:
#     print('    -----------------------')
#     a = float(input('    Введите первое число: '))
#     c = input('    (+, -, *, /, **, //, %)\n    Введите операцию: ')
#     b = float(input('    Введите второе число: '))

#     if a == int(a):
#         a = int(a)
#     if b == int(b):
#         b = int(b)

#     print('\n    Результат:')
#     print('    ', end='')
#     if c == '*':
#         print(a, '*', b, '=', a * b)
#     elif c == '**':
#         print(a, '**', b, '=', a ** b)
#     elif c == '+':
#         print(a, '+', b, '=', a + b)
#     elif c == '-':
#         print(a, '-', b, '=', a - b)    
#     elif (c == '/' or c == '//' or c == '%') and b == 0:
#         print('Делить на ноль нельзя!')
#     elif c == '/':
#         print(a, '/', b, '=', a / b)
#     elif c == '%':
#         print(a, '%', b, '=', a % b)
#     elif c == '//':
#         print(a, '//', b, '=', a // b)


#     ans = input('    Продолжаем(Да/Нет)? ')
#     if ans == 'Да':
#         print()
#         continue
#     elif ans == 'Нет':
#         print('    Good Bye')
#         break
#     print()