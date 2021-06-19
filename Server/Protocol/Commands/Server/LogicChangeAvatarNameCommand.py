from DataStream.ByteStream import ByteStream


class LogicChangeAvatarNameCommand(ByteStream):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.player = player

    def encode(self):
        self.writeVInt(201)
        self.writeString(self.player.name)
        self.writeByte(0)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(1)
        
        print("[INFO] Message LogicChangeAvatarNameCommand has been sent.")