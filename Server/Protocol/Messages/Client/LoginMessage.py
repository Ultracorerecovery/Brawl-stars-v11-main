from Protocol.Messages.Server.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.OwnHomeDataMessage import OwnHomeDataMessage

from Logic.Player import Player
from DataStream.ByteReader import ByteReader
from Logic.Helpers import Helpers
from DataBase.DataBase import DataBase

import random

class LoginMessage(ByteReader):
    def __init__(self, client, crypto, player, initial_bytes):
        super().__init__(initial_bytes)
        self.crypto = crypto
        self.client = client
        self.player = player

    def decode(self):
        self.player.HighID = self.readInt()
        self.player.LowID = self.readInt()
        self.player.Token = str(self.readString())

    def process(self):
        print(str(len(self.player.Token)))
        if len(self.player.Token) == 40:
            LoginOkMessage(self.client, self.player).send(self.crypto)
            DataBase.loadAccount(self)
            OwnHomeDataMessage(self.client, self.player).send(self.crypto)
        else:
            self.player.LowID = random.randint(0, 2147483647)
            self.player.Token = Helpers.generateToken(self)
            LoginOkMessage(self.client, self.player).send(self.crypto)
            DataBase.createAccount(self)
            OwnHomeDataMessage(self.client, self.player).send(self.crypto)