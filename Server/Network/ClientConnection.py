import time

from threading import *
from Crypto.NaCl import NaCl
from Protocol.LogicMessageFactory import packets
from Logic.Player import Player

class ClientConnection(Thread):
    def __init__(self, client, addr):
        super().__init__()
        self.client = client
        self.addr = addr
        self.crypto = NaCl()
        self.player = Player()

    def recvall(self, length: int):
        data = b''
        while len(data) < length:
            d = self.client.recv(length)
            if not d:
                print("ERROR! (Empty data from client!)")
                break
            data += d
        return data

    def run(self): # client processing thread
        last_packet = time.time()
        try:
            while True:
                header = self.client.recv(7)
                if len(header) > 0:
                    last_packet = time.time()
                    packet_id = int.from_bytes(header[:2], 'big')
                    length = int.from_bytes(header[2:5], 'big')
                    data = self.recvall(length)
                    pdata = self.crypto.decrypt(packet_id ,data)
                    if packet_id in packets:
                        print(f'Received packet with id: {packet_id}')
                        message = packets[packet_id](self.client, self.crypto, self.player, pdata)
                        message.decode()
                        message.process()
                    else:
                        print(f'Unhandled: {packet_id}')
                if time.time() - last_packet > 10:
                    print(f"{self.addr[0]} disconnected!")
                    self.client.close()
                    break
        except ConnectionAbortedError:
            print(f"{self.addr[0]} disconnected!")
            self.client.close()
        except ConnectionResetError:
            print(f"{self.addr[0]} disconnected!")
            self.client.close()
        except TimeoutError:
            print(f"{self.addr[0]} disconnected!")
            self.client.close()