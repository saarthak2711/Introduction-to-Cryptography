import random
from Crypto.Util.number import getPrime, inverse, bytes_to_long, long_to_bytes

class RSA:
    """Implements the RSA public key encryption / decryption."""
    def __init__(self, key_length):
        self.e = 65537  # Common choice for e
        self.p = getPrime(key_length // 2)
        self.q = getPrime(key_length // 2)
        self.n = self.p * self.q
        phi = (self.p - 1) * (self.q - 1)
        self.d = inverse(self.e, phi)

    def encrypt(self, binary_data):
        m = bytes_to_long(binary_data)
        c = pow(m, self.e, self.n)
        return c

    def decrypt(self, encrypted_int_data):
        m = pow(encrypted_int_data, self.d, self.n)
        return long_to_bytes(m)

class RSAParityOracle(RSA):
    """Extends the RSA class by adding a method to verify the parity of data."""
    def is_parity_odd(self, encrypted_int_data):
        decrypted_message = self.decrypt(encrypted_int_data)
        return bytes_to_long(decrypted_message) % 2 == 1

def parity_oracle_attack(ciphertext, rsa_parity_oracle):
    n = rsa_parity_oracle.n
    e = rsa_parity_oracle.e

    # Initialize the multiplier
    multiplier = pow(2, e, n)
    current_ciphertext = ciphertext

    lower_bound = 0
    upper_bound = n

    while upper_bound - lower_bound > 1:
        current_ciphertext = (current_ciphertext * multiplier) % n
        if rsa_parity_oracle.is_parity_odd(current_ciphertext):
            lower_bound = (lower_bound + upper_bound) // 2
        else:
            upper_bound = (lower_bound + upper_bound) // 2

    return long_to_bytes(lower_bound)

def main():
    input_bytes = input("Enter the message: ")

    # Generate a 1024-bit RSA pair
    rsa_parity_oracle = RSAParityOracle(1024)

    # Encrypt the message
    ciphertext = rsa_parity_oracle.encrypt(input_bytes.encode())
    print("Encrypted message is: ", ciphertext)

    # Check if the attack works
    plaintext = parity_oracle_attack(ciphertext, rsa_parity_oracle)
    print("Obtained plaintext: ", plaintext.decode())
    assert plaintext == input_bytes.encode()

if __name__ == '__main__':
    main()
