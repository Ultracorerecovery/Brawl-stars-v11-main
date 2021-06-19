from DataStream.ByteStream import ByteStream
from Logic.Player import Player
from Protocol.ServerCommandsFactory import commands

class AvailableServerCommandMessage(ByteStream):
    def __init__(self, client, player, commandID):
        super().__init__(client)
        self.id = 24111;
        self.player = player
        self.commandID = commandID

    def encode(self):
        if self.commandID in commands:
            self.writeVInt(self.commandID)
            commands[self.commandID].encode(self)
        else:
            print("Unable to create server command: ", self.commandID)