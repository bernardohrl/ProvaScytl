import re
import binascii

def get_packets(raw_msg):
    hex_msg = raw_msg.hex()
    hex_list = split_string(hex_msg, 2)

    list_packets = list(get_sublists(hex_list, 7))

    # Removes first and last elements from each lits
    list_packets = [packet[1:6] for packet in list_packets]

    return list_packets


def convert(list_packets):

    print(list_packets)
    print('\n\n\n')

    for i, packet in enumerate(list_packets):

        binary_packet = [hex_to_binary(hex_element) for hex_element in packet]

        concatenated_packet = ''.join(binary_packet)

        packet_5bit = split_string(concatenated_packet, 5)

        print(packet_5bit)

        # for j, element in enumerate(packet_5bit):
        #     print()
        
        list_packets[i] = concatenated_packet
        

    # print(list_packets)



# Get sublists with N elements
def get_sublists(lst, n):
    for i in range(0, len(lst), n):
        yield lst[i:i + n]


def hex_to_binary(hex_string):
    return bin(int(hex_string, 16))[2:].zfill(8)


# Split String into list of N characters || Example: 'olhaesssecara' => ['olha', 'esse', 'cara']
def split_string(string, n):
    regex = n * '.'
    return re.findall(regex, string)

