class LogicClientAvatar:

    def __init__(self):
        pass


    def encodeAvatar(self):
        self.writeLogicLong(self.player.ID)
        self.writeLogicLong(self.player.ID)
        self.writeLogicLong(self.player.ID)

        self.writeString(self.player.Data['Name'])
        self.writeBool(self.player.Data['NameSet'])

        self.writeInt(0)

        # Commodity count
        self.writeVint(8)

        # Unlocked Brawlers & Resources array
        self.writeVint(len(self.player.cardsUnlockID) + len(self.player.Data['Resources']))
        for unlock_id in self.player.cardsUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(1)
        for resource in self.player.Data['Resources']:
            self.writeDataReference(5, resource['ID'])
            self.writeVint(resource['Amount'])

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(0)

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(0)

        self.writeVint(0)

        # Brawlers Upgrade Poitns array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(0)

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(8)

        # Gadgets and Star Powers array
        self.writeVint(len(self.player.cardsSkillsID))
        for skill_id in self.player.cardsSkillsID:
            self.writeVint(23)
            self.writeVint(skill_id)
            self.writeVint(1)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(self.player.gems)
        self.writeVint(self.player.gems)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(2) # Tutorial Step
        self.writeVint(0)
