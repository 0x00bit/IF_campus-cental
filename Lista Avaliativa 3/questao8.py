import subprocess

#trCMD = 'tracert -d4 www.uol.com'
caminho = subprocess.run (strCMD, capture_output=True).stdout.decode('latin1')

with open("rastreio.txt", "w", encoding="utf-8") as file:
    file.write(caminho)

