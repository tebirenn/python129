


# sum min max
# sorted reversed



## sum, min, max

# d = {
#     1: 75,
#     2.5: 105
# }

# print(sum(d.values()))


## sorted reversed

# st = {'a', 'b', 'c', 'x'}
# text = 'Decode'
# sd = {
#     'physics': 82,
#     'math': 65,
#     'history': 75
# }

# print(list(reversed(text)))


# print(sorted(st, reverse=True))
# print(sorted(text, reverse=True))
# print(sorted(sd.values()))



# map

# arr = list(map(int, input().split()))
# print(arr)



# text = 'decode'

# for el in sorted(text):
#     print(el, end=' ')

# print(text)




# Medium B   cw12

# a = input().split()
# d = {}

# for el in a:
#     d[el] = a.count(el)

# for k, v in sorted(d.items()):
#     print(k, v)














#### cw 13

# Easy A

# a = [int(el) for el in input().split()]

# sm = sum(a)
# if sm > 10:
#     print('More')
# elif sm < 10:
#     print('Less')
# else:
#     print('Equal')


# Easy B

# name = input()
# zone = input()

# print(f'http://www.{name}.{zone}/')



# Easy C

# s = input()
# st = set(s)

# shift = False
# for el in s:
#     if el.isupper():
#         shift = True
#         break

# print(len(st) + int(shift))



# Easy D

# s = input().split()
# d = {}

# for el in s:
#     d[el] = len(el)

# for k, v in d.items():
#     print(k, v, sep='-')




# Meduim A

# a = input().split()

# print(*a[1::2])



## Medium B

# alp = 'abcdefghijklmnopqrstuvwxyz'

# s = input().lower()
# l = len(s)

# if s == alp[:l]:
#     print('good')
# else:
#     print('cringe')





# d = {}
# n = int(input())

# for i in range(n):
#     name, grade = input().split()
#     grade = int(grade)

#     if name not in d.keys():
#         d[name] = grade
#     elif grade > d[name]:
#         d[name] = grade

# for name, grade in sorted(d.items()):
#     print(name, grade, sep=": ")








##################### hw 13


# Medium B

# s = input()

# f = s.find('h')
# l = s.rfind('h')

# print(s[:f] + s[l:f-1:-1] + s[l + 1:])


# Hard B

# cpp, python = set(), set()
# n, m = int(input()), int(input())

# for i in range(n):
#     name = input()
#     cpp.add(name)

# for i in range(m):
#     name = input()
#     python.add(name)


# ans = cpp.symmetric_difference(python)

# print(len(ans))