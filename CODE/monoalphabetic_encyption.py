def monoalphabetic_cipher_encrypt(text, substitution_alphabet):
    # Create a mapping of plaintext to ciphertext
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    mapping = {alphabet[i]: substitution_alphabet[i] for i in range(len(alphabet))}
    
    encrypted_text = ""
    for char in text:
        if char.upper() in mapping:
            if char.isupper():
                encrypted_text += mapping[char]
            else:
                encrypted_text += mapping[char.upper()].lower()
        else:
            encrypted_text += char
    return encrypted_text

# Take inputs from user
input_text = input("Enter the text to be encrypted: ")
substitution_alphabet = input("Enter the substitution alphabet (26 uppercase letters): ")

# Ensure the substitution alphabet is valid
if len(substitution_alphabet) != 26 or not substitution_alphabet.isupper():
    print("Invalid substitution alphabet. Please enter 26 uppercase letters.")
else:
    # Encrypt the input text
    encrypted_text = monoalphabetic_cipher_encrypt(input_text, substitution_alphabet)

    # Display the results
    print(f"Input Text: {input_text}")
    print(f"Substitution Alphabet: {substitution_alphabet}")
    print(f"Encrypted Text: {encrypted_text}")
