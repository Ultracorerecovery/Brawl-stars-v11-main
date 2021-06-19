from DataStream.ByteStream import ByteStream
from Logic.Player import Player
from Logic.Home.LogicClientHome import LogicClientHome
from Logic.Avatar.LogicClientAvatar import LogicClientAvatar

class OwnHomeDataMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        LogicClientHome.encode(self)
        LogicClientAvatar.encode(self)
        #self.writeHexa('''08031700010501a1010508a4010000020501a1010508a4010000000110000200000100000000000000028192f5b20b''')
        self.writeVInt(10)
        print("[INFO] Message OHD has been sent.")