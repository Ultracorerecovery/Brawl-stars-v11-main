from Logic.Player import Player
from Protocol.LogicCommandManager import commands

from DataStream.ByteReader import ByteReader


class EndClientTurnMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.data = initial_bytes
        self.player = player
        self.client = client
        self.crypto = crypto

    def decode(self):
        self.readVInt()
        self.readVInt()
        self.readVInt()
        self.isCommand = self.readVInt()
        if self.isCommand != 0:
            self.commandID = self.readVInt()

    def process(self):
        if self.isCommand != 0:
            if self.commandID in commands:
                print("ECT Command handled: ", self.commandID)
                command = commands[self.commandID](self.client, self.crypto, self.player, self.data)
                command.decode()
                command.process()
            elif self.commandID > 0:
                print("Unhandled command: ", self.commandID)      