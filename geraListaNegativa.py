import urllib
import os

#ISSO VAI NA PASTA E GERA UMA LISTA DO NOME DE TODOS OS ARQUIVOS
for file_type in['negatives']:
    for img in os.listdir(file_type):
        line = file_type+"/"+img+"\n"
        with open("negatives.txt","a") as file:
            file.write(file)