import numpy as np

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
            key_string += chr(matrix[i][j] + ord('A'))
    return key_string

def plaintext_vector(text,size):
    matrix = []
    for i in range(size):
        char = text[i]
        matrix.append(ord(char)-ord('A'))
    return np.array(matrix)

def ciphertext(vector):
    string = ''
    size = len(vector)
    for i in range(size):
        string += chr(vector[i]+ord('A'))
    return string

key = "GYBNQKURP"
text1 = "ANTCATDOG"
matrix1 = create_matrix(text1,3)
plaintext = "ACT"
key_matrix = create_matrix(key,3)
vector = plaintext_vector(plaintext,3)
final_vector = np.dot(key_matrix,vector)%26
print(ciphertext(final_vector))
vector2 = np.dot(matrix1,key_matrix)
vector2 = vector2.flatten()
print(ciphertext(vector2))






    
