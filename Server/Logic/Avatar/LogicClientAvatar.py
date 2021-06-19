from Logic.Helpers import Helpers
from DataBase.DataBase import DataBase
class LogicClientAvatar:
    def encode(self):
        helper = Helpers(self.player)
        self.writeVInt(0)
        self.writeVInt(self.player.LowID)
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        self.writeVInt(0)
        self.writeVInt(0)
        
        if self.player.nameSet == 0:
            self.writeString("Betku")
            self.writeByte(0)
        else:
            self.writeString(self.player.name)
            self.writeByte(1)
        
        self.writeString()
        
        self.writeVInt(8) # Commodity array count
        
        self.writeVInt(24) # brawlers and resources array
        
        for x in [0, 4, 8, 12, 16, 20, 24, 28, 32, 36, 40, 44, 48, 52, 56, 60, 64, 68, 72, 95, 100]:
            self.writeDataReference(23, x)
            self.writeVInt(helper.getUnlockedBrawlers(x))
        
        self.writeDataReference(5, 1)
        self.writeVInt(self.player.brawlBoxTokens)
        
        self.writeDataReference(5, 8)
        self.writeVInt(self.player.gold)
        
        self.writeDataReference(5, 9)
        self.writeVInt(self.player.bigBoxTokens)
        
        #brawler trophies array
        self.writeVInt(21)
        for i in range(21):
            self.writeDataReference(16, i)
            self.writeVInt(helper.getTrophies(i))
        
        #brawler trophies for rank array
        self.writeVInt(21)
        for i in range(21):
            self.writeDataReference(16, i)
            self.writeVInt(helper.getTrophies(i))

        self.writeVInt(0)
        #brawler upgrade points
        self.writeVInt(21)
        for i in range(21):
            self.writeDataReference(16, i)
            self.writeVInt(helper.getPowerPoints(i))

        self.writeVInt(21)
        for i in range(21):
            self.writeDataReference(16, i)
            self.writeVInt(helper.getPowerLevel(i))
        self.writeVInt(21)
        for i in range(21):
            self.writeDataReference(16, i)
            self.writeVInt(helper.getPowerLevel(i))
        self.writeVInt(21)
        for i in [76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 99, 104]:
            self.writeDataReference(23, i)
            self.writeVInt(helper.getLockedStarPower(i))
        
        self.writeVInt(self.player.gems)
        self.writeVInt(self.player.gems)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(0)
        self.writeVInt(self.player.tutorialState)