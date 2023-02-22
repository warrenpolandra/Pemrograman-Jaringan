import sys
import socket
import logging
import datetime
import time

#set basic logging
logging.basicConfig(level=logging.INFO)

date = datetime.datetime.now()
start = datetime.datetime(date.year, date.month, date.day, 10, 22, 0)

t = datetime.datetime.now()
print(waktu saat ini: {t})
print(start)
remaining_time = start-t
print(remaining_time)
time.sleep(remaining_time.seconds)

try:
    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    # Connect the socket to the port where the server is listening
    server_address = ('172.16.16.101', 7000)
    logging.info(f"connecting to {server_address}")
    sock.connect(server_address)

    # Send data
    message = 'INI ADALAH DATA YANG DIKIRIM ABCDEFGHIJKLMNOPQ'
    logging.info(f"sending {message}")
    sock.sendall(message.encode())
    # Look for the response
    amount_received = 0
    amount_expected = len(message)
    while amount_received < amount_expected:
        data = sock.recv(16)
        amount_received += len(data)
        logging.info(f"{data}")
        
except Exception as ee:
    logging.info(f"ERROR: {str(ee)}")
    exit(0)
finally:
    logging.info("closing")
    sock.close()
