import socket

from Network.ClientConnection import ClientConnection

class Server:
    def __init__(self):
        self.server = socket.socket()
        self.listening = True

    def start(self):
        self.server.bind(('0.0.0.0', 9339)) #ServerSocket bind
        print('Server started!')
        while self.listening:
            self.server.listen()
            client, addr = self.server.accept()
            print(f'New connection from {addr[0]}')
            ClientConnection(client, addr).start()