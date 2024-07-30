import sys

# Alfabeto
ALPHABET = "abcdefghijklmnopqrstuvwxyz"

# Menu
print("""
                                                                                
                                                                                
                           .*(((#%&&%%&##(#,/&#*,                               
                       (@@@@&@&@%%#%((/**/&%@&##&%%%@&&.                        
                    (@@@&&&#&(*## ,.(/.(,@#*/&&&/&/,*/%@%%#                     
                  &@@&%(@#&@%(*/%%@%/*(%(//(*/*//##&&@%((#&&%%.                 
                @@@#*//,..,,***,,..     .     .,,*,,.*%@@#@(%#%@.               
              #@@@&((*,.     .*,..                ..,.,(%&&&&*&%((              
             #@@@#*//,,     ....                   .,*.,#@&#&(**&(/,            
            #@@@@%(/(*. ...,,*,..                .  ,**/@&&(.%**#%#*            
           *@@@@#*/(//,*.  *((*,,.                 .,*#&&/(//.*/#%%&            
           %@@@@%&&%/*,..,*,/#/,,..            ....,,/&%&(@&/,,(&#@%,           
           @@@@#///**,*/**/(##/*,               ..,*,./%%&&%&#*##@&@*           
           @@@@#**. *%#/*(@@%,             .,*.. *,,,../@@(%%@%(@#@&            
          *@@&@@@@#,.,*,(/*%@&@@@@@@@@@@@%.   ,*,*..,**&@@@&@@#@@@@/            
          %@@@&@&&@@@%((%##(&&&@@@@&@&@&*  *#, ..,.  ..&@@@@@@@%*,&             
          .@@@@@&&@@@&#,*(&@@@@@&@@@@&&# /(  .,       ,#&@@@@(.&,##,            
           (&@@@@@&@&@%&./%@@#&@@@@@@@@%*#%**#&#.    ..*&@%,,&@/ *%,            
           ,@@@(**,*#@(, ./@&(@/(#(&&#. *#((/.       .,(&(, ,@@@, ,             
           ,@@&@@%%%@%*   ,*%*.* (@@&#/..((,       . /@@&@*  ##(                
           ,@&(*..%@@#   ...*/.  .,(&%(,.         ..*(@&,%./(  /(               
           .@@#/*%@@%*   /*,  .   **.           ...  /&&#&(. ,,                 
           *@@@%#@@%/   ,#&((#.  .*/(/     ...*.,.  .#(%@@@@@*                  
           ,@@@#,&@((.  ,((**#@#    ,(&%(/((/.    ..**/&/&@@//*                 
           (@@&/(@@@@@@&@@@@@(,%@(    .,/**,., ./**. .((.%@@,/@                 
          *@@@#&%@@@@@@@@%&@((/, (@&*   ,%/,*//##. ,,&# ,@# .@@,                
          @@&(&%&#*#(%@@@##*./,*&# ,%/   .,*@@%,   ,&@/(*  .#((*                
         .@@&@@@@@#@@@(%@@%@@&%/ .(#/&(  ./#/.   .#(&(.  ,//.,.                 
         ,&@%@@@@@(*/&&/..    .&&*(##/(  *%&(,.*(&@#   .//* /&                  
          %@%&&@&@@#(&@(*,      %@@@&*  ..   (/%@#, ,%#* .*&@@&.                
           @@@@(/@@%&# ,..  ..   *(@&#... .*#@@% *,#&,..,@@@@@%@.               
           (@&@&#,*/##*/...,.    //,#/*&#*#@#* .(%#*..(@@@@@@@*&@#              
           /@@@@@/., .,.        ,,,**%&@@#,   ./##,.&@@@@@@@@& %.@.             
          (@@#@@@@(/,,      . .//(%%@#/  ../..,.,(@@@@@%@@@@&* /*&@(            
       .&@@@@@/,*@@%%(*/(*(##&&@&(.   .((,   ,%@@@@@@#@&@&@&( ..#@@&%&/         
     (@@&&@@@@@(.  .#@@@@@@&%/     ./%&*  .#&@@@@@@@@&*,*@/*   ..&&#,,,(%,      
 .%@@@@@&@#@@@@@#&#..%@@.,     .**,*&,.(@@@@@@@@@@%/***%@((  .,./..*#/.   *%*   
@@@@@@@%&@#@@@@@&@@%&@@*&. .,**.,.*%@@@@@@@@&@/*(*,.,*&@/%.  .,/     .,*.   /#@*
@@@@@@@(#@@@@@@@@@%&@@@@@&,,,,*%@@@@@@@@@#/*///,/,***@@%%.  ....       ,*/     *
&@@@@@@(&&@@@@@@@@@&@@@@@@#@@@@@@&%%((#%(*//(*#*/(,#@@#%. *. (*          ,//.   
&@@@@@&/&@@@@@@@@@@@@@#@@@@@&(%%####(##(#&#//,*///%@@&& .,*.*%,           .,/(, 
@@@@@@/*&&@@@@@@@@@@@@@,@@@@%#%&&##%%#####%/*/**/%@%%#./ (.%(*,,,.           ,/%
@&@@@@@(@&@@@@@@@@@@(%@@@@@%@&@%%%#(%%%##((#((##@@&%.( .(.&#(((/,*.            ,
@@@@@@@%&(@@@@@@@@@@@@&@@&&&&%#%##%(#%###(((%@&@&%..(./,&&#/*%/(&/..          ,/

[1]: Crypt message
[2]: Decrypt message
[0]: Exit    
""")

choice = input("> ")

if choice == "1":
    message = input("Digite sua mensagem: ")
    key = input("Digite sua chave: ")
    
    encrypted_message = ""
    key_index = 0
    
    for char in message:
        if char.isalpha():
            # Obter o valor numérico da chave e da mensagem
            message_value = ord(char.upper()) - ord('A')
            key_value = ord(key[key_index % len(key)].upper()) - ord('A')
            
            # Calcular o novo caractere criptografado
            new_value = (message_value + key_value) % 26
            new_char = chr(new_value + ord('A'))
            
            encrypted_message += new_char
            key_index += 1
        else:
            encrypted_message += char
    
    print(f"Mensagem criptografada: {encrypted_message}")

elif choice == "2":
    encrypted_message = input("Digite sua mensagem criptografada: ")
    key = input("Digite sua chave: ")
    
    decrypted_message = ""
    key_index = 0
    
    for char in encrypted_message:
        if char.isalpha():
            # Obter o valor numérico da chave e da mensagem criptografada
            encrypted_value = ord(char.upper()) - ord('A')
            key_value = ord(key[key_index % len(key)].upper()) - ord('A')
            
            # Calcular o novo caractere descriptografado
            new_value = (encrypted_value - key_value + 26) % 26
            new_char = chr(new_value + ord('A'))
            
            decrypted_message += new_char
            key_index += 1
        else:
            decrypted_message += char
    
    print(f"Mensagem descriptografada: {decrypted_message}")

elif choice == "0":
    sys.exit()

else:
    print("Escolha inválida. Saindo.")
