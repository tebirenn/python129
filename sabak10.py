



# text = 'decode'


############ index

# print(text[0])
# print(text[-1])

############ slice
# print(text[2:])
# print(text[::-1])


############ len

# a = "mac book"
# print(len(a))



############### for 

# string = "python"

# for char in string:
#     print(char)

# for i in range(len(string)):
#     print(string[i])



####### озгерис

# arr = [1, 2, 3]
# arr[0] = -5
# print(arr)

# text = "hecode"
# text[0] = "d"
# print(text)

#### обход
# text = "hecode"
# text = "d" + text[1:]
# print(text)




##########################  Форматирование

# decode.kz
# "https://www.decode.kz/mainPage/"

# domen = input()
# zone = input()


# print("https://www." + domen + "." + zone + "/mainPage/")

#1 format
# link = "https://www.{}.{}/mainPage/"
# print(link.format("decode", "kz"))
# print(link.format('google', 'com'))

#2 format
# print(f"https://www.{domen}.{zone}/mainPage/")

#3 format
# link = "https://www.%s.%s/mainPage/"
# print(link % (domen, zone))




################# methods

# text = 'decode'

# print(text.index('c'))
# print(text.find('c'))

# print(text.index('k'))
# print(text.find('k'))


# print(text.count('e'))


# text = 'hecode'
# print(text.replace('h', 'd'))


# text = 'decode'
# print(text.replace('code', 'program'))


# text = 'DeCode'
# print(text.upper())
# print(text.lower())

# print('tEMirlAn SaIROv'.capitalize())
# print('tEMirlAn SaIROv'.title())


# is
# print('ABcd'.isupper())
# print('QWE'.isupper())

# print('ABcd'.islower())
# print('qwe'.islower())

# print('123'.isdigit())
# print('14x6'.isdigit())

# print('Alan'.isalpha())
# print('Dec#de'.isalpha())

# name = input('Есимниз: ')
# print(f"Cиздин есиминиз: {name.strip()}!")




########  with list

# text = "decode school python"
# print(text.split())

# data = "8/17/2022"
# print(data.split('/'))

# time = "18:26:21"
# print(time.split(":"))


# arr = ["decode", "is", "cool"]
# print(" ".join(arr)) # "decode is cool"

# arr = ["decode", 5, False]
# print(",".join([str(el) for el in arr]))












# CW 10


# Easy A
# a = input()
# b = input()

# if a == b:
#     print('YES')
# else:
#     print('NO')

# Easy B

# a = input()
# print(a[::-1])


# Easy C

# s = input()
# a = int(input())
# b = int(input())

# print(s[a:b+1])


# Easy D

# s = input()
# c = len(s) // 2
# print(s[:c].lower() + s[c:].upper())



# Medium A

# s = input()

# for el in s:
#     if el == el.lower():
#         print(el.upper(), end='')
#     else:
#         print(el.lower(), end='')