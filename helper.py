import re


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