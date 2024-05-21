import random as rd

class VigenereCipher:
    def __init__(self):
        self.alphabets = {chr(x + 97): x for x in range(26)}

    def generate_key(self, length):
        key = ''
        for _ in range(length):
            key += chr(97 + rd.randint(0, 25))
        return key

    def encrypt(self, plaintext, key):
        ciphertext = ''
        key_length = len(key)
        for i, char in enumerate(plaintext):
            if char.isalpha():
                shift = self.alphabets[key[i % key_length]]
                encrypted_char = chr(((self.alphabets[char] + shift) % 26) + 97)
                ciphertext += encrypted_char
        return ciphertext

def main():
    print('Vigenere cipher')
    cipher = VigenereCipher()
    key_length = rd.randint(6, 10)
    key = cipher.generate_key(key_length)
    print('Generated Key:', key)
    num_messages = int(input('\nEnter the number of messages you want to send: '))
    print('\nEncryption:\n')
    ciphertexts = []
    for _ in range(num_messages):
        plaintext = input('Enter plaintext: ').lower().replace(" ", "")
        ciphertext = cipher.encrypt(plaintext, key)
        ciphertexts.append(ciphertext)
        print('Cipher Text:', ciphertext)

if __name__ == "__main__":
    main()
