import socket
import sys
import numpy as np

host = ""
port = 8888

soc = None

def run_server():
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        soc.bind((HOST, PORT))
    except socket.error as error:
        print
        PREFIX + "bind failed: " + str(error)
        sys.exit()

    soc.listen(4)
    while 1:
        conn, addr = soc.accept()
        try:
            # message = "watch this crash the wifi"
            while 1:
                

                conn.send(str(len(stringData)).ljust(16))
                conn.send(stringData)

                # cv2.putText(frame, "PandaVISION 0.1", (0,20), cv2.FONT_HERSHEY_SIMPLEX, 0.8, (40, 255, 20), 1)
                # pickled_image = pickle.dumps(frame)

                # array = ["item1", "itemtwo", "itemthwee"]
                # pickled_array = pickle.dumps(array)
                # conn.sendall(pickled_image)
        except socket.error as error:
            print
            PREFIX + "sendall filed:" + str(error)
            sys.exit()
    oc.close()





