import socket
import numpy as np
from consts import HOST, PORT 
from helper import get_packets, transform, decode_string

def main():

    # Connecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print("\n\nConnected\n")
    except Exception as e:
        print("Cannot connect to the server:", e)
 
    # Decode
    raw_msg = sock.recv(2048)
    list_packets = get_packets(raw_msg)
    hex_transformed_packets = transform(list_packets)
    single_array = np.concatenate(hex_transformed_packets, axis=None)   # Step 3
    decoded_string = decode_string(single_array)


    print("Decoded Message:", decoded_string, "\n\n")


    # Encode
    inverted_string = decoded_string[::-1]

    # padded = pad_message(inverted_string)








main()