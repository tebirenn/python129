



# name1 = 'Alan'
# name2 = 'Erlan'
# name3 = 'Almira'

# #индекс    0        1         2
# names = ['Alan', 'Erlan', 'Almira']
# #         -3       -2        -1

# length - узындык
# print(len(names))

# numbers = [7, 4, 5, 8, 6, 13, 15, 14]

# print(numbers[-1])

# print(names[2])
# print(names[-1])







# #индекс    0        1         2        3        4        5
# names = ['Alan', 'Erlan', 'Almira', 'Erkin', 'Nurtay', 'Dias']
# #          -6       -5       -4        -3       -2        -1


# Кателиктер
# print(names[6])
# print(names[-7])


# Озгерис
# names[0] = 'Abay'
# names[5] = 159
# print(names)



# for i in range(len(names)):
#     print(names[i])


# for el in names:
#     print(el)





# slice - срез

#индекс    0        1         2        3        4        5
# names = ['Alan', 'Erlan', 'Almira', 'Erkin', 'Nurtay', 'Dias']
#          -6       -5       -4        -3       -2       -1

# print(names[1:4])

# print(names[2:5:2])

# print(names[4:0:-1])

# print(names[::-1]) # Керисинше карастыру

# [бастау:токтау:кадам]




# Тизимге колданылатын операциялар

# print('abc' * 3) # "abcabcabc"
# print([1, 2, 3] * 3) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

# print('abc' + 'def') # 'abcdef'
# print([1, 2, 3] + [7, 8, 9]) # [1, 2, 3, 7, 8, 9]





# Тизимди консольдан енгизу

# split() - текстти пробел аркылы болед, боликтерди тизимге толтырады
# arr = input().split() # тексттер тизимин енгизу
# print(arr)

# 1 вариант
# arr = [int(el) for el in input().split()] # cандар тизимин енгизу

# 2 вариант
# arr = input().split()
# for i in range(len(arr)):
#     arr[i] = int(arr[i])

# print(arr)




# list() - аудармашы

# arr1 = []
# arr2 = list() # Бос тизим

# print(arr1, arr2)



# map() - тизимнин букил элементтерин бир типке аударады
# arr = list(map(int, input().split()))
# print(arr)

# ["2", 2, 2.8]
# # int
# [2, 2, 2]




# Тизимнин методтары

# arr1 = [1, 2, 3, 4]
# arr2 = [7, 8, 9]

# arr1.append(5) # cонынан бир элемент косу
# arr2.append(10)

# arr1.insert(2, 5) # (кай жерге косу, кандай элемент косу керек)

# arr1.extend([5, 6, 7]) # баска тизим элементтерин, тизимге косу



# names = ['Alan', 'Erlan', 'Almira', 'Erkin', 'Nurtay', 'Dias']
# names.pop(2) # индекс аркылы жою
# names.remove('Almira') # Элементтин мани бойынша жою
# print(names)



# a = [0, 8, 9]
# b = a.copy() # коширмесин жасау

# a[0] = 7

# print(b)



# a = [7, 8, 9]
# a.clear()
# print(a)


# a = [4, 7, 5, 1, 4, 6, 15, 4, 7, 4]
# print(a.count(7)) # берилген элементтин тизимде неше рет кайталануы



# a = ['x', 'y', 'z', 'k', 'g']

# print(a[2]) # индекс -> элемент
# print(a.index('z'))  # элемент -> индекс


# a = [4, 7, 5, 3, 1, 0, -5, 8]

# a.sort()
# a.reverse()

# print(a)













# Easy A

# a = list()
# for i in range(3):
#     x = input()
#     a.append(x)
# print(a)



# Easy B

# arr = [int(el) for el in input().split()]
# print(arr)


# Easy C
# arr = [int(el) for el in input().split()]

# if len(arr) == 1:
#     print(arr[0])
# else:
#     print(arr[0], arr[-1])


# Easy D

# arr = [int(el) for el in input().split()]
# summ = 0

# for el in arr:
#     summ += el

# print(summ)









# HW 9

# Easy A

# n = int(input())
# arr = input().split()
# print(arr)


# Easy B

# arr = [int(el) for el in input().split()]
# for el in arr:
#     if el % 2 == 1:
#         print(el, end=' ')




# Meduim A

# arr = [int(el) for el in input().split()]

# maxx = arr[0]
# for el in arr:
#     if el > maxx:
#         maxx = el

# print(maxx, arr.index(maxx))



# Meduim B

# arr = [int(el) for el in input().split()]
# x = int(input())

# print(arr.count(x))



# Hard A


# arr = [int(el) for el in input().split()]

# maxx = arr[0] # 7
# minn = arr[0] # 1

# for el in arr:
#     if el > maxx:
#         maxx = el
#     if el < minn:
#         minn = el

# i_max = arr.index(maxx)
# i_min = arr.index(minn)

# arr[i_max], arr[i_min] = arr[i_min], arr[i_max]

# print(arr)





# Hard B

# arr = [int(el) for el in input().split()]
# pair = 0

# for i in range(len(arr)):
#     for j in range(i + 1, len(arr)):
#         if arr[i] == arr[j]:
#             pair += 1


# print(pair)