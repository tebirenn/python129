


# def test():
#     name = 'Alan'
#     print('Бул функция', name)

#     print('Функиянын соны\n')


# test()
# test()
# test()
# print('Программа соны') 




# def greeting(name):
#     print(f'Салем {name}!')

# greeting('Алан')
# greeting("Ерлан")

# x = 'Абай'
# greeting(x)


# def greeting(name, age):
#     print(f'Салем {name}!')
#     print(f'Сиз {age} жастасыз!\n')

# greeting("Ерлан", 15)

# x = 'Абай'
# n = 20
# greeting(x, n)





# x = max(4, 8, 12, 5, 42)
# print(x)


# def my_max(a, b): # v1
#     if a > b:
#         print(a)
#     else:
#         print(b)

# my_max(9, 6)


# def my_max(a, b): # v2
#     if a > b:
#         return a

#     return b

# print(my_max(9, 3, 12))

# print(my_max(my_max(4, 6), 12))  # 4 6 12


# def my_max(*args): # v3
#     mx = args[0]

#     for el in args:
#         if el > mx:
#             mx = el

#     return mx

# ans = my_max(6, 8, 13, 2, 8, 77)
# print(ans)







# def one_to_n(number):
#     ans = []

#     for i in range(1, number + 1):
#         ans.append(i)

#     return ans



# print(one_to_n(5))
# print(one_to_n(5)[2])
# print(one_to_n(10).pop())





# def print_list(arr, i = 0, j = -1):
#     if j == -1:
#         print(*arr[i:])
#     else:
#         print(*arr[i:j+1])


# x = [4, 7, 8, 9, 4, 2]

# print_list(x, 2, 4)









# x = 5

# def test(): 
#     global x
#     number = 20
#     x *= 3

# test()
# print(x)



# def has_negative(arr):
#     for el in arr:
#         if el < 0:
#             return True

#     return False


# x = [int(el) for el in input().split()]
# print(has_negative(x))




################################## Cw 15

# Easy A

# def abc():
#     print('Hi there, Im using WhatsApp')

# abc()


# Easy B

# def show_age(n):
#     print(f"I'm {n} years old.")


# age = int(input())
# show_age(age)



# Easy C

# def check(n):
#     if n % 2 == 0:
#         print('Even')
#     else:
#         print('Odd')


# number = int(input())
# check(number)



# Easy D

# def easy_d(n):
#     ans = 0
#     for i in range(1, n + 1):
#         ans += i

#     return ans


# n = int(input())

# print(easy_d(n))



# Medium A

# def have_digit(string):
#     for el in string:
#         if el.isdigit():
#             return 'cool'

#     return 'hot'


# s = input()
# print(have_digit(s))


# Medium B

# def is_prime(n):
#     if n < 2:
#         return False

#     for i in range(2, n):
#         if n % i == 0:
#             return False
    
#     return True



######################### hw 15
# sort жане sorted
# arr = ['abc', '12345', 'abc', 'pythonlang', 'decode']

# arr.sort(key=len, reverse=True)

# print(arr)

# arr = ['abc', '12345', 'abc', 'py', 'decode']

# print(min(arr, key=len))
# print(max(arr, key=len))


# Hard A

# def sum_of_digit(num):
#     ans = 0
#     while num != 0:
#         ans += num % 10
#         num //= 10

#     return ans

# arr = [int(el) for el in input().split()]

# print(*sorted(arr, key=sum_of_digit))



# Hard B

# def my_reverse(arr):
#     return arr[::-1]

# arr = input().split()

# print(*my_reverse(arr))