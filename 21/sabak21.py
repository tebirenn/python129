

#### mod 'x'

# file = open('test.txt', 'x')
# file.close()

#### mod 'r'

# file = open('test.txt', 'r')

# # v1

# # text = file.read()
# # print(text)

# # v2

# # print(file.readline())
# # print(file.readline())

# # v3

# # lines = file.readlines()
# # for i in range(len(lines)):
# #     lines[i] = lines[i].strip('\n')

# # print(lines)

# file.close()



# ### mod 'w'

# file = open('test.txt', 'w')

# file.write("file_manager")
# file.write("\npython")
# file.write("\nalan")

# file.close()


### mod 'a'

# file = open('test.txt', 'a')

# file.write("\nfile_manager")
# file.write("\npython")
# file.write("\nalan")

# file.close()




######### модуль os, shutil

# import os
# import shutil

# os.rename('folder', 'new_folder')

# # os.rename('test.txt', 'abc.txt')

# os.remove('test.txt')

# shutil.rmtree('test_folder')

# os.mkdir('folder')

# shutil.copy('abc.txt', 'abc_copy.txt')

# shutil.move('abc_copy.txt', 'folder')




# example

# file = open('example.csv', 'r')
# lines = file.readlines()
# file.close()

# res = [0, 0, 0]

# for line in lines[1:]:
#     points = line.strip('\n').split(',')

#     for i in range(len(points)):
#         res[i] += int(points[i])


# file = open('example.csv', 'a')

# file.write(',,\n')
# file.write(','.join(map(str, res)))

# file.close()





########################## cw21

# import os
# import shutil

# # Easy A

# file = open('task1.txt', 'x')
# print('Файл успешно был создан!')
# file.close()



# # Easy B

# os.remove('task1.txt')
# print('Файл успешно был удалён')


# # Easy C

# name = input()
# form = input()

# full_name = f"{name}.{form}"
# file = open(full_name, 'x')
# print(f'Файл "{full_name}" успешно создан')


# # Easy D

# full_name = input()

# try:
#     os.remove(full_name)
#     print(f'Файл "{full_name}" успешно удален')
# except:
#     print(f'Файл "{full_name}" не существует')



# # Medium A

# old_name = input()
# new_name = input()

# try:
#     os.rename(old_name, new_name)
#     print('Done')
# except:
#     print('Error')


# # Medium B

# file = open('MediumBC.txt', 'w')

# n = int(input())

# for i in range(n):
#     word = input()
#     file.write(word + ' ')

# file.close()




# # Medium C

# file = open('MediumBC.txt', 'a')

# file.write('\n')

# n = int(input())

# for i in range(n):
#     word = input()
#     file.write(word + ' ')

# file.close()


# # Hard A

# file = open('hardA.txt', 'r')

# for i in range(5):
#     print(file.readline().upper(), end='')

# file.close()






############################################# hw 21

import os
import shutil

# Easy

# def file_exist(file_name):
#     try:
#         file = open(file_name, 'r')
#         file.close()
#         return True
#     except:
#         return False

# while True:
#     file_name = input("Введите название файла: ")
#     if file_exist(file_name) == True:
#         break
#     else:
#         print("Файл не найден, попробуйте еще раз!")

# file = open(file_name, 'r')
# for i in range(5):
#     print(file.readline().strip('\n'))
# file.close()



# Medium

# file = open('ethics.txt', 'r')

# lines = file.readlines()

# print('Нечетные линий: ')
# for line in lines[::2]:
#     print(line.strip('\n'))

# print('\nЧетные линий: ')
# for line in lines[1::2]:
#     print(line.strip('\n'))

# file.close()


# Hard 

file = open('ethics.txt', 'r')
new_file = open('new_ethics.txt', 'w')

for i in range(6):
    new_file.write(file.readline())

file.close()
new_file.close()

for i in range(1, 4):
    shutil.copy('new_ethics.txt', f'new_ethics_copy{i}.txt')
    os.mkdir(f'ethics{i}')
    shutil.move(f'new_ethics_copy{i}.txt', f'ethics{i}')


os.remove('new_ethics.txt')
