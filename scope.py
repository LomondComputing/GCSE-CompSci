# TEST FUNCTIONS TO ILLUSTRATE SCOPE RULES IN PYTHON

def test1(a):
    a = a + x  # x must be global as not assigned in this function
    print(a)


def test2(a):
    x = 9    # x is now local as assigned in this function
    a = a + x  
    print(a, x)


def test3(a):
    a = a + x    # x is local but has not been assigned here
    x = 9    
    print(a, x)


def test4(a):
    global x    # this ensures it is the global version of x that is used
    x = 9
    a = a + x           
    print(a, x)
