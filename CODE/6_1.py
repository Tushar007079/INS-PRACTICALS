import random

def generate_key(length):
    """Generates a random key of given length."""
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    return ''.join(random.choice(alphabet) for _ in range(length))

def encrypt(plain_text, key):
    """Encrypts the given plain text using the key."""
    alphabet = "qwertyuiopasdfghjklzxcvbnm"
    cipher_text = ""
    for i in range(len(plain_text)):
        plain_index = alphabet.find(plain_text[i])
        key_index = alphabet.find(key[i])
        cipher_index = (plain_index + key_index) % 26
        cipher_text += alphabet[cipher_index]
    return cipher_text

def main():
    plain_text = input("Enter the plain text: ").lower().replace(" ", "")
    key = generate_key(len(plain_text))
    cipher_text = encrypt(plain_text, key)
    print("Key:", key)
    print("Plain text:", plain_text)
    print("Cipher text:", cipher_text)

if __name__ == "__main__":
    main()
