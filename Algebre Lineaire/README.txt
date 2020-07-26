############# Linear Algebra #############
####### Author: aalp75 ########
####### Edited in 2020 ########


Contents
I   - Linear Algebra
II  - Functions
III  - Performance

I - Linear Algebra

This Notebook LinearAlgebra.ipypn contains all basic algorithlm for Linear Algebra.
It worked with numpy

II - Functions

Here is the list of functions

- is_sym(A): Test if the matrix A is symetric

- determinant_naive(A) : Calculate the determinant of A with the basic formula, complexity is n!

- determinant_gauss(A) : Calculate the determinant of A with Gaussian elimination, complexity is n^3

- is_def_pos_sylvester(A) : Test is the symetric matrix A is positive definite with Sylvester critera

- inverse_gauss(A) : Find the inverse of A if there exist with Gaussian elimination method

- cholesky(A) : Find the cholesky decomposition L such that A = L.T * L for a symetric matrix A

- eigen(A) : Find the eigenvalues and eigenvectors of A if the matrix is diagonalizable


III - Performance

The determinant of a matrix (1000,1000) is calculate in approximatively 2 seconds with the gaussian Elimination

The diagonalization of a matrix (500,500) is done in approximatively 10 seconds