# The provided code implements a method for sending a message securely by adding a SHA-256 hash for integrity verification

import hashlib

def send_secure_message_alternative():
    """
    This function sends a message securely by adding a SHA-256 hash for
    integrity verification.
    """
    data = input("Enter the message to be sent: ")
    print("** Sender Side **")
    print("Data:", data)
    print("-" * 10)
    
    # Using SHA-256 instead of SHA-512 for hashing
    digest = hashlib.sha256(data.encode()).hexdigest()
    final_data = data + "::" + digest
    print("Final Data:", final_data)
    print("-" * 10)
    print("** Sending Data **")
    print("-" * 10)
    
    print("** Receiver Side **")
    print("-" * 10)
    print("Received Data:", final_data)
    print("-" * 10)
    
    received_data, received_digest = final_data.split("::")
    new_digest = hashlib.sha256(received_data.encode()).hexdigest()
    print("Received Data:", received_data)
    print("Received Digest:", received_digest)
    print("-" * 10)
    
    print("Verifying Data Integrity...")
    if new_digest == received_digest:
        print("Data Integrity Verified - Message Not Altered")
    else:
        print("Data Integrity Failed - Message Altered")

send_secure_message_alternative()
