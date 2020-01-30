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
            packet_5bit[j] = TABLE_1_INVERSE[element]

        concatenated_packet = ''.join(packet_5bit)
        packet_8bits = split_string(concatenated_packet, 8)
        
        hex_packet = [bin_to_hex(bin_element) for bin_element in packet_8bits]

        list_packets[i] = hex_packet
    
    return list_packets


#### HELPER FUNCTIONS


# Get sublists with N elements
def get_sublists(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(8)

def bin_to_hex(bin_string):
    return hex(int(bin_string, 2))


# Split String into list of N characters || Example: 'olhaesssecara' => ['olha', 'esse', 'cara']
def split_string(string, n):
    regex = n * '.'
    return re.findall(regex, string)

