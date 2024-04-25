
# pip install requests

import requests

ler = requests.get("https://wiki.sj.ifsc.edu.br/images/4/4a/Ecoshower.txt")

# print(ler)


with open("arquivo2.txt", "wb") as arquivo:
    arquivo.write(ler.content)

