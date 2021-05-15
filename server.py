import socket

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

port = 5000 # номер порта
host = socket.gethostname() # имя хоста

server_socket.bind((host, port))
server_socket.listen(5)

def Connect():
    while True:

        user_socket, address = server_socket.accept()
        user_socket.send("You are connected!".encode("utf-8"))

Connect()

