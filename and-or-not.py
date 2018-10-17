
# IMPLEMENTING AND, OR , NOT FUNCTIONS IN PYTHON

def myAnd(a, b):
    if a:
        if b:
            return True
        else:
            return False
    else:
        return False


def myOr(a, b):
    if a:
        return True
    elif b:
        return True
    else:
        return False


def myNot(a):
    if a:
        return False
    else:
        return True

