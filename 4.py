from random import randint
import time
long_list = [randint(0, 3000) for element in range(1000000)]


def timeIt(func):
    start = time.time()
    func()
    end = time.time()
    print(func.__name__, ": ", round((end-start)*1000), " ms")


def method1():
    for i in long_list:
        if i == -1:
            print("jest")
            break


def method2():
    if -1 in long_list:
        print("jest")


def method3():
    a = list(filter(lambda x: x == -1, long_list))
    if len(a) > 0:
        print("jest")


def method4():
    if next((x for x in long_list if x == -1), False):
        print("jest")


def method5():
    if long_list.count(-1):
        print("jest")


timeIt(method1)
timeIt(method2)
timeIt(method3)
timeIt(method4)
timeIt(method5)
