import sys

def sanitize_input(user_input):
    """
    Fuction responsible to sanitize the user input and check if it is a 
    valid IP Address or Mask
    """

    sanitized = []  # Sanitized return

    """
    If the characters on IP Address are letters or symbols, then,
    discart them and return a exception for user
    """

    block = ""
    for character in user_input:
        
        # Temporary variable to add a block of decimal numbers on return

        if character.isdigit() == True:
            block += character
        elif character == ".":
            block += "."
        elif character == "/":
            block += ""
        else:
            sys.exit("Endereço IP ou mascára de rede inválidos!")
    
    return block


def net_address(ip, mask):
    """
    Function which calculates the net address
    """   

    net_address = ""
    padding_s = ""

    padding = 32 - len(mask)
    for _ in range(padding):
        padding_s += "1"

    mask = padding_s + mask
    print(f"net mask: {mask}")

    for i, j in zip(ip, mask):
        sum = int(i) & int(j)
        net_address += str(sum)

    """
    Needs to convert binary IP to decimal IP Address
    """

    print(net_address)
    return net_address


def gen_cidr(cidr):
    bin_mask = ""

    for _ in range(int(cidr)):
        bin_mask += "0"
    
    return bin_mask


def ip_to_bin(ip):
    ip_bin = ""

    aux = ip.split(".")
    for i in aux:
        aux2 = ""
        aux3 = ""
        aux2 += bin(int(i))[2:]
        if len(aux2) == 8:
            ip_bin += aux2
        else:
            a = 8 - len(aux2)
            for _ in range(a):
                aux3 += "0"
            ip_bin += aux3+aux2

    return ip_bin


# Getting info from user
def get_ip():
    """
    Function responsible to get the input of user
    """

    texts = [
        "Insira o endereço IP: ",
        "Insira a máscara de rede inicial: ",
        "Insira a máscara de rede final: "
    ]

    user_input = {"ip":"",
                  "cidr_i":"",
                  "cidr_f":"",
                  "cidr_i_bin":"",
                  "cidr_f_bin":"",
                  "ip_bin":"",
                  "ip_net_address":""  
                  } # Sanitized user input
    
    i = 0
    for i in range(3):
        if i == 0:
            a = input(texts[i])
            user_input["ip"] = sanitize_input(a)
        elif i == 1:
            a = input(texts[i])
            user_input["cidr_i"] = sanitize_input(a)
        elif i == 2:
            a = input(texts[i])
            user_input["cidr_f"] = sanitize_input(a)
        else:
            sys.exit("IP ou CIDR inválidos!")
        
        i+=1

    user_input["cidr_i_bin"] = gen_cidr(int(user_input["cidr_i"]))
    user_input["cidr_f_bin"] = gen_cidr(int(user_input["cidr_f"]))
    user_input["ip_bin"] = ip_to_bin(user_input["ip"])

    print(user_input)

    net_address(user_input["ip_bin"], user_input["cidr_i_bin"])

get_ip()