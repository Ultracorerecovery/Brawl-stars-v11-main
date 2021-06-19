from DataStream.ByteReader import ByteReader
from Protocol.Messages.Server.ServerHelloMessage import ServerHelloMessage
from Logic.Player import Player

class ClientHelloMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.crypto = crypto
        self.player = player

    def decode(self):
        pass #TODO: Decode this stuff

    def process(self):
        ServerHelloMessage(self.client, self.player).send(self.crypto)