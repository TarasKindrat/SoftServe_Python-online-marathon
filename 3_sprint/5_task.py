"""
Create decorator logger. The decorator should print to the console information about
function's name and all its arguments separated with ',' for the function decorated with logger.

Create function concat with any numbers of any arguments which concatenates arguments and apply logger
decorator for this function.

For example
print(concat(2, 3)) display
Executing of function concat with arguments 2, 3...
23

print(concat('hello', 2)) display
Executing of function concat with arguments hello, 2...
hello2

print(concat (first = 'one', second = 'two')) display
Executing of function concat with arguments one, two
onetwo



"""


def logger(func):
    # inner function like in closures
    def wrapper(*args, **kwargs):
        args_items = ''
        kwargs_items = ''
        if len(args) >= 2:
            for i in args:
                args_items += ', '+str(i)
        if len(args) == 1:
            args_items = args[0]
           # print(args_items)
        if len(kwargs) > 0:
            for item, value in kwargs.items():
                kwargs_items += ', ' + str(value)
            #print(kwargs_items)

        if func(*args, **kwargs) is None:
            sentence = f"Executing of function {func.__name__} with arguments " \
                       f"{str(args_items).lstrip(',')}{kwargs_items}..."
            print(sentence)
        elif func(*args, **kwargs) is not None and len(args) > 0:
            sentence = f"Executing of function {func.__name__} with arguments " \
                       f"{str(args_items).lstrip(',')}{kwargs_items.lstrip(',')}...\n{func(*args, **kwargs)}"

        else:
            sentence = f"Executing of function {func.__name__} with arguments " \
                       f"{kwargs_items.lstrip(',')}...\n"
            print(sentence)
        return sentence
    return wrapper


@logger
def concat(*args, **kwargs):
    list1 = [i for i in args]
    list2 = [str(value) for item, value in kwargs.items()]
    return ''.join(map(str, list1)) + ''.join(map(str, list2))


# type your code here

@logger
def sum(a, b):
    return a + b


@logger
def print_arg(arg):
    print(arg)


print(concat(1))
print(concat('first string', second = 2, third = 'second string'))
print(concat('first string', {'first kwarg':0, 'second kwarg': 'second kwarg'}))
print(sum(2,3))
print_arg(2)
dict_args = {'first kwarg': 0, 'second kwarg': 'second kwarg'}
concat(**dict_args)


# def fn(g):
#    pass
# fn(4)
# print(fn.__dict__)
"""
 	Test 	Expected 	Got 	
	

print(concat(1))

	

Executing of function concat with arguments 1...
1

	

Executing of function concat with arguments 1...
0
None

	
	

print(concat('first string', second = 2, third = 'second string'))

	

Executing of function concat with arguments first string, 2, second string...
first string2second string

	

Executing of function concat with arguments first stringsecond,2third,second string...
0
None

	
	

print(concat('first string', {'first kwarg' :0, 'second kwarg': 'second kwarg'}))

	

Executing of function concat with arguments first string, {'first kwarg': 0, 'second kwarg': 'second kwarg'}...
first string{'first kwarg': 0, 'second kwarg': 'second kwarg'}

	

Executing of function concat with arguments first string{'first kwarg': 0, 'second kwarg': 'second kwarg'}...
0
None

	
	

print(sum(2,3))

	

Executing of function sum with arguments 2, 3...
5

	

Executing of function sum with arguments 2
None

	
	

dict_args={'first kwarg' :0, 'second kwarg': 'second kwarg'}
concat(**dict_args)

	

Executing of function concat with arguments 0, second kwarg...

	

Executing of function concat with arguments first kwarg,0second kwarg,second kwarg...
0

	
	

print_arg(2)

	

2
Executing of function print_arg with arguments 2...

	

Executing of function print_arg with arguments 2
1

	
"""
