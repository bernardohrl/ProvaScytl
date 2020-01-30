import socket
import consts 

def main():

    # Connecting
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        sock.connect((consts.HOST, consts.PORT))
        print("\n\nConnected\n\n")

    except Exception as e:
        print("Cannot connect to the server:", e)
 

main()