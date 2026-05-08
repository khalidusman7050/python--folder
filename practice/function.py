def hello():
    print("Hello, World!")
    
hello()

def add(a,b):
    return a + b
result = add(5, 3)
print(result)

def sum(num1, num2):
    print(num1 + num2)

sum(10, 20)
sum(5, 7)
sum(3, 4)
sum(1, 2)


def multiple_items(*args):
    print(args)
    print(type(args))
    
    
multiple_items("khalid",'usman')


def mult_name(**kwargs):
    print(kwargs)
    print(type(kwargs))
    
mult_name(first="khalid", last="usman")
