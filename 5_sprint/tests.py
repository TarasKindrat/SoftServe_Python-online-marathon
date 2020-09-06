def foo():
    try:
        return 1
    finally:
        return 2

k = foo()
print(k)

print("hello" + str(2) + "hh")

def f2():
    try:
        if '1'!=1:
            raise ("someer")
        else:
            print("noEr")
    except "someer":
        print("")


print('1'==1)