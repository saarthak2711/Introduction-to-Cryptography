import numpy as np
import math
from numpy import matrix
from numpy import linalg

def create_matrix(text, size):
    matrix = []
    for i in range(size):
        row = [(ord(char) - ord('A'))%26 for char in text[i*size:(i+1)*size]]
        matrix.append(row)
    return np.array(matrix)

def matrix_to_key_string(matrix):
    key_string = ''
    size = matrix.shape[0]
    for i in range(size):
        for j in range(size):
            key_string += chr(int(matrix[i][j])%26 + ord('A'))
    return key_string

def plaintext_vector(text,size):
    matrix = []
    for i in range(size):
        char = text[i]
        matrix.append(ord(char)-ord('A'))
    return np.array(matrix)

def modMatInv(A,p):
    n = len(A)
    A = matrix(A)
    adj = np.zeros(shape=(n,n))
    for i in range(0,n):
        for j in range(0,n):
            adj[i][j] = ((-1)**(i+j)*int(round(linalg.det(minor(A,j,i)))))%p
    return (modInv(int(round(linalg.det(A))),p)*adj)%p

def modInv(a,p):
    for i in range(1,p):
        if(i*a)%p==1:
            return i
    raise ValueError(str(a)+" has no inverse mod "+ str(p))

def minor(A,i,j):
    A = np.array(A)
    minor = np.zeros(shape=(len(A)-1,len(A)-1))
    p=0
    for s in range(0,len(minor)):
        if p==i:
            p=p+1
        q=0
        for t in range(0,len(minor)):
            if q ==j:
                q = q+1
            minor[s][t]=A[p][q]
            q=q+1
        p=p+1
    return minor


def ciphertext(vector):
    string = ''
    size = len(vector)
    for i in range(size):
        string += chr(vector[i]+ord('A'))
    return string

plaintext ="ANTCATDOG"
ciphertext = "TIMFINWLY"
plainmatrix = create_matrix(plaintext,3)
ciphermatrix = create_matrix(ciphertext,3)

plaininverse = modMatInv(plainmatrix,26)
key_matrix = np.dot(ciphermatrix,plaininverse)%26
print(matrix_to_key_string(key_matrix))