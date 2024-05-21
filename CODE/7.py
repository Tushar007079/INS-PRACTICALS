from math import gcd

def RSA(p, q, messages):
    # Calculate n
    n = p * q
    print("The value of n is:", n)
    
    # Calculate the totient function
    totient = (p - 1) * (q - 1)
    print("The value of totient is:", totient)
    
    # Find a suitable value for e
    for i in range(2, totient):
        if gcd(i, totient) == 1:
            e = i
            break
    print("The selected value of e is:", e)
    
    # Find the modular multiplicative inverse of e
    j = 0
    while True:
        if (j * e) % totient == 1:
            d = j
            break
        j += 1
    print("The private key is:", [d, n])
    
    # Encryption
    cipher = [(message ** e) % n for message in messages]
    print("Encrypted messages are:", cipher)
    
    # Decryption
    decrypted_messages = [(ct ** d) % n for ct in cipher]
    print("Decrypted messages are:", decrypted_messages)

def main():
    # Input values of p, q, and the stream of data
    p = int(input("Enter a value of p: "))
    q = int(input("Enter the value of q: "))
    messages = input("Enter the stream of data separated by spaces: ").split()
    messages = [int(i) for i in messages]
    
    # Call the RSA function
    RSA(p, q, messages)

if __name__ == "__main__":
    main()
