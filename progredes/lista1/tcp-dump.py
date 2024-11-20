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
        bytes_array.append(struct.unpack("I", section[byte:byte+4])[0])

    array_to_hex = hex(sum(bytes_array))
    return array_to_hex


def fileHead(arquivo):

    package = {}

    HEADER = arquivo[0]
    print(HEADER)

    # Auxiliar variables to translations and paddings

    ma_v = HEADER[4:6]
    mi_v = HEADER[6:8]
    majorVersion = ma_v.rjust(4, b'\x00')
    minorVersion = mi_v.rjust(4, b'\x00')

    Reserved1 = HEADER[8:40]
    Reserved2 = HEADER[40:72]

    SnapLen = HEADER[72:104]  # 32 bits
    LinkType = HEADER[104:120]  # 16 bits

    package["Magic Number"] = hex(struct.unpack("I", HEADER[:4])[0])  # Little-endian

    # Checking if the application is reading a PCAP file
    if package["Magic Number"] != MAGIC1:
        sys.exit("Arquivo não PCAP")

    # Building the Header sector
    package["Major Version"] = hex(struct.unpack("I", majorVersion)[0])
    package["Minor Version"] = hex(struct.unpack("I", minorVersion)[0])

    package["Reserved1"] = unpackBits(Reserved1)
    package["Reserved2"] = unpackBits(Reserved2)

    package["SnapLen"] = unpackBits(SnapLen)
    package["LinkType"] = unpackBits(LinkType)
    print(len(Reserved2))


fileHead(getFile())



"""     print(temp_LinkType)

    for byte in range(0, len(temp_SnapLen), 4):
        SnapLen_aux.append(struct.unpack("I", temp_SnapLen[byte:byte+4])[0])
    package["SnapLen"] = hex(sum(SnapLen_aux))  # SnapLen_to_hex

    for byte in range(0, len(temp_LinkType), 4):
        LinkType_aux.append(struct.unpack("I", temp_LinkType[byte:byte+4])[0])

    package["LinkType"] = hex(sum(LinkType_aux))
 """
