def monoalphabetic_cipher_decrypt(text, substitution_alphabet):
    # Create a mapping of ciphertext to plaintext
    alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    reverse_mapping = {substitution_alphabet[i]: alphabet[i] for i in range(len(alphabet))}
    
    decrypted_text = ""
    for char in text:
        if char.upper() in reverse_mapping:
            if char.isupper():
                decrypted_text += reverse_mapping[char]
            else:
                decrypted_text += reverse_mapping[char.upper()].lower()
        else:
            decrypted_text += char
    return decrypted_text

# Take inputs from user
encrypted_text = input("Enter the text to be decrypted: ")
substitution_alphabet = input("Enter the substitution alphabet (26 uppercase letters): ")

# Ensure the substitution alphabet is valid
if len(substitution_alphabet) != 26 or not substitution_alphabet.isupper():
    print("Invalid substitution alphabet. Please enter 26 uppercase letters.")
else:
    # Decrypt the input text
    decrypted_text = monoalphabetic_cipher_decrypt(encrypted_text, substitution_alphabet)

    # Display the results
    print(f"Encrypted Text: {encrypted_text}")
    print(f"Substitution Alphabet: {substitution_alphabet}")
    print(f"Decrypted Text: {decrypted_text}")
