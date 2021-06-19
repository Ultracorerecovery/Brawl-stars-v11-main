from DataStream.ByteReader import ByteReader
from Protocol.Messages.Server.KeepAliveServerMessage import KeepAliveServerMessage
from Logic.Player import Player
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

class KeepAliveMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        pass

    def process(self):
        KeepAliveServerMessage(self.client, self.player).send(self.crypto)