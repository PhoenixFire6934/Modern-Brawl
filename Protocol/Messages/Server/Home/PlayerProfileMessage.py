from Core.Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.ID = ID

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.ID)

        self.writeVint(0) # SCID

        # Unlocked Brawlers Array
        self.writeVint(len(self.player.brawlersID))
        for brawler_id in self.player.brawlersID:
            self.writeDataReference(16, brawler_id)
            self.writeVint(0)     # SCID
            self.writeVint(99999) # Brawler Trophies
            self.writeVint(99999) # Brawler Highest Trophies
            self.writeVint(10)    # Brawler Power Level

        # Player Stats Array
        self.writeVint(15)

        for i in range(1):
            self.writeVint(1)
            self.writeVint(99999) # 3v3 Victories

            self.writeVint(2)
            self.writeVint(99999) # Unknown

            self.writeVint(3)
            self.writeVint(99999) # Unknown

            self.writeVint(4)
            self.writeVint(99999) # Highest Trophies

            self.writeVint(5)
            self.writeVint(len(self.player.brawlersID))

            self.writeVint(7)
            self.writeVint(2800000)

            self.writeVint(8)
            self.writeVint(99999) # Solo Victories

            self.writeVint(9)
            self.writeVint(21)   # Robo Rumble Lvl

            self.writeVint(10)
            self.writeVint(99999) # Unknown

            self.writeVint(11)
            self.writeVint(99999) # Duo Victories

            self.writeVint(12)
            self.writeVint(21)   # Boss Fight Lvl

            self.writeVint(13)
            self.writeVint(99999) # Unknown

            self.writeVint(14)
            self.writeVint(1)    # Power Play Rank

            self.writeVint(15)
            self.writeVint(99999) # Most Challenge Wins

            self.writeVint(16)
            self.writeVint(21)   # Rampage Lvl Passed

        # sub_64DF74
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeNullVint()

        self.writeBoolean(False) # Is Player in Club
        self.writeVint(0)        # SCID


