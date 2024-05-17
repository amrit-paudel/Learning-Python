
# nonlocal keyword is used to work with variables inside nested functions

def counter(start):
    
    def inc(step = 1):
        nonlocal start
        start = start + step
        print( start )
    return inc # here we are returning the inner function inc() from the function counter()
temp = counter(10)
temp(2) # 12
temp(5) #17



# global variable is always connected from the global scope
# nonlocal variable is always connected from the nearest namespace

temp = 100
temp1 = 100
def outer():
    temp = 200
    temp1 = 50
    def inner():
        global temp
        nonlocal temp1
        print( f"Global variable : {temp}" ) # 100
        print( f"Non local variable: {temp1} " )
    return inner
temp2 = outer()
temp2()


