from DataStream.ByteReader import ByteReader
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage
from Logic.Player import Player
from DataBase.DataBase import DataBase

class GoHomeMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        pass

    def process(self):
        OwnHomeDataMessage(self.client, self.player).send(self.crypto)