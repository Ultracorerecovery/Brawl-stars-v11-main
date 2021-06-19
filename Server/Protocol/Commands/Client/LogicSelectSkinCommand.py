import random
from Logic.Player import Player
from Logic.Helpers import Helpers
from DataStream.ByteReader import ByteReader


class LogicSelectSkinCommand(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.skinID = self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.player.brawlerID = self.readVInt()


    def process(self):
        Helpers.changeSelectSkin(self, self.player.brawlerID, self.player.skinID)