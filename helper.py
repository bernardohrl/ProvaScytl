import re
import binascii
from consts import TABLE_1_INVERSE

#### DECODING MESSAGE


# Step 1
def get_packets(raw_msg):
    hex_msg = raw_msg.hex()
    hex_list = split_string(hex_msg, 2)

    list_packets = list(get_sublists(hex_list, 7))

    # Removes first and last elements from each lits
    list_packets = [packet[1:6] for packet in list_packets]

    return list_packets


# Step 2
def transform(list_packets):

    for i, packet in enumerate(list_packets):

        binary_packet = [hex_to_binary(hex_element) for hex_element in packet]

        concatenated_packet = ''.join(binary_packet)

        packet_5bit = split_string(concatenated_packet, 5)

        for j, element in enumerate(packet_5bit):
            try:
                packet_5bit[j] = TABLE_1_INVERSE[element]
            except Exception as e:
                print("\n\n\nInvalid packet recived. Execute it again.\n\n\n")
                exit()
            

        concatenated_packet = ''.join(packet_5bit)
        packet_8bits = split_string(concatenated_packet, 8)
        
        hex_packet = [bin_to_hex(bin_element) for bin_element in packet_8bits]

        list_packets[i] = hex_packet
    
    return list_packets



# Steps 4 to 7
def decode_string(array_hex):

    # Step 4
    hex_string = ''.join(array_hex)
    ascii_string = bytearray.fromhex(hex_string).decode()

    ascii_string = ascii_string.rstrip()   # Step 5

    formated = lower_and_upper(ascii_string) # Step 6

    replaced = formated.replace(' ', '_') # Step 7

    return replaced




#### HELPER FUNCTIONS


# Get sublists with N elements
def get_sublists(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(8)

def bin_to_hex(bin_string):
    return hex(int(bin_string, 2))[2:]


# Split String into list of N characters || Example: 'olhaesssecara' => ['olha', 'esse', 'cara']
def split_string(string, n):
    regex = n * '.'
    return re.findall(regex, string)


def lower_and_upper(string):
    formated = []
    for i in range(len(string)):
        if i%2==0:
            formated.append(string[i].upper())
        else:
            formated.append(string[i].lower())
    return ''.join(formated)