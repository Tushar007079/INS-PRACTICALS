def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        # Encrypt uppercase characters
        if char.isupper():
            encrypted_text += chr((ord(char) + shift - 65) % 26 + 65)
        # Encrypt lowercase characters
        elif char.islower():
            encrypted_text += chr((ord(char) + shift - 97) % 26 + 97)
        # If it's neither, just add the character as is
        else:
            encrypted_text += char
    return encrypted_text

# Take inputs from user
input_text = input("Enter the text to be encrypted: ")
shift_value = int(input("Enter the shift value: "))

# Encrypt the input text
encrypted_text = caesar_cipher_encrypt(input_text, shift_value)

# Display the results
print(f"Input Text: {input_text}")
print(f"Shift Value: {shift_value}")
print(f"Encrypted Text: {encrypted_text}")
