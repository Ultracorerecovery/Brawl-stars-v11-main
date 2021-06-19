from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class LoginOkMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20104
        self.version = 1
        self.player = player;

    def encode(self):
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        self.writeInt(self.player.HighID)
        self.writeInt(self.player.LowID)
        
        self.writeString(self.player.Token)
        self.writeString()
        self.writeString()
        
        self.writeInt(11)
        self.writeInt(112)
        self.writeInt(1)
        
        self.writeString("integration")
        
        self.writeInt(0) #1
        self.writeInt(0) #1
        self.writeInt(0) #61
        
        self.writeString()
        
        #isAtEnd
        
        self.writeString()
        self.writeString()
        
        #isAtEnd
        
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        self.writeInt(0)
        self.writeString()
        self.writeString()
        self.writeString()
        
        #isAtEnd
        
        self.writeVInt(0)
        
        #isAtEnd
        
        #TODO: stringReference
        print("[INFO] Message LoginOkMessage has been sent.")