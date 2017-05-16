import socket
import sys

host = ""
port = 8888

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

data_to_send = "cool data"  # this var is modified by the other threads throguh Laptio/main.py


def run_server():
    try:
        soc.bind((host, port))
    except socket.error as error:
        sys.exit()

    # not sure if this is nessesary but it is in here for now.  pls try and remove once we can test this
    soc.listen(4)
    while 1:
        conn, addr = soc.accept()
        try:
            while 1:
                # This tells the client how long to expect the message to be
                conn.send(str(len(data_to_send)).ljust(16))
                # This sends the message to the client
                conn.send(data_to_send)

        except socket.error:
            break
    soc.close()
