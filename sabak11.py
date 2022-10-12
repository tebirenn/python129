

# коллекциялар

#1 озгеру

# a = ['a', 'b', 'c']
# a[0] = 'z'
# print(a)


# s = "text"
# s[2] = 's'
# print(s)




# {}

# a1 = {}
# print(type(a1))

# a2 = {4, 5, 6}
# print(type(a2))

# st = set()    # пустой cет

# st = {1, 1, 1, 2, 2, 2}
# print(st)


# st = {'a', 'b', 'c', 'd'}

# print(st[0]) # ошибка: индекс жок

# print(st)



# list1 = [1, 2, 3, 1, 2, 2]
# str1 = "test"

# print(set(list1))
# print(set(str1))



# s = {8, 1, 8, 10, 1}

# print(len(s))
# print(s)


# s = {8, 1, 8, 10, 1}
# for el in s:
#     print(el)


# in,   not in

# arr = [4, 5, 6, 7, 8, 1, 2]

# print(7 in arr)


# st = {'a', 't', 'z', 'y'}

# print('x' in st)  # бар ма?
# print('x' not in st) # жок па?



############### set   input

# s1 = set(map(int, input().split()))
# print(s1)

# s2 = {int(el) for el in input().split()}
# print(s2)

# s3 = set(input().split())
# print(s3)


######## set методтары

# s = set()

# s.add('a')   # .add() - бир элемент косу
# s.add('z')
# s.add(5)

# print(s)




# s = {1, 7, 8}
# newset = {'a', 'b', 'c'}

# s.update(newset) # екинши сет элементтерын биринши сетке косып жибереди

# print(s)



# s = {'a', 'b', 'c', 'd'}

# el = s.pop()   # кездейсок бир элементты сеттен шыгару
# print(el)

# print(s)




# s = {'a', 'b', 'c', 'd'}

# s.remove('a')    # Элементты мани бойынша жою
# s.discard('a')   # Элементты мани бойынша жою

# s.remove('z')  # Ошибка, жою керек элементты таппаганда
# s.discard('z')   # Жою керек элементты таппаган жагдайда, унсыз калады

# print(s)





# user = {'alan', 'dias', 'erlan'}
# client = {'qairat', 'bauka', 'dias'}

# print(user.union(client))  # {'bauka', 'dias', 'qairat', 'erlan', 'alan'}

# print(user.intersection(client))  # {'dias'}

# print(user.difference(client))  # {'erlan', 'alan'}
# print(client.difference(user))  # {'qairat', 'bauka'}

# print(user.symmetric_difference(client))  # {'qairat', 'bauka', 'alan', 'erlan'}





# user = {'alan', 'dias', 'erlan', 'qairat'}
# client = {'qairat', 'dias'}

# print(client.issubset(user))
# print(user.issuperset(client))








################ cw 11


# Easy A

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# set1.update(set2)
# print(set1)

# print(set1.union(set2))



# Easy B

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# print(set1.intersection(set2))



# Easy C

set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}

# print(set1.difference(set2))
# print(set2.difference(set1))



# Easy D

# s = set(input().split())
# print(s)




# Medium A

# s = input()

# ans = set(s)
# print(len(ans))
# print(*ans)



# Meduim B

# n = int(input())
# names = set(input().split())

# print(n - len(names))



# Medium C

# n = int(input())
# ans = set()

# while n != 0:
#     ans.add(n % 10)
#     n //= 10

# print(*ans)






# Hard A

# s = input()
# ans = set()

# for el in s:
#     if el.isalpha():
#         ans.add(el)

# print(*ans)





# Hard B

# lesson = set()
# listt = set()

# n = int(input())
# for i in range(n):
#     name = input()
#     lesson.add(name)

# m = int(input())
# for i in range(m):
#     name = input()
#     listt.add(name)

# print('\nABSENCE:')
# print(*listt.difference(lesson))

# print('\nIMPOSTER:')
# print(*lesson.difference(listt))








######### hw11

# Easy A

# st = {int(i) for i in input().split()}
# ans = set()

# for el in st:
#     if el % 3 != 0:
#         ans.add(el)

# print(ans)


# Medium A

# st = {int(el) for el in input().split()}

# print('Максимальный элемент -', max(st))
# print('Минимальный элемент -', min(st))


# Medium B
# st = {int(el) for el in input().split() # 1 2 3

# print(len(st))



# Hard A

# st = set()
# n = int(input())

# for i in range(n):
#     x = input().split()

#     for el in x:
#         st.add(el)

# print(len(st))