#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import math


# In[2]:


def is_sym(A):
    '''
    input : numpy A 
    output : boolean if the Matrix A is symetric
    '''
    n,m = A.shape[0],A.shape[1]
    if (n != m):
        print("Not squared Matrix")
        return False
    for i in range(n//2):
        for j in range(n//2):
            if A[i,j] != A[j,i]:
                return False
    return True     


# In[3]:


def determinant_naive(A):
    '''
    in : numpy A
    out : float 
    calculate the determinant of a matrix A 
    iterative method
    '''
    det = 0
    if (A.shape[0] != A.shape[1]):
        print("Not squared matrix")
        return 0
    n = A.shape[0]
    if (n == 2):
        det = A[0,0]*A[1,1] - A[0,1]*A[1,0]
        return det
    index = np.arange(n)
    for i in range(n):
        if (A[0,i] != 0):  
            det += pow(-1,i) * A[0,i] * determinant_naive(A[1:n,index !=i])
    return det
        


# In[4]:


def permute_rows(A,i1,i2):
    n = A.shape[0]
    tmp = np.zeros(n)
    for j in range(n):
        tmp[j] = A[i1,j]
    A[i1,:]=A[i2,:]
    for j in range (n):
        A[i2,j] = tmp[j]
    return(A)

def determinant_gauss(A,show=False):
    '''
    in : numpy A
    out : float 
    calculate the determinant of a matrix A 
    gaussian elimination method
    show=True if you want to print the tringular matrix at the end
    '''
    A = A.astype(float)
    det = 0
    n,m = A.shape[0],A.shape[1]
    if (n !=m):
        print("Not squared Matrix")
        return 0
    number_permut = 0
    for j in range(n):
        row = n
        for i in range(j,n):
            if (A[i,j] != 0):
                row  = i
                break
        if (row == n):
            return 0
        if (row != j):
            permute_rows(A,j,row)
            number_permut +=1         
        for i in range(j+1,n):
            mult = A[i,j]/A[j,j]
            A[i,:] = A[i,:] - A[j,:] * mult
    if show:
        print(A)
    det = 1
    for i in range(n):
        det = det * A[i,i]
    return pow(-1,number_permut)*det
    


# In[5]:


def is_def_pos_sylvester(A):
    '''
    input : numpy A a symetric matrix
    output : boolean if the matrix is positive definite
    Sylvester Criteria that check if all the minor determinant are positive
    '''
    n,m = A.shape[0],A.shape[1]
    if ( n != m):
        print("Not squared Matrix")
        return False
    for i in range(1,n+1):
        if (determinant_gauss(A[0:i,0:i]) <= 0):
            return False
    return True


# In[6]:


def inverse_gauss(A):
    '''
    input : numpy A a squared matrix
    output : the inverse of A
    inverse by gaussian elimination
    '''
    A = A.astype(float)
    n,m = A.shape[0],A.shape[1]
    if (n !=m):
        print("Not squared Matrix")
        return np.zeros((n,n))
    inv = np.identity(n)
    for j in range(n):
        row = n
        for i in range(j,n):
            if (A[i,j] != 0):
                row  = i
                break
        if (row == n):
            return 0
        if (row != j):
            permute_rows(A,j,row)
            permute_rows(inv,j,row)        
        for i in range(j+1,n):
            mult = A[i,j]/A[j,j]
            A[i,:] = A[i,:] - A[j,:] * mult
            inv[i,:] = inv[i,:] - inv[j,:] * mult
    det = 1
    for i in range(n):
        det = det * A[i,i]
    if(det==0):
        print("Not inversible")
        return np.zeros((nn))
    for j in np.arange(n-1,0,-1):
        divisor = A[j,j]
        A[j,j] = A[j,j] / divisor # =1
        inv[j,:] = inv[j,:] / divisor #jusque la OK
        for i in np.arange(j-1,-1,-1):
            mult = A[i,j]
            A[i,:] = A[i,:] - mult *A[j,:]
            inv[i,:] = inv[i,:] - mult * inv[j,:]
    divisor = A[0,0]
    A[0,0] = A[0,0] / divisor
    inv[0,:] = inv[0,:] / divisor
    return(inv)
            
        


# In[7]:


def cholesky(A):
    """
    Input : numpy A(n,n) (matrix symetric)
    Output : numpy L(n,n) The triangular lower matrix of the Cholesky Decomposition
    A = L * L.T
    """
    if not is_def_pos_sylvester(A):
        print("Not squared symetric matrix")
        return 0
    n = A.shape[0]
    L = np.zeros((n,n))
    L[0,0] = math.sqrt(A[0,0])
    for j in range(1,n):
        L[j,0] = A[0,j] / L[0,0]
    for i in range(1,n):
        L[i,i] = math.sqrt(A[i,i] -pow(L[i,0:i],2).sum())
        for j in range(i+1,n):
            L[j,i] = (A[i,j] - np.dot(L[i,0:i].T,L[j,0:i]))/L[i,i]
    return L

def determinant_cholesky(A):
    L = cholesky(A)
    determinant = 1
    for i in range(L.shape[0]):
        determinant = determinant * pow(L[i,i],2)
    return determinant


# In[8]:


def power_iteration(A, num_simulations_max=pow(10,5), tol=pow(10,-3)):
    """
    input : A a squared matrix
    output : the biggest eigenvalor and the eigenvector associate
    power iteration method x = A*A*A*A*A*...*A(x)
    """
    x_n = np.random.rand(A.shape[1])

    for i in range(num_simulations_max):
        # calculate the matrix-by-vector product Ax
        x_n1 = np.dot(A, x_n)

        # calculate the norm L2 of vector
        x_n1_norm = np.linalg.norm(x_n1,2)

        # re normalize the vector
        x_n = x_n1 / x_n1_norm
        if (i>200 and np.linalg.norm(abs(x_n) - abs(x_old),2) < tol):
            break

        x_old = x_n
        if (i == num_simulations_max - 1):
            return([None,None])
    # Round at 3 decimal after coma
    eigenvalue = round(np.dot(np.dot(x_n.T,A),x_n)/np.dot(x_n.T,x_n),5)
    res = [eigenvalue, x_n]

    return res

def deflation(A, eigenvalue, v , w):
    """
    v is the eigenvector of A associate to the eigenvalue lambda
    v is the eigenvector of A.T associate to the eigenvalue lambda
    B = A - lambda * (v*w.T)/(w.T,v)
    """
    v = v.reshape(A.shape[0],1)
    w = w.reshape(A.shape[0],1)
    B = A - eigenvalue * np.dot(v,w.T) / np.dot(w.T,v)
    return B


# In[9]:


def eigen(A):
    '''
    input : numpy squared matrix A
    out : eigenvalues and eigevectors of the matrix if A is diagonalizable
    '''
    B = A
    if (B.shape[0] != B.shape[1]):
        print("Not squared Matrix")
        return (0,0)
    eigenvectors = []
    eigenvalues = []
    for i in range(B.shape[0]):
        tmp = power_iteration(B)
        if (tmp[0] == None) :
            print("Matrix is not diagonalizable")
            break
        eigenvalues.append(tmp[0])
        eigenvectors.append(tmp[1])
        tmp2 = power_iteration(B.T)#To apply deflation method we need to have eigenvector of the transpose matrix
        B = deflation(B,tmp[0],tmp[1],tmp2[1])
    return eigenvalues,eigenvectors


# In[10]:


def eigen_matrix(A):
    """
    input : numpy squared matrix A
    out : the transition matrix P if A is diagonalizable such that A = inv(P)*D*P
    """
    eigenvalues,eigenvectors = eigen(A)
    n = A.shape[0]
    P = np.zeros((n,n))
    for i in range(n):
        P[:,i] = eigenvectors[i]
    return P

