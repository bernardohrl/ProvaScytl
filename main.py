import socket
import numpy as np
from consts import HOST, PORT 
from decode import get_packets, transform, decode_string
from encode import pad_message, invert_format, findPrime, xor, adds_extremities

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
    list_packets, list_end_start = get_packets(raw_msg)
    hex_transformed_packets = transform(list_packets)
    single_array = np.concatenate(hex_transformed_packets, axis=None)   # Step 3
    decoded_string = decode_string(single_array)


    print("Decoded Message (formated):", decoded_string, "\n")


    # Encode
    inverted_string = decoded_string[::-1]

    padded = pad_message(inverted_string)
    lists_hex = invert_format(padded)

    prime_factor = findPrime()
    lists_xor = xor(lists_hex, prime_factor)

    result_list = adds_extremities(lists_xor, list_end_start)
    result_conc = ''.join(result_list)
    result = result_conc.replace('0x', ' ').lstrip()    
    byte_array = bytearray.fromhex(result)

    
    
    sock.send(byte_array)
    response = sock.recv(2048)
    

    if(response.hex() == "c657557a7a9e21"):
        print('\n\n\t\t SUCCESS\n\n\n')
    if(response.hex() == "c652d745d29e21"):
        print('\n\n\t\t FAIL\n\n\n')


main()