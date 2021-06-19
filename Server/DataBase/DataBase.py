import json
import string
import random

class DataBase:

    def loadAccount(self):
        with open('data.db', 'r') as read_data:
            for line in read_data.readlines():

                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file

                if self.player.Token in dict:
                    self.player.name = dict[str(self.player.Token)]["name"]
                    self.player.gems = dict[str(self.player.Token)]["gems"]
                    self.player.gold = dict[str(self.player.Token)]["gold"]
                    self.player.nameSet = dict[str(self.player.Token)]["nameSet"]
                    self.player.allianceID = dict[str(self.player.Token)]["allianceID"]
                    self.player.keysReward = dict[str(self.player.Token)]["keysReward"]
                    self.player.starKeysReward = dict[str(self.player.Token)]["starKeysReward"]
                    self.player.trophiesReward = dict[str(self.player.Token)]["trophiesReward"]
                    self.player.tutorialState = dict[str(self.player.Token)]["tutorialState"]
                    self.player.experience = dict[str(self.player.Token)]["experience"]
                    self.player.tickets = dict[str(self.player.Token)]["tickets"]
                    self.player.brawlerID = dict[str(self.player.Token)]["selectedBrawler"]
                    self.player.skinID = dict[str(self.player.Token)]["skinID"]
                    self.player.trophies = dict[str(self.player.Token)]["trophies"]
                    self.player.profileIcon = dict[str(self.player.Token)]["profileIcon"]
                    self.player.brawlBoxTokens = dict[str(self.player.Token)]["brawlBoxTokens"]
                    self.player.bigBoxTokens = dict[str(self.player.Token)]["bigBoxTokens"]
                    self.player.shellyUnlock = dict[str(self.player.Token)]["shellyUnlock"]
                    self.player.nitaUnlock = dict[str(self.player.Token)]["nitaUnlock"]
                    self.player.coltUnlock = dict[str(self.player.Token)]["coltUnlock"]
                    self.player.bullUnlock = dict[str(self.player.Token)]["bullUnlock"]
                    self.player.jessieUnlock = dict[str(self.player.Token)]["jessieUnlock"]
                    self.player.brockUnlock = dict[str(self.player.Token)]["brockUnlock"]
                    self.player.dynamikeUnlock = dict[str(self.player.Token)]["dynamikeUnlock"]
                    self.player.boUnlock = dict[str(self.player.Token)]["boUnlock"]
                    self.player.elprimoUnlock = dict[str(self.player.Token)]["elprimoUnlock"]
                    self.player.barleyUnlock = dict[str(self.player.Token)]["barleyUnlock"]
                    self.player.pocoUnlock = dict[str(self.player.Token)]["pocoUnlock"]
                    self.player.ricoUnlock = dict[str(self.player.Token)]["ricoUnlock"]
                    self.player.darrylUnlock = dict[str(self.player.Token)]["darrylUnlock"]
                    self.player.pennyUnlock = dict[str(self.player.Token)]["pennyUnlock"]
                    self.player.piperUnlock = dict[str(self.player.Token)]["piperUnlock"]
                    self.player.pamUnlock = dict[str(self.player.Token)]["pamUnlock"]
                    self.player.frankUnlock = dict[str(self.player.Token)]["frankUnlock"]
                    self.player.mortisUnlock = dict[str(self.player.Token)]["mortisUnlock"]
                    self.player.taraUnlock = dict[str(self.player.Token)]["taraUnlock"]
                    self.player.spikeUnlock = dict[str(self.player.Token)]["spikeUnlock"]
                    self.player.crowUnlock = dict[str(self.player.Token)]["crowUnlock"]
                    self.player.shellyScore = dict[str(self.player.Token)]["shellyScore"]
                    self.player.nitaScore = dict[str(self.player.Token)]["nitaScore"]
                    self.player.coltScore = dict[str(self.player.Token)]["coltScore"]
                    self.player.bullScore = dict[str(self.player.Token)]["bullScore"]
                    self.player.jessieScore = dict[str(self.player.Token)]["jessieScore"]
                    self.player.brockScore = dict[str(self.player.Token)]["brockScore"]
                    self.player.dynamikeScore = dict[str(self.player.Token)]["dynamikeScore"]
                    self.player.boScore = dict[str(self.player.Token)]["boScore"]
                    self.player.elprimoScore = dict[str(self.player.Token)]["elprimoScore"]
                    self.player.barleyScore = dict[str(self.player.Token)]["barleyScore"]
                    self.player.pocoScore = dict[str(self.player.Token)]["pocoScore"]
                    self.player.ricoScore = dict[str(self.player.Token)]["ricoScore"]
                    self.player.darrylScore = dict[str(self.player.Token)]["darrylScore"]
                    self.player.pennyScore = dict[str(self.player.Token)]["pennyScore"]
                    self.player.piperScore = dict[str(self.player.Token)]["piperScore"]
                    self.player.pamScore = dict[str(self.player.Token)]["pamScore"]
                    self.player.frankScore = dict[str(self.player.Token)]["frankScore"]
                    self.player.mortisScore = dict[str(self.player.Token)]["mortisScore"]
                    self.player.taraScore = dict[str(self.player.Token)]["taraScore"]
                    self.player.spikeScore = dict[str(self.player.Token)]["spikeScore"]
                    self.player.crowScore = dict[str(self.player.Token)]["crowScore"]
                    self.player.shellyLVL = dict[str(self.player.Token)]["shellyLVL"]
                    self.player.nitaLVL = dict[str(self.player.Token)]["nitaLVL"]
                    self.player.coltLVL = dict[str(self.player.Token)]["coltLVL"]
                    self.player.bullLVL = dict[str(self.player.Token)]["bullLVL"]
                    self.player.jessieLVL = dict[str(self.player.Token)]["jessieLVL"]
                    self.player.brockLVL = dict[str(self.player.Token)]["brockLVL"]
                    self.player.dynamikeLVL = dict[str(self.player.Token)]["dynamikeLVL"]
                    self.player.boLVL = dict[str(self.player.Token)]["boLVL"]
                    self.player.elprimoLVL = dict[str(self.player.Token)]["elprimoLVL"]
                    self.player.barleyLVL = dict[str(self.player.Token)]["barleyLVL"]
                    self.player.pocoLVL = dict[str(self.player.Token)]["pocoLVL"]
                    self.player.ricoLVL = dict[str(self.player.Token)]["ricoLVL"]
                    self.player.darrylLVL = dict[str(self.player.Token)]["darrylLVL"]
                    self.player.pennyLVL = dict[str(self.player.Token)]["pennyLVL"]
                    self.player.piperLVL = dict[str(self.player.Token)]["piperLVL"]
                    self.player.pamLVL = dict[str(self.player.Token)]["pamLVL"]
                    self.player.frankLVL = dict[str(self.player.Token)]["frankLVL"]
                    self.player.mortisLVL = dict[str(self.player.Token)]["mortisLVL"]
                    self.player.taraLVL = dict[str(self.player.Token)]["taraLVL"]
                    self.player.spikeLVL = dict[str(self.player.Token)]["spikeLVL"]
                    self.player.crowLVL = dict[str(self.player.Token)]["crowLVL"]
                    self.player.shellyPP = dict[str(self.player.Token)]["shellyPP"]
                    self.player.nitaPP = dict[str(self.player.Token)]["nitaPP"]
                    self.player.coltPP = dict[str(self.player.Token)]["coltPP"]
                    self.player.bullPP = dict[str(self.player.Token)]["bullPP"]
                    self.player.jessiePP = dict[str(self.player.Token)]["jessiePP"]
                    self.player.brockPP = dict[str(self.player.Token)]["brockPP"]
                    self.player.dynamikePP = dict[str(self.player.Token)]["dynamikePP"]
                    self.player.boPP = dict[str(self.player.Token)]["boPP"]
                    self.player.elprimoPP = dict[str(self.player.Token)]["elprimoPP"]
                    self.player.barleyPP = dict[str(self.player.Token)]["barleyPP"]
                    self.player.pocoPP = dict[str(self.player.Token)]["pocoPP"]
                    self.player.ricoPP = dict[str(self.player.Token)]["ricoPP"]
                    self.player.darrylPP = dict[str(self.player.Token)]["darrylPP"]
                    self.player.pennyPP = dict[str(self.player.Token)]["pennyPP"]
                    self.player.piperPP = dict[str(self.player.Token)]["piperPP"]
                    self.player.pamPP = dict[str(self.player.Token)]["pamPP"]
                    self.player.frankPP = dict[str(self.player.Token)]["frankPP"]
                    self.player.mortisPP = dict[str(self.player.Token)]["mortisPP"]
                    self.player.taraPP = dict[str(self.player.Token)]["taraPP"]
                    self.player.spikePP = dict[str(self.player.Token)]["spikePP"]
                    self.player.crowPP = dict[str(self.player.Token)]["crowPP"]
                    self.player.shellySPUnlock = dict[str(self.player.Token)]["shellySPUnlock"]
                    self.player.nitaSPUnlock = dict[str(self.player.Token)]["nitaSPUnlock"]
                    self.player.coltSPUnlock = dict[str(self.player.Token)]["coltSPUnlock"]
                    self.player.bullSPUnlock = dict[str(self.player.Token)]["bullSPUnlock"]
                    self.player.jessieSPUnlock = dict[str(self.player.Token)]["jessieSPUnlock"]
                    self.player.brockSPUnlock = dict[str(self.player.Token)]["brockSPUnlock"]
                    self.player.dynamikeSPUnlock = dict[str(self.player.Token)]["dynamikeSPUnlock"]
                    self.player.boSPUnlock = dict[str(self.player.Token)]["boSPUnlock"]
                    self.player.elprimoSPUnlock = dict[str(self.player.Token)]["elprimoSPUnlock"]
                    self.player.barleySPUnlock = dict[str(self.player.Token)]["barleySPUnlock"]
                    self.player.pocoSPUnlock = dict[str(self.player.Token)]["pocoSPUnlock"]
                    self.player.ricoSPUnlock = dict[str(self.player.Token)]["ricoSPUnlock"]
                    self.player.darrylSPUnlock = dict[str(self.player.Token)]["darrylSPUnlock"]
                    self.player.pennySPUnlock = dict[str(self.player.Token)]["pennySPUnlock"]
                    self.player.piperSPUnlock = dict[str(self.player.Token)]["piperSPUnlock"]
                    self.player.pamSPUnlock = dict[str(self.player.Token)]["pamSPUnlock"]
                    self.player.frankSPUnlock = dict[str(self.player.Token)]["frankSPUnlock"]
                    self.player.mortisSPUnlock = dict[str(self.player.Token)]["mortisSPUnlock"]
                    self.player.taraSPUnlock = dict[str(self.player.Token)]["taraSPUnlock"]
                    self.player.spikeSPUnlock = dict[str(self.player.Token)]["spikeSPUnlock"]
                    self.player.crowSPUnlock = dict[str(self.player.Token)]["crowSPUnlock"]
                    self.player.roomID = dict[str(self.player.Token)]["roomID"]
                    self.player.mapID = dict[str(self.player.Token)]["mapID"]

    def createAccount(self):
        data = {
            self.player.Token: {
                "lowID":self.player.LowID,
                "name": self.player.name,
                "allianceID": 0,
                "tutorialState": 0,
                "experience": self.player.experience,
                "gems": self.player.gems,
                "gold": self.player.gold,
                "nameSet": 0,
                "tickets": self.player.tickets,
                "trophiesReward": 0,
                "starKeysReward": 0,
                "keysReward": 0,
                "selectedBrawler": 0,
                "skinID": 0,
                "trophies": 0,
                "profileIcon": 0,
                "brawlBoxTokens": self.player.brawlBoxTokens,
                "bigBoxTokens": 0,
                "shellyUnlock": 1,
                "nitaUnlock": 0,
                "coltUnlock": 0,
                "bullUnlock": 0,
                "jessieUnlock": 0,
                "brockUnlock": 0,
                "dynamikeUnlock": 0,
                "boUnlock": 0,
                "elprimoUnlock": 0,
                "barleyUnlock": 0,
                "pocoUnlock": 0,
                "ricoUnlock": 0,
                "darrylUnlock": 0,
                "pennyUnlock": 0,
                "piperUnlock": 0,
                "pamUnlock": 0,
                "frankUnlock": 0,
                "mortisUnlock": 0,
                "taraUnlock": 0,
                "spikeUnlock": 0,
                "crowUnlock": 0,
                "shellyScore": 0,
                "nitaScore": 0,
                "coltScore": 0,
                "bullScore": 0,
                "jessieScore": 0,
                "brockScore": 0,
                "dynamikeScore": 0,
                "boScore": 0,
                "elprimoScore": 0,
                "barleyScore": 0,
                "pocoScore": 0,
                "ricoScore": 0,
                "darrylScore": 0,
                "pennyScore": 0,
                "piperScore": 0,
                "pamScore": 0,
                "frankScore": 0,
                "mortisScore": 0,
                "taraScore": 0,
                "spikeScore": 0,
                "crowScore": 0,
                "shellyLVL": 0,
                "nitaLVL": 0,
                "coltLVL": 0,
                "bullLVL": 0,
                "jessieLVL": 0,
                "brockLVL": 0,
                "dynamikeLVL": 0,
                "boLVL": 0,
                "elprimoLVL": 0,
                "barleyLVL": 0,
                "pocoLVL": 0,
                "ricoLVL": 0,
                "darrylLVL": 0,
                "pennyLVL": 0,
                "piperLVL": 0,
                "pamLVL": 0,
                "frankLVL": 0,
                "mortisLVL": 0,
                "taraLVL": 0,
                "spikeLVL": 0,
                "crowLVL": 0,
                "shellyPP": 0,
                "nitaPP": 0,
                "coltPP": 0,
                "bullPP": 0,
                "jessiePP": 0,
                "brockPP": 0,
                "dynamikePP": 0,
                "boPP": 0,
                "elprimoPP": 0,
                "barleyPP": 0,
                "pocoPP": 0,
                "ricoPP": 0,
                "darrylPP": 0,
                "pennyPP": 0,
                "piperPP": 0,
                "pamPP": 0,
                "frankPP": 0,
                "mortisPP": 0,
                "taraPP": 0,
                "spikePP": 0,
                "crowPP": 0,
                "shellySPUnlock": 0,
                "nitaSPUnlock": 0,
                "coltSPUnlock": 0,
                "bullSPUnlock": 0,
                "jessieSPUnlock": 0,
                "brockSPUnlock": 0,
                "dynamikeSPUnlock": 0,
                "boSPUnlock": 0,
                "elprimoSPUnlock": 0,
                "barleySPUnlock": 0,
                "pocoSPUnlock": 0,
                "ricoSPUnlock": 0,
                "darrylSPUnlock": 0,
                "pennySPUnlock": 0,
                "piperSPUnlock": 0,
                "pamSPUnlock": 0,
                "frankSPUnlock": 0,
                "mortisSPUnlock": 0,
                "taraSPUnlock": 0,
                "spikeSPUnlock": 0,
                "crowSPUnlock": 0,
                "roomID": 0,
                "mapID": 7
            }
        }

        with open('data.db', 'a+') as data_file:
            json.dump(data, data_file)  # writing data for new account
            data_file.write('\n')  # writing a new line



    def replaceValue(self, value_name, new_value): # usage: replaceValue(self, 'gems', 7777)
        with open('data.db', 'r+') as file:
            list = []

            for line in file.readlines():
                json_data = json.loads(line)
                dict = json.loads(json.dumps(json_data))  # loading and dumping json data from file
                if self.player.Token in dict:
                    dict[str(self.player.Token)][str(value_name)] = new_value
                list.append(dict)
                file.close()

        with open('data.db', 'w') as o:
            for i in list:
                o.write(str(i).replace("'", '"') + '\n')
            o.close()

