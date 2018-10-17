#  Program to implement Logic Gates
#  NOT, AND, OR, XOR, NAND, NOR

t = True
f = False

# NOT Gate
def notGate(A) :
    if A :
        return False
    else :
        return True

# AND Gate
def andGate(A, B) :
    if A == False :
        return False
    elif B == False:
        return False
    else :
        return True

# OR Gate
def orGate(A, B):
    if A:
        return True
    elif B:
        return True
    else:
        return False

# XOR Gate
def xorGate(A, B) :
    if A == B :
        return False
    else :
        return True

# NAND Gate
def nandGate(A, B) :
    return notGate(andGate(A, B))

# NOR Gate
def norGate(A, B) :
    return notGate(orGate(A, B))

# Truth table for NOT gate
def notTable():
    print ("\nNOT Gate")
    print ("A","X")
    print (t, notGate(t))
    print (f, notGate(f))

# Truth table for OR gate
def orTable():
    print ("\nOR Gate")
    print ("A","B", "X")
    print (f, f, orGate(f,f))
    print (f, t, orGate(f,t))
    print (t, f, orGate(t,f))
    print (t, t, orGate(t,t))

# Truth table for AND gate
def andTable():
    print ("\nAND Gate")
    print ("A","B", "X")
    print (f, f, andGate(f,f))
    print (f, t, andGate(f,t))
    print (t, f, andGate(t,f))
    print (t, t, andGate(t,t))
    
# Truth table for XOR gate
def xorTable():
    print ("\nXOR Gate")
    print ("A","B", "X")
    print (f, f, xorGate(f,f))
    print (f, t, xorGate(f,t))
    print (t, f, xorGate(t,f))
    print (t, t, xorGate(t,t))

# Truth table for NAND gate
def nandTable():
    print ("\nNAND Gate")
    print ("A","B","X")
    print (f, f, nandGate(f,f))
    print (f, t, nandGate(f,t))
    print (t, f, nandGate(t,f))
    print (t, t, nandGate(t,t))

# Truth table for NAND gate
def norTable():
    print ("\nNOR Gate")
    print ("A","B", "X")
    print (f, f, norGate(f,f))
    print (f, t, norGate(f,t))
    print (t, f, norGate(t,f))
    print (t, t, norGate(t,t))

# (AB + AC)
def abac(A, B, C) :
    return orGate(andGate(A,B), andGate(A,C))

# Truth table for (AB + AC) circuit
def abacTable():
    print ("\n(AB + AC) Circuit")
    print ("A","B","C","X")
    print (0,0,0,abac(0,0,0))
    print (0,0,1,abac(0,0,1))
    print (0,1,0,abac(0,1,0))
    print (0,1,1,abac(0,1,1))
    print (1,0,0,abac(1,0,0))
    print (1,0,1,abac(1,0,1))
    print (1,1,0,abac(1,1,0))
    print (1,1,1,abac(1,1,1))

# Generate truth tables
notTable()
andTable()
orTable()
xorTable()
nandTable()
norTable()
abacTable()
