#!/usr/bin/env python3

def print_fibonacci(length):
    if length == 0:
        print([])
        return
    fibList = [0]
    fibNum = 1
    for i in range(length-1):
        fibList.append(fibNum)
        fibNum = fibList[i] + fibNum
    print(fibList)

print_fibonacci(9)