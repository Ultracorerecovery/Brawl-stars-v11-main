from DataStream.ByteReader import ByteReader
from Logic.Player import Player
from Protocol.Messages.Server.BattleEndMessage import BattleEndMessage
from Protocol.Messages.Server.KeepAliveServerMessage import KeepAliveServerMessage

import time

class ClientInputMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        self.readVInt() #0
        self.readVInt() #unknown 16, 33, 34
        self.readVInt() #Count
        v3 = self.readVInt()
        result = self.sub_3A9EC(v3, 0, 30)
        print(str(result))
        #("ClientInput: Tick: ", self.tick)
    
    def sub_3A9EC(self, a1, a2, a3):
        if a1 < a3:
            a3 = a1
        if a1 <= a2:
            a3 = a2
        return a3

    def process(self):
        pass
        '''ticking = 0
        while True:
            if ticking >= 4:
                self.player.battleTick += 1
                KeepAliveServerMessage(self.client, self.player).send(self.crypto)
                ticking = 0
            
            
            VisionUpdateMessage(self.client, self.player).send(self.crypto)
            time.sleep(0.03)
            ticking += 1'''