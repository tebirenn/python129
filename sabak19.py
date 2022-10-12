# import re

# s = input()
# pattern = r'^decode'

# print(bool(re.search(pattern, s)))


# s = input()
# pattern = r'decode$'

# print(bool(re.search(pattern, s)))


# s = input()
# pattern = r'\.(jpg|png|jpeg|svg|webp)$'

# print(bool(re.search(pattern, s)))


# s = input()
# pattern = r'^[a-zA-Z]+$'

# print(bool(re.search(pattern, s)))


# s = input()
# pattern = r'[!@#\$%\^&\*\-]'   #   !@#$%^&*-
# print(bool(re.search(pattern, s)))

# s = input()
# pattern = r'^[^!@#\$%\^&\*\-]+$'   # []  [^]
# print(bool(re.search(pattern, s)))


# s = input()
# pattern = r'^[0-9]+\$?$'
# print(bool(re.search(pattern, s)))



# s = input()
# pattern = r'^[0-9]+\$*$'
# print(bool(re.search(pattern, s)))


#   ?     [0, 1]
#   +     [1, inf)
#   *     [0, inf)


# s = input()
# pattern = r'^[0-9]{3}$'
# print(bool(re.search(pattern, s)))



# s = input()
# pattern = r'^[0-9]{2,4}$'
# print(bool(re.search(pattern, s)))



# s = input()
# pattern = r'([0-9]{1,2}/[0-9]{1,2})/([0-9]{1,4})'
# res = re.search(pattern, s)

# print(res.group(0))
# print(res.group(1))
# print(res.group(2))


# s = input()
# pattern = r'^\w$'
# print(bool(re.search(pattern, s)))





# s = input()
# pattern = r'\d'
# print(bool(re.match(pattern, s)))


# pattern = r'[0-9]'
# pattern = re.compile('[0-9]')


# s = input()

# print(re.findall(r'\b[0-9]{2}\b', s))


# s = input()

# print(re.split(r'\d', s))



# s = 'HelloWorld'

# print(re.sub(r'[A-Z]', r'_', s))


# s = 'HelloWorld'

# print(re.sub(r'([A-Z])', r'\1', s))


###################### cw 19


# Easy A

# s = input()

# print(bool(re.search(r'[0-9]', s)))


# Easy B

# s = input()

# if re.search(r'^[a-zA-Z0-9]+$', s):
#     print('Нашел совпадение!')
# else:
#     print('Не нашел совпадение')



# Easy C

# s = input()

# if re.search(r'[A-Z][a-z]+', s):
#     print('Нашел совпадение!')
# else:
#     print('Не нашел совпадение')



# Medium A

# s = input()

# print(bool(re.search(r'cool$', s)))


# Medium B

# s = input()

# if re.search(r'^a.+b$', s):
#     print('Нашел совпадение!')
# else:
#     print('Не нашел совпадение')

# Medium C

# ip = input()

# pattern = r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$'

# if re.search(pattern, ip):
#     print('IP')
# else:
#     print('Something else')


# Hard A

# number = input()

# pattern = r'^(77|87)\d{9}$'

# if re.search(pattern, number):
#     print('Call me maybe')
# else:
#     print('Something else')



########################### hw 19

import re

# Easy B
# s = input()
# pattern = r'\b[AEOIUaeoiu][A-Za-z]+\b'

# print(re.findall(pattern, s))


# Medium B

# s = input()

# pattern = r'[0-9]+'

# res = re.search(pattern, s)

# print(res.group(0))
# print('Индекс:', res.start())


# Hard A

# s = input()

# pattern = r'\b[A-Za-z]{5}\b'

# print(re.findall(pattern, s))


# Hard B

# s = input()

# s = re.sub(r'([A-Z])', r'_\1', s)[1:].lower()

# print(s)



