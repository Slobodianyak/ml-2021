import numpy as np
from random import random
import time

start_time = time.time()

#n = int(input("n = "))
n = 1000

A = []
B = []
C = []

def find_mtrx(A,B,n):
    for i in range(n):
        r_A = []
        r_B = []
        for j in range(n):
            r_A.append(int(random()*9))
            r_B.append(int(random()*9))
        A.append(r_A)
        B.append(r_B)
         
def print_mtrx(A,n):
    print("\n")
    for i in range(n):
        print(A[i])

def zeros_mtrx(A,n):
    for i in range(n):
        z_A = []
        for j in range(n):
            z_A.append(int(0))
        A.append(z_A)

def mtrx_on_mtrx(A,B,С,n):
    for i in range(n):
        for j in range(n):
            for k in range(n):
                C[i][j] += A[i][k]*B[k][j]

zeros_mtrx(C,n)

find_mtrx(A,B,n)

#print_mtrx(A,n)
#print_mtrx(B,n)

mtrx_on_mtrx(A,B,C,n)

#print_mtrx(C,n)

print("\nHandmade, if n =",n)
print("--- %s seconds ---" % (time.time() - start_time))