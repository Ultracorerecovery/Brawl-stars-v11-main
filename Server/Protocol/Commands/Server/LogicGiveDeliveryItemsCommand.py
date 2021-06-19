from DataStream.ByteStream import ByteStream
from Logic.Player import Player
from Logic.Helpers import Helpers
import random
from DataBase.DataBase import DataBase

class LogicGiveDeliveryItemsCommand:
    def encode(self):
        # Brawler Randomaizer:

        a = 0
        i = 0
        droppedChr = 0
        helper = Helpers(self.player)
        while a == 0 and i < 10:
            dropper = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20]
            droppedChr = random.randint(0, 20)
            if helper.getUnlockedCharacter(droppedChr) == 1:
                i += 1
            else:
                a = 1

        DataBase.replaceValue(self, 'brawlBoxTokens', self.player.brawlBoxTokens - 100)
        self.writeVInt(10)
        self.writeVInt(1) 
        self.writeVInt(0) 
        self.writeVInt(3) # reward count
        #Gold
        if self.player.boxID == 5:
            GoldValue = random.randrange(10, 100)
            DataBase.replaceValue(self, 'gold', self.player.gold + GoldValue)
        else:
            GoldValue = random.randrange(30, 150)
            DataBase.replaceValue(self, 'gold', self.player.gold + GoldValue)
        self.writeVInt(GoldValue) # reward amount
        self.writeDataReference(0, 7)
        self.writeVInt(0)


        #Brawler
        # PowerPoints
        PPValue = random.randrange(2, 19)
        PPBrawlers = random.randrange(0, 20)
        self.writeVInt(PPValue)
        self.writeDataReference(16, PPBrawlers)
        self.writeVInt(6)
        self.writeVInt(0)
        helper.addPowerPoints(PPBrawlers, PPValue)
        #Brawler
        if i < 10:
            self.writeVInt(1)
            self.writeDataReference(16, droppedChr)
            self.writeVInt(1)
            self.writeVInt(0)
            self.writeVInt(0)
            helper.UnlockBrawler(droppedChr)
        else:
            a = 0
            PP2Value = random.randrange(2, 19)
            PP2Brawlers = 0
            while a == 0:
                PP2Brawlers = random.randrange(0, 20)
                if PP2Brawlers == PPBrawlers:
                    pass
                else:
                    a = 1
            self.writeVInt(PP2Value)
            self.writeDataReference(16, PP2Brawlers)
            self.writeVInt(6)
            self.writeVInt(0)
            helper.addPowerPoints(PP2Brawlers, PP2Value)

        for x in range(8):
            self.writeVInt(x)
        
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)
        self.writeVInt(1)