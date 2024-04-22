# having small issue with decrypting
from cryptography.fernet import Fernet
import base64
import os

def decrypt_file(encrypted_file_path, key):
    # Read the encrypted file content
    with open(encrypted_file_path, "rb") as encrypted_file:
        encrypted_content = encrypted_file.read()

    try:
        # Create a Fernet cipher object with the provided key
        cipher = Fernet(key)
        print("cipher here: ", cipher)
        
        # Decrypt the encrypted content
        decrypted_content = cipher.decrypt(encrypted_content)
        print("decrypted_content: ", decrypted_content)
        # Decode and print the decrypted content
        print(decrypted_content.decode())

    except Exception as e:
        print("Error occurred during decryption:", e)

if __name__ == "__main__":
    # Get the encrypted file path from user input
    encrypted_file_path = input("Enter the path of the encrypted file: ")
    print("file path: ", encrypted_file_path)

    #if not os.path.isfile(encrypted_file_path):
    #    print("The specified file does not exist.")
    #exit(1)

    # Get the Fernet key from user input or use the default password
    password = input("Enter the password (default password is 'p4ssw0rdp4ssw0rdp4ssw0rd'): ")
    
    key = base64.urlsafe_b64encode(password.encode())
    print('key here: ', key)

    decrypt_file(encrypted_file_path, key)
