import binascii
from consts import TABLE_1, PORT, MAX_NUMBER_1_BYTE
from helper import split_string, hex_to_binary, get_sublists, bin_to_hex, largest_prime_factor


# Step 1
def pad_message(string):
    rest = len(string) % 4

    if(rest != 0):
        string = string + ((4-rest) * '_')

    return string


# Steps 2 and 3
def invert_format(string):

    # String to list of Hexs
    hex_string = string.encode("utf-8").hex()
    hex_list = split_string(hex_string, 2)

    # List of hex turn into list of bins
    bin_list = [hex_to_binary(hex_el) for hex_el in hex_list]

    # Group every 4 elements in a sublist
    lists_bin = list(get_sublists(bin_list, 4))

    # Concatenate sublists, so they can be splited in 4 char for element
    lists_concatenated = [''.join(list_bin) for list_bin in lists_bin ]
    lists_4bits = [split_string(list_concatenated, 4) for list_concatenated in lists_concatenated ]


    # Transform lists_4bits elements to 5 bits
    for i, list_ in enumerate(lists_4bits):
        for j, element in enumerate(list_):
            lists_4bits[i][j] = TABLE_1[element]
     

    # Transforms elements with 5 bits to 8 bits
    lists_5bits_concatenated = [''.join(list_) for list_ in lists_4bits ]
    lists_8bits = [split_string(list_, 8) for list_ in lists_5bits_concatenated ]


    # 8 bits to hex
    lists_hex = lists_8bits
    for i, list_ in enumerate(lists_hex):
        for j, element in enumerate(list_):
            lists_hex[i][j] = bin_to_hex(element)
            # lists_hex[i][j] = hex(int(element, 2))

            
    return lists_hex    

# Step 4
def findPrime():
    
    largest = largest_prime_factor(PORT)
    temp_port = PORT

    while(largest > MAX_NUMBER_1_BYTE):
        temp_port = PORT / largest
        largest = largest_prime_factor(temp_port)



    return hex(largest)[2:]
    


def xor(lists, prime):
    for i, list_ in enumerate(lists):
        for j, element in enumerate(list_):
            lists[i][j] = hex(int(element, 16) ^ int(prime, 16))

    return lists


