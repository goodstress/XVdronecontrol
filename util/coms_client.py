import socket
import numpy as np

# settings for run_client()
host = ""  # raspberry pi ip
port = 8888  # port to use

# code for comunication
soc = None


def recvall(count):
    buf = b''
    while count:
        newbuf = soc.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


def run_client():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        soc.connect((host, port))
    except socket.error as error:
        pass
    while 1:
        # noinspection PyBroadException
        try:
            soc.send()
            length = recvall(16)
            data_string = recvall(int(length))
            data = np.fromstring(data_string, dtype="uint8")
            print(data)
            # at this point we would unpack the data from the dictionary that was sent
        except:
            pass
            # huston we gotta problem


