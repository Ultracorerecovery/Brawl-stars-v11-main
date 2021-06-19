from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class KeepAliveServerMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20108;
        self.player = player

    def encode(self):
        print("KeepAliveServer sent.")