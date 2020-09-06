"""
Create function with name outer(name). This function should return inner function with name inner.
This inner function prints message Hello, <name>!
For example
tom = outer("tom")
tom() -> Hello, tom!
"""

#def outer(name):
#    def inner(name):
#        print(f"Hello, {name}!")
#        return None
#    return inner(name)

#print(outer("Tom"))
#tom = outer("tom")
#print(tom)
#print((outer("Tom")()))

def outer(name):
    inner = lambda: print(f"Hello, {name}!")
    return inner

outer("Tom")()