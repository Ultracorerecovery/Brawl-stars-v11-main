from Protocol.Messages.Server.VisionUpdateMessage import VisionUpdateMessage
from Protocol.Messages.Server.StartLoadingMessage import StartLoadingMessage

import time
from threading import Thread

class LogicBattle(Thread):
    def __init__(self, client, crypto, player):
        Thread.__init__(self)
        self.client = client
        self.player = player
        self.crypto = crypto
        self.subTick = 0
        self.tick = 0
        self.started = 0
    
    def run(self):
        self.startBattle()
    
    def startBattle(self):
        self.started = 1
        StartLoadingMessage(self.client, self.player).send(self.crypto)
        while self.started:
            if self.subTick >= 4:
                self.tick += 1
                self.subTick = 0
                self.player.battleTick = self.tick
                #print("Tick: ", self.tick)
            self.process()
            time.sleep(0.003)

    def process(self):
        VisionUpdateMessage(self.client, self.player).send(self.crypto)
        self.subTick += 1
