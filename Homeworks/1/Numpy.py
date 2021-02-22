import random
import numpy as np
import time


start_time = time.time()

#n = int(input("n = "))
n = 1000

A = np.random.randint(1, 9, size=(n, n))
#print("\n",A)

B = np.random.randint(1, 9, size=(n, n))
#print("\n",B)

C = np.dot(A,B)
#print("\n",C)

print("\nNumpy, if n = ",n)
print("--- %s seconds ---" % (time.time() - start_time))