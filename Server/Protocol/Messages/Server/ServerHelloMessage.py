from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class ServerHelloMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20100;
        self.player = player

    def encode(self):
        self.writeInt(24)
        self.writeHexa('''0A2BBCCFFFFF00AA0FEBAA''')
        self.writeHexa('''00446f6e277420747279203a29''')
        print("ServerHelloMessage sent.")