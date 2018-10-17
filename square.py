
# BAD way to use functions,
# by reassigning global variables in the function

def squareGlobal():
    global result
    result = num**2


# GOOD way to use functions,
# by passing in  parameters and returning a value

def squareLocal(x):
    return x**2



    
