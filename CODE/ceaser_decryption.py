def caesar_cipher_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        # Decrypt uppercase characters
        if char.isupper():
            decrypted_text += chr((ord(char) - shift - 65) % 26 + 65)
        # Decrypt lowercase characters
        elif char.islower():
            decrypted_text += chr((ord(char) - shift - 97) % 26 + 97)
        # If it's neither, just add the character as is
        else:
            decrypted_text += char
    return decrypted_text

# Take inputs from user
encrypted_text = input("Enter the text to be decrypted: ")
shift_value = int(input("Enter the shift value: "))

# Decrypt the input text
decrypted_text = caesar_cipher_decrypt(encrypted_text, shift_value)

# Display the results
print(f"Encrypted Text: {encrypted_text}")
print(f"Shift Value: {shift_value}")
print(f"Decrypted Text: {decrypted_text}")
