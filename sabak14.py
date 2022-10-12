

arr = [
    [1, 2, 3], 
    [4, 5, 6], 
    [7, 8, 9]
]

# print(arr[2][0])
# print(len(arr))

########### консольга шыгару
# print(*arr, sep='\n')  # v1

# for row in arr:  # v2
#     print(*row)


########### итерация

# for row in arr:
#     for el in row:
#         print(el**2, end=' ')
    
#     print()


# for i in range(len(arr)):
#     # print(arr[i])

#     for j in range(len(arr[i])):
#         print(arr[i][j] * 2, end=' ')
    
#     print()


######## Сумма
# ans = 0

# for row in arr:
#     ans += sum(row)

# print(ans)



######### генерация

####### v1
# arr = []

# for i in range(3):
#     arr.append([0] * 5)

####### v2

# arr = [[0] * 5 for i in range(3)]

# arr[1][1] = 5

# for row in arr:
#     print(*row)




########## input

# n, m = map(int, input().split()) # [2, 3]


########## v1
# arr = []

# for i in range(n):
#     x = [int(el) for el in input().split()]
#     arr.append(x[:m])


########## v2
# arr = [0] * n

# for i in range(n):
#     arr[i] = [int(el) for el in input().split()][:m]

# print('Результат: ')
# for row in arr:
#     print(*row)



# ######## практика

# n = int(input())

# arr = [['x'] * n for i in range(n)]

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if i == j:
#             arr[i][j] = 1
#         elif i > j:
#             arr[i][j] = 2
#         elif i < j:
#             arr[i][j] = 0

# for row in arr:
#     print(*row)



################## Cw 14

## Easy B

# arr = []

# for i in range(2):
#     x = [int(el) for el in input().split()]
#     arr.append(x)

# print(arr)


## Easy C

# n = int(input())
# arr = []
# cnt = 0

# for i in range(n):
#     x = [int(el) for el in input().split()][:n]
#     arr.append(x)

# for row in arr:
#     for el in row:
#         if el < 0:
#             cnt += 1

# print(cnt)


## Easy D

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     x = [int(el) for el in input().split()][:m]
#     arr.append(x)

# for row in arr:
#     print(*row[::-1])




## Medium A

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     x = [int(el) for el in input().split()][:m]
#     arr.append(x)

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if (i + j) % 2 == 0:
#             arr[i][j] += 1
#         else:
#             arr[i][j] -= 1

# for row in arr:
#     print(*row)



## Medium B

# n, m = map(int, input().split())
# arr = []
# for i in range(n):
#     x = [int(el) for el in input().split()][:m]
#     arr.append(x)

# mx = max(arr[0])
# for row in arr:
#     max_of_row = max(row)
#     if max_of_row > mx:
#         mx = max_of_row

# for i in range(len(arr)):
#     for j in range(len(arr[i])):
#         if arr[i][j] == mx:
#             print(i, ':', j)



########### Hw 14


# Medium A

# n, m = map(int, input().split())

# arr = []

# for i in range(n):
#     x = [int(el) for el in input().split()]
#     arr.append(x[:m])

# print()

# for row in arr[::-1]:
#     print(*row[::-1])





# Hard 

# n = int(input())

# arr = [['.'] * n for i in range(n)]

# for j in range(n):
#     arr[n//2][j] = '*'

# for i in range(n):
#     arr[i][n//2] = '*'

# for i in range(n):
#     arr[i][i] = '*'

# for i in range(n):
#     arr[i][n - i - 1] = '*'

# for row in arr:
#     print(*row)