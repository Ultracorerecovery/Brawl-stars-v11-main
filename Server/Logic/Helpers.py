import string
import random

from DataBase.DataBase import DataBase
from Logic.Player import Player

class Helpers:

    def __init__(self, player):
        self.player = player
    
    def generateToken(self):
        lettersAndDigits = string.ascii_letters + string.digits
        return ''.join(random.choice(lettersAndDigits) for i in range(40))

    def addTrophies(self, brawler, count):
        if brawler == 0:
            self.player.shellyScore += count
            DataBase.replaceValue(self, 'shellyScore', self.player.shellyScore)
        elif brawler == 1:
            self.player.coltScore += count
            DataBase.replaceValue(self, 'coltScore', self.player.coltScore)
        elif brawler == 2:
            self.player.bullScore += count
            DataBase.replaceValue(self, 'bullScore', self.player.bullScore)
        elif brawler == 3:
            self.player.brockScore += count
            DataBase.replaceValue(self, 'brockScore', self.player.brockScore)
        elif brawler == 4:
            self.player.ricoScore += count
            DataBase.replaceValue(self, 'ricoScore', self.player.ricoScore)
        elif brawler == 5:
            self.player.spikeScore += count
            DataBase.replaceValue(self, 'spikeScore', self.player.spikeScore)
        elif brawler == 6:
            self.player.barleyScore += count
            DataBase.replaceValue(self, 'barleyScore', self.player.barleyScore)
        elif brawler == 7:
            self.player.jessieScore += count
            DataBase.replaceValue(self, 'jessieScore', self.player.jessieScore)
        elif brawler == 8:
            self.player.nitaScore += count
            DataBase.replaceValue(self, 'nitaScore', self.player.nitaScore)
        elif brawler == 9:
            self.player.dynamikeScore += count
            DataBase.replaceValue(self, 'dynamikeScore', self.player.dynamikeScore)
        elif brawler == 10:
            self.player.elprimoScore += count
            DataBase.replaceValue(self, 'elprimoScore', self.player.elprimoScore)
        elif brawler == 11:
            self.player.mortisScore += count
            DataBase.replaceValue(self, 'mortisScore', self.player.mortisScore)
        elif brawler == 12:
            self.player.crowScore += count
            DataBase.replaceValue(self, 'crowScore', self.player.crowScore)
        elif brawler == 13:
            self.player.pocoScore += count
            DataBase.replaceValue(self, 'pocoScore', self.player.pocoScore)
        elif brawler == 14:
            self.player.boScore += count
            DataBase.replaceValue(self, 'boScore', self.player.boScore)
        elif brawler == 15:
            self.player.piperScore += count
            DataBase.replaceValue(self, 'piperScore', self.player.piperScore)
        elif brawler == 16:
            self.player.pamScore += count
            DataBase.replaceValue(self, 'pamScore', self.player.pamScore)
        elif brawler == 17:
            self.player.taraScore += count
            DataBase.replaceValue(self, 'taraScore', self.player.taraScore)
        elif brawler == 18:
            self.player.darrylScore += count
            DataBase.replaceValue(self, 'darrylScore', self.player.darrylScore)
        elif brawler == 19:
            self.player.pennyScore += count
            DataBase.replaceValue(self, 'pennyScore', self.player.pennyScore)
        elif brawler == 20:
            self.player.frankScore += count
            DataBase.replaceValue(self, 'frankScore', self.player.frankScore)
        
        self.player.trophies += count
        DataBase.replaceValue(self, 'trophies', self.player.trophies)

    def getTrophies(self, brawler):
        if brawler == 0:
            return self.player.shellyScore
        elif brawler == 1:
            return self.player.coltScore
        elif brawler == 2:
            return self.player.bullScore
        elif brawler == 3:
            return self.player.brockScore
        elif brawler == 4:
            return self.player.ricoScore
        elif brawler == 5:
            return self.player.spikeScore
        elif brawler == 6:
            return self.player.barleyScore
        elif brawler == 7:
            return self.player.jessieScore
        elif brawler == 8:
            return self.player.nitaScore
        elif brawler == 9:
            return self.player.dynamikeScore
        elif brawler == 10:
            return self.player.elprimoScore
        elif brawler == 11:
            return self.player.mortisScore
        elif brawler == 12:
            return self.player.crowScore
        elif brawler == 13:
            return self.player.pocoScore
        elif brawler == 14:
            return self.player.boScore
        elif brawler == 15:
            return self.player.piperScore
        elif brawler == 16:
            return self.player.pamScore
        elif brawler == 17:
            return self.player.taraScore
        elif brawler == 18:
            return self.player.darrylScore
        elif brawler == 19:
            return self.player.pennyScore
        elif brawler == 20:
            return self.player.frankScore

    def getSkinID(self, brawler):
        if brawler == 0:
            return 0
        elif brawler == 1:
            return 1
        elif brawler == 2:
            return 3
        elif brawler == 3:
            return 4
        elif brawler == 4:
            return 9
        elif brawler == 5:
            return 10
        elif brawler == 6:
            return 12
        elif brawler == 7:
            return 13
        elif brawler == 8:
            return 14
        elif brawler == 9:
            return 6
        elif brawler == 10:
            return 7
        elif brawler == 11:
            return 18
        elif brawler == 12:
            return 19
        elif brawler == 13:
            return 21
        elif brawler == 14:
            return 22
        elif brawler == 15:
            return 23
        elif brawler == 16:
            return 24
        elif brawler == 17:
            return 32
        elif brawler == 18:
            return 34
        elif brawler == 19:
            return 41
        elif brawler == 20:
            return 42

    def getPowerLevel(self, brawler):
        if brawler == 0:
            return self.player.shellyLVL
        elif brawler == 1:
            return self.player.coltLVL
        elif brawler == 2:
            return self.player.bullLVL
        elif brawler == 3:
            return self.player.brockLVL
        elif brawler == 4:
            return self.player.ricoLVL
        elif brawler == 5:
            return self.player.spikeLVL
        elif brawler == 6:
            return self.player.barleyLVL
        elif brawler == 7:
            return self.player.jessieLVL
        elif brawler == 8:
            return self.player.nitaLVL
        elif brawler == 9:
            return self.player.dynamikeLVL
        elif brawler == 10:
            return self.player.elprimoLVL
        elif brawler == 11:
            return self.player.mortisLVL
        elif brawler == 12:
            return self.player.crowLVL
        elif brawler == 13:
            return self.player.pocoLVL
        elif brawler == 14:
            return self.player.boLVL
        elif brawler == 15:
            return self.player.piperLVL
        elif brawler == 16:
            return self.player.pamLVL
        elif brawler == 17:
            return self.player.taraLVL
        elif brawler == 18:
            return self.player.darrylLVL
        elif brawler == 19:
            return self.player.pennyLVL
        elif brawler == 20:
            return self.player.frankLVL

    def getPowerPoints(self, brawler):
        if brawler == 0:
            return self.player.shellyPP
        elif brawler == 1:
            return self.player.coltPP
        elif brawler == 2:
            return self.player.bullPP
        elif brawler == 3:
            return self.player.brockPP
        elif brawler == 4:
            return self.player.ricoPP
        elif brawler == 5:
            return self.player.spikePP
        elif brawler == 6:
            return self.player.barleyPP
        elif brawler == 7:
            return self.player.jessiePP
        elif brawler == 8:
            return self.player.nitaPP
        elif brawler == 9:
            return self.player.dynamikePP
        elif brawler == 10:
            return self.player.elprimoPP
        elif brawler == 11:
            return self.player.mortisPP
        elif brawler == 12:
            return self.player.crowPP
        elif brawler == 13:
            return self.player.pocoPP
        elif brawler == 14:
            return self.player.boPP
        elif brawler == 15:
            return self.player.piperPP
        elif brawler == 16:
            return self.player.pamPP
        elif brawler == 17:
            return self.player.taraPP
        elif brawler == 18:
            return self.player.darrylPP
        elif brawler == 19:
            return self.player.pennyPP
        elif brawler == 20:
            return self.player.frankPP

    def addPowerPoints(self, brawler, count):
        if brawler == 0:
            self.player.shellyPP += count
            DataBase.replaceValue(self, 'shellyPP', self.player.shellyPP)
        elif brawler == 1:
            self.player.coltPP += count
            DataBase.replaceValue(self, 'coltPP', self.player.coltPP)
        elif brawler == 2:
            self.player.bullPP += count
            DataBase.replaceValue(self, 'bullPP', self.player.bullPP)
        elif brawler == 3:
            self.player.brockPP += count
            DataBase.replaceValue(self, 'brockPP', self.player.brockPP)
        elif brawler == 4:
            self.player.ricoPP += count
            DataBase.replaceValue(self, 'ricoPP', self.player.ricoPP)
        elif brawler == 5:
            self.player.spikePP += count
            DataBase.replaceValue(self, 'spikePP', self.player.spikePP)
        elif brawler == 6:
            self.player.barleyPP += count
            DataBase.replaceValue(self, 'barleyPP', self.player.barleyPP)
        elif brawler == 7:
            self.player.jessiePP += count
            DataBase.replaceValue(self, 'jessiePP', self.player.jessiePP)
        elif brawler == 8:
            self.player.nitaPP += count
            DataBase.replaceValue(self, 'nitaPP', self.player.nitaPP)
        elif brawler == 9:
            self.player.dynamikePP += count
            DataBase.replaceValue(self, 'dynamikePP', self.player.dynamikePP)
        elif brawler == 10:
            self.player.elprimoPP += count
            DataBase.replaceValue(self, 'elprimoPP', self.player.elprimoPP)
        elif brawler == 11:
            self.player.mortisPP += count
            DataBase.replaceValue(self, 'mortisPP', self.player.mortisPP)
        elif brawler == 12:
            self.player.crowPP += count
            DataBase.replaceValue(self, 'crowPP', self.player.crowPP)
        elif brawler == 13:
            self.player.pocoPP += count
            DataBase.replaceValue(self, 'pocoPP', self.player.pocoPP)
        elif brawler == 14:
            self.player.boPP += count
            DataBase.replaceValue(self, 'boPP', self.player.boPP)
        elif brawler == 15:
            self.player.piperPP += count
            DataBase.replaceValue(self, 'piperPP', self.player.piperPP)
        elif brawler == 16:
            self.player.pamPP += count
            DataBase.replaceValue(self, 'pamPP', self.player.pamPP)
        elif brawler == 17:
            self.player.taraPP += count
            DataBase.replaceValue(self, 'taraPP', self.player.taraPP)
        elif brawler == 18:
            self.player.darrylPP += count
            DataBase.replaceValue(self, 'darrylPP', self.player.darrylPP)
        elif brawler == 19:
            self.player.pennyPP += count
            DataBase.replaceValue(self, 'pennyPP', self.player.pennyPP)
        elif brawler == 20:
            self.player.frankPP += count
            DataBase.replaceValue(self, 'frankPP', self.player.frankPP)

    def getPowerPoints(self, brawler):
        if brawler  == 0:
            return self.player.shellyPP
        elif brawler == 1:
            return self.player.coltPP
        elif brawler == 2:
            return self.player.bullPP
        elif brawler == 3:
            return self.player.brockPP
        elif brawler == 4:
            return self.player.ricoPP
        elif brawler == 5:
            return self.player.spikePP
        elif brawler == 6:
            return self.player.barleyPP
        elif brawler == 7:
            return self.player.jessiePP
        elif brawler == 8:
            return self.player.nitaPP
        elif brawler == 9:
            return self.player.dynamikePP
        elif brawler == 10:
            return self.player.elprimoPP
        elif brawler == 11:
            return self.player.mortisPP
        elif brawler == 12:
            return self.player.crowPP
        elif brawler == 13:
            return self.player.pocoPP
        elif brawler == 14:
            return self.player.boPP
        elif brawler == 15:
            return self.player.piperPP
        elif brawler == 16:
            return self.player.pamPP
        elif brawler == 17:
            return self.player.taraPP
        elif brawler == 18:
            return self.player.darrylPP
        elif brawler == 19:
            return self.player.pennyPP
        elif brawler == 20:
            return self.player.frankPP

    def getUnlockedBrawlers(self, cardID):
        if cardID == 0:
            return self.player.shellyUnlock
        elif cardID == 4:
            return self.player.coltUnlock
        elif cardID == 8:
            return self.player.bullUnlock
        elif cardID == 12:
            return self.player.brockUnlock
        elif cardID == 16:
            return self.player.ricoUnlock
        elif cardID == 20:
            return self.player.spikeUnlock
        elif cardID == 24:
            return self.player.barleyUnlock
        elif cardID == 28:
            return self.player.jessieUnlock
        elif cardID == 32:
            return self.player.nitaUnlock
        elif cardID == 36:
            return self.player.dynamikeUnlock
        elif cardID == 40:
            return self.player.elprimoUnlock
        elif cardID == 44:
            return self.player.mortisUnlock
        elif cardID == 48:
            return self.player.crowUnlock
        elif cardID == 52:
            return self.player.pocoUnlock
        elif cardID == 56:
            return self.player.boUnlock
        elif cardID == 60:
            return self.player.piperUnlock
        elif cardID == 64:
            return self.player.pamUnlock
        elif cardID == 68:
            return self.player.taraUnlock
        elif cardID == 72:
            return self.player.darrylUnlock
        elif cardID == 95:
            return self.player.pennyUnlock
        elif cardID == 100:
            return self.player.frankUnlock

    def UnlockBrawler(self, brawler):
        if brawler == 0:
            self.player.shellyUnlock = 1
            DataBase.replaceValue(self, 'shellyUnlock', self.player.shellyUnlock)
        elif brawler == 1:
            self.player.coltUnlock = 1
            DataBase.replaceValue(self, 'coltUnlock', self.player.coltUnlock)
        elif brawler == 2:
            self.player.bullUnlock = 1
            DataBase.replaceValue(self, 'bullUnlock', self.player.bullUnlock)
        elif brawler == 3:
            self.player.brockUnlock = 1
            DataBase.replaceValue(self, 'brockUnlock', self.player.brockUnlock)
        elif brawler == 4:
            self.player.ricoUnlock = 1
            DataBase.replaceValue(self, 'ricoUnlock', self.player.ricoUnlock)
        elif brawler == 5:
            self.player.spikeUnlock = 1
            DataBase.replaceValue(self, 'spikeUnlock', self.player.spikeUnlock)
        elif brawler == 6:
            self.player.barleyUnlock = 1
            DataBase.replaceValue(self, 'barleyUnlock', self.player.barleyUnlock)
        elif brawler == 7:
            self.player.jessieUnlock = 1
            DataBase.replaceValue(self, 'jessieUnlock', self.player.jessieUnlock)
        elif brawler == 8:
            self.player.nitaUnlock = 1
            DataBase.replaceValue(self, 'nitaUnlock', self.player.nitaUnlock)
        elif brawler == 9:
            self.player.dynamikeUnlock = 1
            DataBase.replaceValue(self, 'dynamikeUnlock', self.player.dynamikeUnlock)
        elif brawler == 10:
            self.player.elprimoUnlock = 1
            DataBase.replaceValue(self, 'elprimoUnlock', self.player.elprimoUnlock)
        elif brawler == 11:
            self.player.mortisUnlock = 1
            DataBase.replaceValue(self, 'mortisUnlock', self.player.mortisUnlock)
        elif brawler == 12:
            self.player.crowUnlock = 1
            DataBase.replaceValue(self, 'crowUnlock', self.player.crowUnlock)
        elif brawler == 13:
            self.player.pocoUnlock = 1
            DataBase.replaceValue(self, 'pocoUnlock', self.player.pocoUnlock)
        elif brawler == 14:
            self.player.boUnlock = 1
            DataBase.replaceValue(self, 'boUnlock', self.player.boUnlock)
        elif brawler == 15:
            self.player.piperUnlock = 1
            DataBase.replaceValue(self, 'piperUnlock', self.player.piperUnlock)
        elif brawler == 16:
            self.player.pamUnlock = 1
            DataBase.replaceValue(self, 'pamUnlock', self.player.pamUnlock)
        elif brawler == 17:
            self.player.taraUnlock = 1
            DataBase.replaceValue(self, 'taraUnlock', self.player.taraUnlock)
        elif brawler == 18:
            self.player.darrylUnlock = 1
            DataBase.replaceValue(self, 'darrylUnlock', self.player.darrylUnlock)
        elif brawler == 19:
            self.player.pennyUnlock = 1
            DataBase.replaceValue(self, 'pennyUnlock', self.player.pennyUnlock)
        elif brawler == 20:
            self.player.frankUnlock = 1
            DataBase.replaceValue(self, 'frankUnlock', self.player.frankUnlock)
        
    def getUnlockedCharacter(self, brawler):
        if brawler == 0:
            return self.player.shellyUnlock
        elif brawler == 1:
            return self.player.coltUnlock
        elif brawler == 2:
            return self.player.bullUnlock
        elif brawler == 3:
            return self.player.brockUnlock
        elif brawler == 4:
            return self.player.ricoUnlock
        elif brawler == 5:
            return self.player.spikeUnlock
        elif brawler == 6:
            return self.player.barleyUnlock
        elif brawler == 7:
            return self.player.jessieUnlock
        elif brawler == 8:
            return self.player.nitaUnlock
        elif brawler == 9:
            return self.player.dynamikeUnlock
        elif brawler == 10:
            return self.player.elprimoUnlock
        elif brawler == 11:
            return self.player.mortisUnlock
        elif brawler == 12:
            return self.player.crowUnlock
        elif brawler == 13:
            return self.player.pocoUnlock
        elif brawler == 14:
            return self.player.boUnlock
        elif brawler == 15:
            return self.player.piperUnlock
        elif brawler == 16:
            return self.player.pamUnlock
        elif brawler == 17:
            return self.player.taraUnlock
        elif brawler == 18:
            return self.player.darrylUnlock
        elif brawler == 19:
            return self.player.pennyUnlock
        elif brawler == 20:
            return self.player.frankUnlock

    def getUnlockedCharacter(self, brawler):
        if brawler == 0:
            return self.player.shellyUnlock
        elif brawler == 1:
            return self.player.coltUnlock
        elif brawler == 2:
            return self.player.bullUnlock
        elif brawler == 3:
            return self.player.brockUnlock
        elif brawler == 4:
            return self.player.ricoUnlock
        elif brawler == 5:
            return self.player.spikeUnlock
        elif brawler == 6:
            return self.player.barleyUnlock
        elif brawler == 7:
            return self.player.jessieUnlock
        elif brawler == 8:
            return self.player.nitaUnlock
        elif brawler == 9:
            return self.player.dynamikeUnlock
        elif brawler == 10:
            return self.player.elprimoUnlock
        elif brawler == 11:
            return self.player.mortisUnlock
        elif brawler == 12:
            return self.player.crowUnlock
        elif brawler == 13:
            return self.player.pocoUnlock
        elif brawler == 14:
            return self.player.boUnlock
        elif brawler == 15:
            return self.player.piperUnlock
        elif brawler == 16:
            return self.player.pamUnlock
        elif brawler == 17:
            return self.player.taraUnlock
        elif brawler == 18:
            return self.player.darrylUnlock
        elif brawler == 19:
            return self.player.pennyUnlock
        elif brawler == 20:
            return self.player.frankUnlock

    def getLockedStarPower(self, starpower):
        if starpower == 76:
            return self.player.shellySPUnlock

        elif starpower == 77:
            return self.player.coltSPUnlock
        elif starpower == 78:
            return self.player.bullSPUnlock
        elif starpower == 79:
            return self.player.brockSPUnlock

        elif starpower == 80:
            return self.player.ricoSPUnlock
        elif starpower == 81:
            return self.player.spikeSPUnlock

        elif starpower == 82:
            return self.player.barleySPUnlock
        elif starpower == 83:
            return self.player.jessieSPUnlock
        elif starpower == 84: 
            return self.player.nitaSPUnlock
        elif starpower == 85:
            return self.player.dynamikeSPUnlock
        elif starpower == 86:
            return self.player.elprimoSPUnlock
        elif starpower == 87:
            return self.player.mortisSPUnlock
        elif starpower == 88:
            return self.player.crowSPUnlock
        elif starpower == 89:
            return self.player.pocoSPUnlock
        elif starpower == 90:
            return self.player.boSPUnlock

        elif starpower == 91:
            return self.player.piperSPUnlock
        elif starpower == 92:
            return self.player.pamSPUnlock
        elif starpower == 93:
            return self.player.taraSPUnlock
        elif starpower == 94:
            return self.player.darrylSPUnlock
        elif starpower == 99:
            return self.player.pennySPUnlock
        elif starpower == 104:
            return self.player.frankSPUnlock

    def UnlockStarPower(self, starpower):
        if starpower == 0:
            self.player.shellySPUnlock = 1
            DataBase.replaceValue(self, 'shellySPUnlock', self.player.shellySPUnlock)
        elif starpower == 1:
            self.player.coltSPUnlock = 1
            DataBase.replaceValue(self, 'coltSPUnlock', self.player.coltSPUnlock)
        elif starpower == 2:
            self.player.bullSPUnlock = 1
            DataBase.replaceValue(self, 'bullSPUnlock', self.player.bullSPUnlock)
        elif starpower == 3:
            self.player.brockSPUnlock = 1
            DataBase.replaceValue(self, 'brockSPUnlock', self.player.brockSPUnlock)
        elif starpower == 4:
            self.player.ricoSPUnlock = 1
            DataBase.replaceValue(self, 'ricoSPUnlock', self.player.ricoSPUnlock)
        elif starpower == 5:
            self.player.spikeSPUnlock = 1
            DataBase.replaceValue(self, 'spikeSPUnlock', self.player.spikeSPUnlock)
        elif starpower == 6:
            self.player.barleySPUnlock = 1
            DataBase.replaceValue(self, 'barleySPUnlock', self.player.barleySPUnlock)
        elif starpower == 7:
            self.player.jessieSPUnlock = 1
            DataBase.replaceValue(self, 'jessieSPUnlock', self.player.jessieSPUnlock)
        elif starpower == 8:
            self.player.nitaSPUnlock = 1
            DataBase.replaceValue(self, 'nitaSPUnlock', self.player.nitaSPUnlock)
        elif starpower == 9:
            self.player.dynamikeSPUnlock = 1
            DataBase.replaceValue(self, 'dynamikeSPUnlock', self.player.dynamikeSPUnlock)
        elif starpower == 10:
            self.player.elprimoSPUnlock = 1
            DataBase.replaceValue(self, 'elprimoSPUnlock', self.player.elprimoSPUnlock)
        elif starpower == 11:
            self.player.mortisSPUnlock = 1
            DataBase.replaceValue(self, 'mortisSPUnlock', self.player.mortisSPUnlock)
        elif starpower == 12:
            self.player.crowSPUnlock = 1
            DataBase.replaceValue(self, 'crowSPUnlock', self.player.crowSPUnlock)
        elif starpower == 13:
            self.player.pocoSPUnlock = 1
            DataBase.replaceValue(self, 'pocoSPUnlock', self.player.pocoSPUnlock)
        elif starpower == 14:
            self.player.boSPUnlock = 1
            DataBase.replaceValue(self, 'boSPUnlock', self.player.boSPUnlock)
        elif starpower == 15:
            self.player.piperSPUnlock = 1
            DataBase.replaceValue(self, 'piperSPUnlock', self.player.piperSPUnlock)
        elif starpower == 16:
            self.player.pamSPUnlock = 1
            DataBase.replaceValue(self, 'pamSPUnlock', self.player.pamSPUnlock)
        elif starpower == 17:
            self.player.taraSPUnlock = 1
            DataBase.replaceValue(self, 'taraSPUnlock', self.player.taraSPUnlock)
        elif starpower == 18:
            self.player.darrylSPUnlock = 1
            DataBase.replaceValue(self, 'darrylSPUnlock', self.player.darrylSPUnlock)
        elif starpower == 19:
            self.player.pennySPUnlock = 1
            DataBase.replaceValue(self, 'pennySPUnlock', self.player.pennySPUnlock)
        elif starpower == 20:
            self.player.frankSPUnlock = 1
            DataBase.replaceValue(self, 'frankSPUnlock', self.player.frankSPUnlock)