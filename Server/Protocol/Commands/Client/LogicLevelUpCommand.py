import random
from Logic.Player import Player
from Logic.Helpers import Helpers
from DataStream.ByteReader import ByteReader


class LogicLevelUpCommand(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass


    def process(self):
        pass