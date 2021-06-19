from DataStream.ByteReader import ByteReader
from Logic.Player import Player
from Logic.Battle.LogicBattle import LogicBattle

from threading import Thread

class StartGameMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        pass

    def process(self):
        battle = LogicBattle(self.client, self.crypto, self.player)
        battle.start()