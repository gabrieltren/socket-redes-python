import socket
from decouple import config
from utils.veri_number import tam_number, par_impar_number
from utils.string_random import string_random

HOST = config("HOST", default="127.0.0.1")
PORT = config("PORT", default=55555, cast=int)


print("##################################")
print("######$$ Server Side ON $$########")
print("######$$ XXXXXXXXXXXXXX $$########")
print("##################################")
num_conn= 1
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conexao, ipinfo = s.accept()
        with conexao:
            print(f"#{num_conn}: IP: {ipinfo[0]} - PID: {ipinfo[1]}")
            num_conn +=1
            while True:
                data = conexao.recv(1024)
                if not data:
                    conexao.sendall(b"ERRO401")
                    break
                tam = tam_number(data)
                conexao.sendall(
                    string_random(tam) if tam >10 else par_impar_number(data)
                )
               
