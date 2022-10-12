
# while
# for ___ in

# text = "pyth0n"

# for bukva in text:
#     if bukva == "0":
#         print(bukva, 'Да')
#     else:
#         print(bukva, "Нет")

# i = 0
# while i < 5:
#     print(i)
#     i += 1
# n = 2
# for i in range(10, n-1, -1):
#     print(i)
    
# 0 1 2 3 4
# басталуы, соны, кадам
#   0       ?      1

# hour = 15
# minute = 30
# second = 45

# print(hour, minute, second, sep=":")


# print("decode", "python", end=".")
# print("school", end='-')    



# for i in range(5, 16):
#     if i == 10:
#         continue
#     print(i, end=' ')


# n = int(input())

# for i in range(1, n + 1):
#     print(i, end=' ')


# n = int(input())

# for i in range(n):
#     print("decode")


# l = int(input())
# r = int(input())

# for i in range(l, r + 1):
#     if i % 2 == 0:
#         print(i, end=' ')


# a = int(input())
# b = int(input())

# for i in range(a, b - 1, -1):
#     if i % 2 != 0:
#         print(i, end=' ')




############# уй жумысы


# a = int(input())
# b = int(input())

# if a < b:
#     for i in range(a, b + 1):
#         print(i, end=' ')
# else:
#     for i in range(a, b - 1, -1):
#         print(i, end=' ')


# a = int(input()) # 199

# a += a % 2 - 1

# b = int(input())

# for i in range(a, b - 1, -2):
#     print(i, end=' ')


# a b c d
# 2 5 0 2

# 2    3    4    5
# 2         4



# a b  c d
# 1 10 1 3

# 1   2  3   4   5  6   7   8   9  10
#   1 4 7 10


# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for i in range(a, b+1):
#     if i % d == c:
#         print(i, end=' ')


# n = int(input())
# summ = 0
# for i in range(n):
#     x = int(input())
#     summ += x

# print('Cумма:',summ)




# a = int(input()) # косындысы
# b = int(input()) # кобейтиндиси

# find = False

# for x in range(0, a + b + 1):
#     for y in range(0, a + b + 1):
#         if x + y == a and x * y == b:
#             print(x, y)
#             find = True
#             break

#     if find == True:
#         break






# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())

# for x in range(-100, 101):
#     if (a * x**3) + (b * x**2) + (c * x) + (d) == 0:
#         print(x, end=' ')