
# import re

#   '123.123'   => ['123', '123']




# Easy A

# s = input()
# patt = r'\d+'
# print(re.sub(patt, '', s))


# Easy B

# s = input()

# print(re.split(r'[\.,\s]', s))


# Easy C

# s = input()

# if re.search(r'^(T|t)he', s):
#     print('Нашел совпадение')
# else:
#     print('Не нашел совпадение')


# Medium A

# s = input().lower()

# res = re.search("decode", s)
# if res:
#     print(res.start(), res.end())
# else:
#     print('Совпадений нет!')

# Medium B

# link = input()

# patt = r'^(http|https)://[a-z]+\.[a-z]+/?$'

# print(bool(re.search(patt, link)))


################################### hw20
import re

### Easy B

# color = input().replace(' ', '')

# rgb = re.search(r'^rgb\((\d{1,3}),(\d{1,3}),(\d{1,3})\)$', color)
# hsl = re.search(r'^hsl\((\d+),(\d+)%,(\d+)%\)$', color)

# if rgb:
#     if rgb.group(1) == rgb.group(2) == rgb.group(3) and rgb.group(1) != '0' and rgb.group(1) != '255':
#         print('YES')
#     else:
#         print('NO')
# if hsl:
#     if hsl.group(1) == hsl.group(2) == '0' and hsl.group(3) and hsl.group(3) != '0' and hsl.group(3) != '100':
#         print('YES')
#     else:
#         print('NO') 


### Medium A

# s = input()

# s = re.sub(r'\b[Aa]([a-zA-Z]+)[Aa]\b', r'!\1!', s)

# print(s)


### Medium B


# s = input()
# letter = input()

# words = re.findall(r'\b[a-zA-Z]+\b', s)
# patt = r'[' + letter.lower() + letter.upper() + ']'
# cnt = 0
# for word in words:
#     if re.search(patt, word):  # r'[eE]'
#         cnt += 1

# print(cnt)