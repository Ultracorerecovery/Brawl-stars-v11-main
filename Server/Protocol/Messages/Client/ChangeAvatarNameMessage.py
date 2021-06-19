from random import choice
from string import ascii_uppercase
import json

from Logic.Player import Player
from Protocol.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from DataBase.DataBase import DataBase

from DataStream.ByteReader import ByteReader


class ChangeAvatarNameMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.crypto = crypto

    def decode(self):
        self.player.name = self.readString()

    def process(self):
        DataBase.replaceValue(self, 'name', self.player.name)
        self.player.nameSet = 1
        DataBase.replaceValue(self, 'nameSet', self.player.nameSet)
        LogicChangeAvatarNameCommand(self.client, self.player).send(self.crypto)