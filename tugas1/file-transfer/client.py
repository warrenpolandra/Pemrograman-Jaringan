import sys
import socket
import logging

#set basic logging
logging.basicConfig(level=logging.INFO)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.16.16.101', 32444)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Read file
    file = open("newFile.txt", "r")
    message = file.read()
    
    # Send filename
    sock.send("newFile.txt".encode("utf-8"))
    logging.info(f"sending filename")
    msg = sock.recv(32).decode("utf-8")
    logging.info(f"{msg}")
    
    # Send file data
    sock.send(message.encode("utf-8"))
    logging.info(f"sending file...")
    
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16).decode("utf-8")
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    file.close()
    sock.close()
