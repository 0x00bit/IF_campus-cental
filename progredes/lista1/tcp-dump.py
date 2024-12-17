import sys
import struct

# Magic numbers allowed:
MAGIC1 = '0xa1b2c3d4'
MAGIC2 = '0xa1c2c3d4'


def getFile():
    """
    This function is responsible to deal with paths
    and the PCAP file which the user will pass as 
    argument
    """

    arquivo = ""

    try:
        user_input = input("Insira o arquivo ou o caminho absoluto: ")

        with open(user_input, "rb") as f:
            arquivo = f.readlines()

        return arquivo

    except FileNotFoundError:
        sys.exit("Arquivo informado não existe")


def unpackBits(section):
    """
    This function is responsible to convert bytes gretter than
    4 bytes to hexadecimal and this returns a hexadecimal number
    """

    bytes_array = []  # Auxiliary variable

    for byte in range(0, len(section), 4):
        bytes_array.append(struct.unpack("<I", section[byte:byte+4])[0])

    array_to_hex = hex(sum(bytes_array))
    return array_to_hex


def recordedPackets(arquivo):

    """This function is responsible to read the header of network packages
    and theirs respective data"""

    print(f"{'-'*12} Cabeçalho de rede {'-'*12}")

    offset = 24
    PACKET_HEADER_SIZE = 16
    packer_header = arquivo[offset:offset + PACKET_HEADER_SIZE]


def fileHead(arquivo):

    print(f"{'-'*12} Cabeçalho PCAP {'-'*12}")

    all = arquivo

    HEADER = arquivo[0]

    magic_number, major, minor, reserved1, reserved2, snaplen, linktype = struct.unpack("<IHHIIII", HEADER[:24])

    package = {
        "Magic Number": hex(magic_number),
        "Major Version": hex(major),
        "Minor Version": hex(minor),
        "Reserved 1": hex(reserved1),
        "Reserved 2": hex(reserved2),
        "Snaplen": hex(snaplen),
        "LinkType": hex(linktype)
    }

    print(package)
    recordedPackets(all)


fileHead(getFile())
