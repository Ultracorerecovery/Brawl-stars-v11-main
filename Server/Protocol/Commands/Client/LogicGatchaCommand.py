from Logic.Player import Player
from Protocol.Messages.Server.AvailableServerCommandMessage import AvailableServerCommandMessage

from DataStream.ByteReader import ByteReader

class LogicGatchaCommand(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.crypto = crypto

    def decode(self):
        pass

    def process(self):
        AvailableServerCommandMessage(self.client, self.player, 203).send(self.crypto)