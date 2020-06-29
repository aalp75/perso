#!/usr/bin/env python
# coding: utf-8


import numpy as np
import time
import random


def PGCD(a,b):
    if (b==0):
        return a
    else:
        r=a%b
        return PGCD(b,r)


# Deterministic Method

def is_prime(n):#Naive method
    if (n%2 == 0):
        return False
    for i in range(3,int((np.sqrt(float(n)))+2)):
        #print(i)
        if (n%i == 0):
            return False
    return True

def is_prime_faster(n):
    if (n<=1):
        return False
    if (n<=3):
        return True
    if (n%2 ==0 or n%3 ==0):
        return False
    i = 5
    while(i*i <n):
        if(n%i == 0 or n%(i+2)==0):
            return False
        i = i+6
    return True


# Probabilistic Method


# Python3 program Miller-Rabin primality test

def MillerTest(d, n):

    # Pick a random number in [2..n-2]
    # Corner cases make sure that n > 4
    a = 2 + random.randint(1, n - 4);

    x = pow(a, d, n)

    if (x == 1 or x == n - 1):
        return True;

    # Keep squaring x while one
    # of the following doesn't
    # happen
    # (i) d does not reach n-1
    # (ii) (x^2) % n is not 1
    # (iii) (x^2) % n is not n-1
    while (d != n - 1):
        x = (x * x) % n
        d *= 2

        if (x == 1):
            return False;
        if (x == n - 1):
            return True;

    # Return composite
    return False

# It returns false if n is
# composite and returns true if n
# is probably prime. k is an
# input parameter that determines
# accuracy level. Higher value of
# k indicates more accuracy.
def is_prime_Miller( n, k):

    # Corner cases
    if (n <= 1 or n == 4):
        return False
    if (n <= 3):
        return True
    d = n - 1
    while (d % 2 == 0):
        d //= 2

    # Iterate given nber of 'k' times
    for i in range(k):
        if (MillerTest(d, n) == False):
            return False

    return True


# Decomposition in prime number



#Iterative method
def decomposition_prime_number(n):
    tmp = n
    res = []
    if (n < 2):
        res.append(n)
        return res
    for i in range(2,n+1):
        while (n % i == 0):
            res.append(i)
            n /= i
    print('%d'%tmp + ' = ' + ' * '.join('%d'%item for item in res))
    return f


# Pollard Rho decomposition


##############################################################################
def facteursdiv2(n):
    """Décomposition par division de n (entier) en 2 facteurs quelconques"""
    pp = [2, 3, 5, 7, 11]
    racn = int(np.sqrt(n))+1  # racine carrée entière de n
    for p in pp:
        if p>racn:
            return [n, 1]  # n est premier
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
    p = pp[-1] + 2
    while p <= racn:
        if n%p == 0:
            return [p, n//p]  # on a trouvé une décomposition
        p += 2
    # si on arrive ici, n est premier
    return [n, 1]

#############################################################################
def pollardrho(n):
    """Factorisation d'un nombre entier décomposable (méth. rho de pollard)"""
    f = lambda z: z*z+1
    x, y, d = 2, 2, 1
    while d==1:
        x = f(x) % n
        y = f(f(y)) % n
        d = PGCD(x-y, n)
    return [d, n//d]

##############################################################################
def factpremiers(n):
    """liste des facteurs premiers de n, avec la fonction 'a, b = decomp(n)' """
    R = []  # liste des facteurs premiers trouvés
    P = [n]  # pile de calcul
    while P!=[]:
        x = P.pop(-1)  # lecture et dépilage de la dernière valeur empilée
        if is_prime_Miller(x,1):
            R.append(x)  # on a trouvé un facteur 1er => on ajoute à la liste
        else:
            a, b = pollardrho(x)  # on calcule une nouvelle décomposition
            if a==1 or b==1:
                # echec: x n'est pas 1er mais sa decomposition ne se fait pas
                # on essaie une décomposition par division
                a, b = facteursdiv2(x)
            P.append(a)  # on empile a
            P.append(b)  # on empile b
    R.sort()
    print('%d'%n + ' = ' + ' * '.join('%d'%item for item in R))
    return R
