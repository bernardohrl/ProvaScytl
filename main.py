import socket
import numpy as np
from consts import HOST, PORT 
from helper import get_packets, transform

def main():

    # Connecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print("\n\nConnected\n\n")
    except Exception as e:
        print("Cannot connect to the server:", e)
 
    # Decode
    raw_msg = sock.recv(2048)
    list_packets = get_packets(raw_msg)
    hex_transformed_packets = transform(list_packets)
    single_array = np.concatenate(hex_transformed_packets, axis=None)   # Step 3

    print(hex_transformed_packets)
    print(single_array)

    





main()