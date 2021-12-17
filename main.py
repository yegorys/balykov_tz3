from math import inf


def mins(numbers):
    minnum = numbers[0]
    for l in numbers:
        if minnum > l:
            minnum = l
    return minnum


def maxs(numbers):
    maxnum = numbers[0]
    for l in numbers:
        if maxnum < l:
            maxnum=l
    return maxnum


def mul(numbers):
    proz = 1
    try:
        for l in numbers:
            proz*=l
    except OverflowError:
        proz = "error"

    return proz


def sums(numbers):
    summa = 0
    for l in numbers:
        summa = summa + l
    return summa


data = []
with open("data.txt", 'r') as file_obj:
    data = list(map(int, file_obj.read().split()))

max = maxs(data)
min = mins(data)
proiz = mul(data)
summa = sums(data)
