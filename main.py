import socket
from consts import HOST, PORT 
from helper import get_packets, convert

def main():

    # Connecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((HOST, PORT))
        print("\n\nConnected\n\n")
    except Exception as e:
        print("Cannot connect to the server:", e)
 

    raw_msg = sock.recv(2048)   
    list_packets = get_packets(raw_msg)
    convert(list_packets)



main()