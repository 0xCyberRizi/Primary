Server-Client Connection with Base64 Command Execution

This is a server-client program that establishes a connection between the server and the client. The server can execute base64 encoded commands received from the client and decode the information. The client will run the commands and return the results in a get request to the server. This program is developed as part of the DSU Class CSC842 Security Tool Development, taught by Professor Welu.

Main Ideas:

    Base64 Encoding and Decoding: The program utilizes base64 encoding and decoding to securely transmit and receive commands between the server and the client.

    Command Execution: The server can execute commands received from the client and provide the command results.

    File Upload and Storage: The program supports file upload functionality, allowing the client to send files to the server, which are then stored in a specified location.

    Multi-threaded Server: The server is implemented using a multi-threaded approach, allowing it to handle multiple client connections concurrently.

    Can be used for educational purposes for simulating malware network traffic.

    
Challenges:

    Getting the Server to talk to the client via posts. The client reaches out to conduct get requests for commands and responds with results. The overall challenge was encoding and decoding the base64 traffic so the traffic could not be directly seen. Designing the program to handle a large number of client connections and ensuring efficient resource utilization can be challenging, especially when dealing with multiple simultaneous requests. User Experience: Designing a user-friendly interface, providing clear instructions, and handling user inputs effectively is essential for a smooth user experience.

Future Improvements:

Implementing additional security measures such as encryption for command transmission such as ssh and so on. Maybe throw in a GUI.

Usage

    Run the program by executing the Python script.
    The program will prompt you to enter the server IP, port, bot IP address, and file location. You can provide default values or customize them.
    The server will start listening for incoming connections from the client.
    Once the client is connected, the server will display a menu of options for commands to be executed on the client.
    You can choose a command from the menu and enter it as input in the server shell.
    If the encode_send_command flag is set to 'yes' (or 'y'), the command will be encoded in base64 before sending to the client. This helps in protecting the command during transmission.
    The client receives the command, decodes it, and executes it.
    The command results are saved to a file, along with any uploaded files.

Prerequisites

    Python 3.x

Instructions

    Clone the repository or download the source code to your local machine.
    Open a terminal or command prompt and navigate to the project directory.
    Install the required dependencies by running the following command:

    bash

pip install base64

    Client:

    import requests
    import subprocess
    import time
    import os
    import base64
    import datetime

    Server:

    import os
    import cgi
    import threading
    from http.server import HTTPServer, BaseHTTPRequestHandler
    from socketserver import ThreadingMixIn
    from datetime import datetime
    import base64

Run the program using Python 3 by executing the following command:

    python3 server.py

    This will start the server and display the server IP and port where it's listening for connections.

Customization

You can customize the following parameters when running the program:

    Server IP: The IP address of the server. The default value is 127.0.0.1.
    Server Port: The port number on which the server listens for connections. The default value is 80.
    Bot IP Address: The IP address of the client (bot) that connects to the server. The default value is 127.0.0.1.
    File Location: The directory where the command results and uploaded files will be saved. The default location is /home/ubuntu/Desktop/. You can change it to a different directory by providing the appropriate path.

When the server is running, you can interact with it by entering commands in the server shell. The server will send the commands to the client, execute them, and save the results to a file. Additionally, if the server receives an uploaded file from the client, it will save the file to the specified file location.

Note: It's important to ensure that the server and client are running on the same network and can reach each other's IP addresses.

Server-Client Connection with Base64 Command Execution

This is a server-client program that establishes a connection between the server and the client. The server can execute base64 encoded commands received from the client and decode the information. This program is developed as part of the DSU Class CSC842 Security Tool Development, taught by Professor Welu.
Usage

    Run the program by executing the Python script.
    The program will prompt you to enter the server IP, port, bot IP address, and file location. You can provide default values or customize them.
    The server will start listening for incoming connections from the client.
    Once the client is connected, the server will display a menu of options for commands to be executed on the client.
    You can choose a command from the menu and enter it as input in the server shell.
    If the encode_send_command flag is set to 'yes' (or 'y'), the command will be encoded in base64 before sending to the client. This helps in protecting the command during transmission.
    The client receives the command, decodes it, and executes it.
    The command results are saved to a file, along with any uploaded files.

Prerequisites

    Python 3.x

Instructions

    Clone the repository or download the source code to your local machine.
    Open a terminal or command prompt and navigate to the project directory.
    Install the required dependencies by running the following command:

    bash

pip install base64

Run the program using Python 3 by executing the following command:

    sudo python3 server.py

    This will start the server and display the server IP and port where it's listening for connections.

    python3 client.py
    
Customization

You can customize the following parameters when running the program:

    Server IP: The IP address of the server. The default value is 127.0.0.1
    Server Port: The port number on which the server listens for connections. The default value is 80.
    Bot IP Address: The IP address of the client (bot) that connects to the server. The default value is 127.0.0.1.
    File Location: The directory where the command results and uploaded files will be saved. The default location is /home/ubuntu/Desktop/. You can change it to a different directory by providing the appropriate path.

When the server is running, you can interact with it by entering commands in the server shell. The server will send the commands to the client, execute them, and save the results to a file. Additionally, if the server receives an uploaded file from the client, it will save the file to the specified file location.
References

    Python Software Foundation. (n.d.). Python 3. Retrieved from https://www.python.org/
    Base64 - Python Documentation. (n.d.). Retrieved from https://docs.python.org/3/library/base64.html
