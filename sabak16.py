

# def rec():
#     print('decode', end=' ')
#     rec()


# rec()



# def one_to_n(num, i = 1):
#     print(i, end=' ')

#     if i == num:
#         return
#     else:
#         one_to_n(num, i + 1)

# n = int(input())
# one_to_n(n)



# def reverse_print(arr, i = -1):
#     print(arr[i], end=' ')

#     if i * (-1) == len(arr):
#         return
#     else:
#         reverse_print(arr, i - 1)

# arr = input().split()
# reverse_print(arr)


# def one_to_n(num): # 4
#     if num == 1:
#         return 1
#     else:
#         return one_to_n(num - 1) + num

# num = int(input())
# print(one_to_n(num))


# s(4) = s(3) + 4 
# s(3) = s(2) + 3
# s(2) = s(1) + 2
# s(1) = 1




# def factorial(num):
#     if num == 0 or num == 1:
#         return 1
#     else:
#         return factorial(num - 1) * num

# num = int(input())
# print(factorial(num))


# fact(4) = fact(3) * 4
# fact(3) = 1 * 2 * 3 
# fact(2) = 1 * 2
# fact(1) = 1
# fact(0) = 1




# def sum_of_array(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
#     else:
#         return arr[0] + sum_of_array(arr[1:])

# arr = [7, 8, 10, 20]
# arr = [15]
# arr = []
# print(sum_of_array(arr))

# s([7, 8, 10, 20]) == 7 + s([8, 10, 20])
# s([8, 10, 20]) == 8 + s([10, 20])
# s([10, 20]) == 10 + s([20])
# s([20]) == 20




############ cw 16

# Easy D

# def akerman(m, n):
#     if m == 0:
#         return n + 1
#     elif m > 0 and n == 0:
#         return akerman(m - 1, 1)
#     elif m > 0 and n > 0:
#         return akerman(m - 1, akerman(m, n - 1))

# m = int(input())
# n = int(input())

# print(akerman(m, n))



# # Medium A

# def sum_of_digits(num):
#     if num == 0:
#         return 0
    
#     return num % 10 + sum_of_digits(num // 10)

# num = int(input())
# print(sum_of_digits(num))

# # s(4567) == 7 + s(456)


# Medium B

# def prod(arr, i = 0, ans = 1):
#     if len(arr) == 0:
#         return 0
#     if i == len(arr):
#         return ans

#     ans *= arr[i]
#     return prod(arr, i + 1, ans)

# def prod(arr):
#     if len(arr) == 0:
#         return 0
#     elif len(arr) == 1:
#         return arr[0]
    
#     return arr[0] * prod(arr[1:])

# arr = [int(el) for el in input().split()]
# print(prod(arr))



# Medium C

# def is_power_of_two(num):
#     if num == 1:
#         print('YES')
#         return
#     elif num < 1:
#         print('NO')
#         return
    
#     is_power_of_two(num / 2)
    

# n = int(input())
# is_power_of_two(n)

# def is_power_of_two(num):
#     if num == 1:
#         return True
#     elif num < 1:
#         return False
    
#     return is_power_of_two(num / 2)


# n = int(input())
# if is_power_of_two(n):
#     print('YES')
# else:
#     print('NO')






################### hw 16


# Hard

#         0     3       2
# def func(num, i = 1, cnt = 0):  # консоль: 1 2 2 3 3
#     if num == 0:
#         return
#     elif i == cnt:
#         func(num, i + 1, 0)
#     else:
#         print(i, end=' ')
#         func(num - 1, i, cnt + 1)

# n = int(input())
# func(n)