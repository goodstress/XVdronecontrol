import socket
import numpy as np
from threading import Thread

# Yeah this is a little sketchy, but I think it is a decent way to do the loop

host = ""
port = 8888


def recvall(count):
    buf = b''
    while count:
        newbuf = s.recv(count)
        if not newbuf: return None
        buf += newbuf
        count -= len(newbuf)
    return buf


class Client(Thread):
    def __init__(self):
        pass

    def run(self):
        soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            soc.connect((host, port))
        except socket.error as error:
            pass
        while 1:
            try:
                length = recvall(16)
                data_string = recvall(int(length))
                data = np.fromstring(data_string, dtype="uint8")
            except:
                pass
                # huston we gotta problem

