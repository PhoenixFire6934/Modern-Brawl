from Core.Utils.Writer import Writer


class TeamMessage(Writer):

    def __init__(self, client, player, roomType = 1):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.roomType = roomType


    def encode(self):
        # Gameroom Type
        self.writeVint(self.roomType)

        self.writeUInt8(0)
        self.writeVint(1)

        # MapID
        self.writeLong(self.player.roomID)

        self.writeUInt8(0)
        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(0)

        # MapID
        self.writeDataReference(15, self.player.mapID)

        # Players in Room
        self.writeVint(1)
        for x in range(1):

            self.writeVint(1)

            self.writeLong(self.player.ID) # AccountID

            self.writeDataReference(16, self.player.homeBrawler)  # BrawlerID
            self.writeDataReference(29, self.player.homeSkin)     # SkinID

            self.writeVint(99999) # Trophies
            self.writeVint(99999) # Highest Trophies
            self.writeVint(10)    # Power Level

            self.writeVint(3)     # Player State
            self.writeVint(0)     # Is Player Ready
            self.writeVint(0)     # Team (Blue/Red)
            self.writeVint(0)
            self.writeVint(0)

            # Player Name
            self.writeString(self.player.Data['Name'])

            self.writeVint(100)
            self.writeVint(28000000 + self.player.thumbnail) # Thumbnail
            self.writeVint(43000000 + self.player.nameColor) # Name Color

            self.writeNullVint()

            self.writeDataReference(23, self.player.starpower) # StarpowerID
            self.writeDataReference(23, self.player.gadget)    # GadgetID


        self.writeVint(0) # array
        self.writeVint(0) # array

        self.writeUInt8(0)
        if self.player.useGadget:
            self.writeUInt8(6)
        else:
            self.writeUInt8(0)

