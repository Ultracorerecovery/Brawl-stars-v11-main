from DataStream.ByteReader import ByteReader
from Protocol.Messages.Server.BattleEndMessage import BattleEndMessage
from Protocol.Messages.Server.BattleEnd2Message import BattleEnd2Message

class AskForBattleEndMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.crypto = crypto
    
    def decode(self):
        self.player.battle_result = self.readVInt()
        self.readVInt()
        self.player.rank = self.readVInt()
        
        self.readVInt()
        self.readVInt()
        
        self.readVInt() #players count
        
        self.readVInt() #16
        self.player.selectedBrawler = self.readVInt()
        self.readVInt() #null dataref
        self.player_team = self.readVInt()
        self.readVInt() #boolean
        self.readString() #name
        
        self.readVInt()
        self.player.bot1 = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.bot1n = str(self.readString())
        
        self.readVInt()
        self.player.bot2 = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.bot2n = str(self.readString())
        
        self.readVInt()
        self.player.bot3 = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.bot3n = str(self.readString())
        
        self.readVInt()
        self.player.bot4 = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.bot4n = str(self.readString())
        
        self.readVInt()
        self.player.bot5 = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.bot5n = str(self.readString())
    
    def process(self):
        if self.player.rank != 0:
            BattleEndMessage(self.client, self.player).send(self.crypto)
        else:
            BattleEnd2Message(self.client, self.player).send(self.crypto)