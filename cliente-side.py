import socket
from decouple import config
from time import sleep

from utils.random_number import random_number_int

HOST = config("HOST", default="127.0.0.1")
PORT = config("PORT", default=55555, cast=int)
while True:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        str_byte = bytes(f"{random_number_int()}", "utf-8")
        s.sendall(str_byte)
        data = s.recv(1024)

    print(f"Resposta: {data.decode('utf-8')!r} - FIM")
    sleep(10)