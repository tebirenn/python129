


x = 5

arr = [123, 456, 789]

d = {
    'python': 3,
    'pip': 22,
    'decode': 5
}

def summa(a, b):
    return a+b

# Meduim A

def reversed_str(s):
    return s[::-1]


# Medium B

def abs(num):
    return num if num > 0 else -num

def sqrt(num):
    return num**0.5

def pow(num, p):
    return num**p    


# Hard A
def sum_index(arr):
    mx = max(arr)
    mn = min(arr)

    return mx + mn



if __name__ == '__main__':
    print(summa(45, 87))



