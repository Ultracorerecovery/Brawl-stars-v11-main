from DataStream.ByteStream import ByteStream
from Logic.Player import Player

class LogicDiamondsAddedCommand:
    def encode(self):
        self.writeByte(0)
        self.writeInt(80) #gems count
        self.writeInt(0)
        self.writeInt(0)
        self.writeString("G:0") #transaction ID
        
        self.writeVInt(0) #sub_19A63C