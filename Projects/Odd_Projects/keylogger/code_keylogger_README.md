# CerealSpiller Keylogger
CerealSpiller is a simple keylogger script written in Python. It captures keystrokes entered by the user and stores them in a file. The script also provides basic encryption functionality to encrypt the captured keystrokes. It also include a decrypter script. Purpose of encryption of text to reduce changes of being discovered through deep packet technology. Generic file naming convention intentionally  created for ease of instruction and not for obfucation.

## Features
- **Keystroke Logging**: The script captures keystrokes, including normal characters, special keys (e.g., Space, Enter, Backspace), and Ctrl + C, and logs them to a file.
- **File Encryption**: The captured keystrokes can be encrypted using the Fernet encryption scheme provided by the cryptography library.
- **Graceful Termination**: The script can be terminated by pressing the Escape key, which closes the file, encrypts the captured keystrokes, and exits the program.

## Requirements
- Python 3.x
- Install dependencies by running `pip install cryptography also pynput `

## Usage
1. Run the script by executing the following command: `python CerealSpiller.py`.
2. The script will start capturing keystrokes and logging them to a file named `secretlogs_<date>.txt`, where `<date>` is the current date in the format `YYYY-MM-DD`.
3. Press the Escape key to stop the keylogging and encrypt the captured keystrokes.
4. The encrypted file will be saved as `secretlogs_<date>.txt.encrypted`.

## Functionality

### Keystroke Logging
CerealSpiller captures various types of keystrokes, including:

- Normal characters: Any letter, number, or symbol entered by the user.
- Special keys: Space, Enter, Backspace.
- Ctrl + C: Captures the Ctrl + C combination, which is commonly used for copying text.

### File Encryption
CerealSpiller provides a basic encryption functionality using the Fernet encryption scheme from the cryptography library. When the keylogging is stopped, the captured keystrokes are encrypted using a provided password and saved to an encrypted file. This ensures that the captured data remains secure and unreadable without the encryption key.

### Graceful Termination
The keylogging process can be terminated gracefully by pressing the Escape key. When the Escape key is pressed, CerealSpiller performs the following actions:

1. Closes the file used for logging keystrokes.
2. Encrypts the captured keystrokes using the provided password.
3. Exits the program.

# File Decryption Script - Cleanbowl.py

Having small issue with Cleanbowl decrypting

This script allows you to decrypt an encrypted file using the Fernet encryption scheme from the cryptography library in Python.
Prerequisites

##Before running the script, make sure you have the following:
    Python 3 installed
    The cryptography library installed. You can install it using pip:

    pip install cryptography

#Usage
To use this script, follow these steps:

    Copy the script into a Python file (e.g., decrypt_file.py).

    Import the Fernet class from the cryptography.fernet module:

    python

###from cryptography.fernet import Fernet

Run the script with the following command:

python3 CleanBowl.py\
Enter the path of the encrypted file: file name\
Enter the password (default password is 'p4ssw0rdp4ssw0rdp4ssw0rd'): p4ssw0rdp4ssw0rdp4ssw0rd\
