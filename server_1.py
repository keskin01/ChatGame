import sys
from time import perf_counter
import socket

localIP = "127.0.0.1"

localPort = 20001

bufferSize = 1024

msgFromServer = ""

bytesToSend = str.encode(msgFromServer)

# Create a datagram socket

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

# Bind to address and ip

UDPServerSocket.bind((localIP, localPort))
print("Game is started")

# Listen for incoming datagrams
list_1 = []
while 1:
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    tstart = perf_counter()
    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "{}".format(message)

    s = str(clientMsg)

    msgFromServer = clientMsg

    # Sending a reply to client

    UDPServerSocket.sendto(bytesToSend, address)
    tend = perf_counter()
    tcalc = tend - tstart
    list_1.append(s)
    if len(list_1) == 1 and tcalc <= 15:
        continue
    elif len(list_1) == 2:
        if list_1[0][- 3:-1] == list_1[1][2:4] and tcalc <= 15:
            list_1.pop(0)
            print("Okay")
            continue
        else:
            print("lose")
            break

    elif len(list_1) == 3:
        list_1.pop(0)
    if list_1[0][- 2:] == list_1[1][:2]:
        list_1.pop(0)
        print("Okay")
        continue
    else:
        print("lose")
        break
