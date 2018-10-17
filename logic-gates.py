#  Program to implement Logic Gates
#  NOT, AND, OR, XOR, NAND, NOR

# NOT Gate
def notGate(A) :
    if A == 0 :
        return 1
    else :
        return 0

# AND Gate
def andGate(A, B) :
    if A == 0 :
        return 0
    else :
        if B == 0 :
            return 0
        else :
            return 1

# OR Gate
def orGate(A, B) :
    if A == 0 :
        if B == 0 :
            return 0
        else :
            return 1
    else :
        return 1

# XOR Gate
def xorGate(A, B) :
    if A == B :
        return 0
    else :
        return 1

# NAND Gate
def nandGate(A, B) :
    return notGate(andGate(A, B))

# NOR Gate
def norGate(A, B) :
    return notGate(orGate(A, B))


# Truth table for NOT gate
print "NOT Gate"
print "A","X"
print 0, notGate(0)
print 1, notGate(1)

# Truth table for OR gate
print "OR Gate"
print "A","B", "X"
print 0, 0, orGate(0,0)
print 0, 1, orGate(0,1)
print 1, 0, orGate(1,0)
print 1, 1, orGate(1,1)

# Truth table for XOR gate
print "XOR Gate"
print "A","B", "X"
print 0, 0, xorGate(0,0)
print 0, 1, xorGate(0,1)
print 1, 0, xorGate(1,0)
print 1, 1, xorGate(1,1)

# Truth table for NAND gate
print "NAND Gate"
print "A","B","X"
print 0, 0, nandGate(0,0)
print 0, 1, nandGate(0,1)
print 1, 0, nandGate(1,0)
print 1, 1, nandGate(1,1)

# Truth table for NAND gate
print "NOR Gate"
print "A","B", "X"
print 0, 0, norGate(0,0)
print 0, 1, norGate(0,1)
print 1, 0, norGate(1,0)
print 1, 1, norGate(1,1)

# (AB + AC)
def abac(A, B, C) :
    return orGate(andGate(A,B), andGate(A,C))

# Truth table for (AB + AC) circuit
print "(AB + AC) Circuit"
print "A","B","C","X"
print 0,0,0,abac(0,0,0)
print 0,0,1,abac(0,0,1)
print 0,1,0,abac(0,1,0)
print 0,1,1,abac(0,1,1)
print 1,0,0,abac(1,0,0)
print 1,0,1,abac(1,0,1)
print 1,1,0,abac(1,1,0)
print 1,1,1,abac(1,1,1)

# deathByArvid Circuit
def deathbyArvid(A, B, C, D) :
    return (norGate(nandGate(A,B),orGate(xorGate(A,C),andGate(notGate(B),D))))

# Truth table for deathByArvid Circuit
print "deathByArvid Circuit"
print "A","B","C","D","X"
print 0,0,0,0,deathbyArvid(0,0,0,0)
print 0,0,0,1,deathbyArvid(0,0,0,1)
print 0,0,1,0,deathbyArvid(0,0,1,0)
print 0,0,1,1,deathbyArvid(0,0,1,1)
print 0,1,0,0,deathbyArvid(0,1,0,0)
print 0,1,0,1,deathbyArvid(0,1,0,1)
print 0,1,1,0,deathbyArvid(0,1,1,0)
print 0,1,1,1,deathbyArvid(0,1,1,1)
print 1,0,0,0,deathbyArvid(1,0,0,0)
print 1,0,0,1,deathbyArvid(1,0,0,1)
print 1,0,1,0,deathbyArvid(1,0,1,0)
print 1,0,1,1,deathbyArvid(1,0,1,1)
print 1,1,0,0,deathbyArvid(1,1,0,0)
print 1,1,0,1,deathbyArvid(1,1,0,1)
print 1,1,1,0,deathbyArvid(1,1,1,0)
print 1,1,1,1,deathbyArvid(1,1,1,1)
