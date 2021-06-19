from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class StartLoadingMessage(ByteStream):
    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20559;
        self.player = player

    def encode(self):
        self.writeInt(6) #6
        self.writeInt(0)
        self.writeInt(0)
        
        self.writeInt(6) #players count
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        self.writeString("Dudnik")
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 1)
        self.writeDataReference(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(3) #Low ID
        self.writeString("Land")
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 5)
        self.writeDataReference(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(4) #Low ID
        self.writeString("Polaris")
        self.writeVInt(2)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 8)
        self.writeDataReference(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(5) #Low ID
        self.writeString("Mozhevelnik")
        self.writeVInt(4)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 0)
        self.writeDataReference(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(6) #Low ID
        self.writeString("Guest")
        self.writeVInt(5)
        self.writeVInt(1)
        self.writeVInt(0)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 9)
        self.writeDataReference(29, 0)
        self.writeByte(0)
        
        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        self.writeString("Debil")
        self.writeVInt(3)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeInt(30) #unk
        
        self.writeDataReference(16, 1)
        self.writeDataReference(29, 0)
        
        self.writeByte(0)
        
        #PLAYERS SLOT END#
        
        self.writeInt(2) #count...
        
        self.writeInt(0) #High ID
        self.writeInt(1) #Low ID
        
        self.writeInt(0) #High ID
        self.writeInt(2) #Low ID
        
        self.writeInt(1000) #unknown
        
        self.writeVInt(1)
        self.writeVInt(1) #DrawMap
        self.writeVInt(1)
        
        self.writeByte(1) #2, 39 - Spectating
        
        self.writeDataReference(15, 7)
        
        print("StartLoadingMessage sent.")