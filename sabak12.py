

#key    -1      2.5     'abc'    True     False
#        4       6        4       15       156


# d1 = {}
# d2 = dict()

# print(type(d1), type(d2))

# d1 = {
#     -1: 4, 
#     2.5: 6, 
#     'abc': 4,
#     True: 15, 
#     False: 156
# }

# d1[5] = False

# print(d1)

# d = dict(abc=123, qwe='decode')
# print(d)

# print(d1)
# print(type(d1))

# print(d1['abc'])

# d1['abc'] = '123'    # егер key бар болса, элемент озгереди
# d1['qwe'] = 'decode'  # егер key жок болса, элемент пайда болады

# print(d1)





###########  Dict метод


d = {
    -1: 789, 
    2.5: 6, 
    'abc': 4,
    True: 15, 
    False: 156
}


# print(d['abc'])
# print(d.get('abc'))

# print(d['qwe'])
# print(d.get('qwe'))

# if d.get('qwe') == None:
#     print('Сиз жазган килт жок!')

d = {
    -1: 789, 
    2.5: 6, 
    'abc': 4,
    True: 15, 
    False: 156
}

# print(d.popitem())  # Сонгы параны жою

# print(d.pop(2.5)) # key аркылы параны жою

# print(d)



d = {
    -1: 789, 
    2.5: 6, 
    'abc': 4,
}

# d.update({10: 100, 20: 200}) # баска бир dict параларын косу




# lst = [1, 2, 3, 4]
# s = 'decode'
# d = dict.fromkeys(lst, 0)

# print(d)




# lst = [1, 2, 3, 4]
# s = 'abcd'
# d = dict(zip(s, lst))

# print(d)



# d = {
#     -1: 789, 
#     2.5: 6, 
#     'abc': 4,
# }

# print(d.values())
# print(d.keys())

# print(d.items())

# for v in d.values():
#     print(v)

# for k in d.keys():
#     print(k)

# for k, v in d.items():
#     print(k, v)


# d.setdefault('qwe', 5)

# print(d)




############ tuple

#    0  1     2       3     4
# a = (7, 5, 'decode', False, 5)
#    -5  -4   -3      -2     -1

# print(a[2])

# print(a[1:])

# print(a.index('decode'))
# print(a.count(5))







# d = {
#     True: 123,
#     0: 'abc'
# }

# d[1] = 456
# d[False] = 'def'

# print(d)





######################### input

# n = int(input())
# d = {}

# for i in range(n):
#     k, v = input().split()

#     d[k] = v


# print(d)




###########   cw 12

# Easy A

# keys = ['ten', 'twenty', 'thirty']
# values = [10, 20, 30]

# d = dict(zip(keys, values))

# print(d)



# Easy B

# sampleDict={
#     "class":{
#         "student":{
#             "name":"Mike",
#             "marks":{
#                 "physics":70,
#                 "history":80
#             }
#         }
#     }
# }

# print(sampleDict['class']['student']['marks']['history'])




# Easy C

# sd = {
#     'physics': 82,
#     'math': 65,
#     'history': 75
# }

# m = min(sd.values())

# for k, v in sd.items():
#     if v == m:
#         print(k)


# Easy D

# info = {
#     'name': "Aidana",
#     'grades': [96, 78, 67, 73, 90]
# }

# x = info['grades']

# print(sum(x) / len(x))





# Medium A
# d = {}
# n = int(input())

# for i in range(n):
#     name, grade = input().split()
#     d[name] = grade


# print('name | grade')
# for k, v in d.items():
#     print(k, v, sep=': ')


# Medium B

# a = input().split()
# d = {}

# for el in a:
#     d[el] = a.count(el)

# for k, v in d.items():
#     print(k, v)





# Medium C

# n = int(input())
# d = {}

# while n != 0:
#     last = n % 10

#     if last not in d.keys():
#         d[last] = 0

#     d[last] += 1

#     n //= 10

# for k, v in d.items():
#     print(k, v)




#### Hard B

# acc = {}
# n = int(input())

# for i in range(n):
#     login, passw = input().split()
#     acc[login] = passw


# auth = {}
# m = int(input())

# for i in range(m):
#     login, passw = input().split()
#     auth[login] = passw


# for login, passw in auth.items():
#     if login not in acc.keys():
#         print('user not defined')
#     elif passw != acc[login]:
#         print('wrong password')
#     else:
#         print('welcome')





######### hw12

#### Easy A
# a, b = map(int, input().split())



#### Easy B

# d = {
#     "OOP": [77,88,99,66],
#     "ICT": [100,98,99,96]
# }

# for key in d.keys():
#     for el in d[key]:
#         print(key, el, sep=' : ')


####  Medium A

# words = input().split()
# d = {}

# for word in words:
#     if word not in d.keys():
#         print(0, end=' ')
#         d[word] = 1
#     else:
#         print(d[word], end=' ')
#         d[word] += 1
