class LogicClientAvatar:

    def __init__(self):
        pass


    def encodeAvatar(self):
        self.writeLong(self.player.ID)

        self.writeVint(0) # array
        for x in range(0):
            pass

        self.writeVint(0)

        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(self.player.ID)

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)

        self.writeString(self.player.name)     # Player Name
        self.writeBoolean(self.player.nameSet) # Name Set By User

        self.writeInt(0)

        # Commodity count
        self.writeVint(8)

        # Unlocked Brawlers $ Resources array
        self.writeVint(len(self.player.cardsUnlockID) + len(self.player.Data['Resources']))
        for unlock_id in self.player.cardsUnlockID:
            self.writeVint(23)
            self.writeVint(unlock_id)
            self.writeVint(1)
        for resource in self.player.Data['Resources']:
            self.writeScId(5, resource['ID'])  # Resource SCID
            self.writeVint(resource['Amount']) # Resource Amount

        # Brawlers Trophies array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(0)

        # Brawlers Trophies for Rank array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(0)

        self.writeVint(0) # array

        # Brawlers Upgrade Poitns array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
            self.writeVint(0)

        # Brawlers Power Level array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeScId(16, brawler_id)
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

        self.writeVint(self.player.gems)  # Gems
        self.writeVint(self.player.gems)  # Free Gems

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        # Tutorial Step
        self.writeVint(2)

        self.writeVint(0)
