from Utils.Writer import Writer


class TeamMessage(Writer):

    def __init__(self, client, player, roomType = 1):
        super().__init__(client)
        self.id = 24124
        self.player = player
        self.roomType = roomType


    def encode(self):
        self.writeVint(self.roomType)
        self.writeUInt8(0)
        self.writeVint(1)

        self.writeLong(self.player.roomID)

        self.writeUInt8(0)
        self.writeUInt8(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeDataReference(15, self.player.mapID)

        self.writeVint(1)
        for x in range(1):

            self.writeVint(1)

            self.writeLong(self.player.ID)

            self.writeDataReference(16, self.player.homeBrawler)
            self.writeDataReference(29, self.player.homeSkin)

            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10)

            self.writeVint(3)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            # sub_64DF74
            self.writeString(self.player.Data['Name'])
            self.writeVint(100)
            self.writeVint(28000000 + self.player.thumbnail)
            self.writeVint(43000000 + self.player.nameColor)
            self.writeNullVint()

            self.writeDataReference(23, self.player.starpower) if self.player.starpower != None else self.writeVint(0)
            self.writeDataReference(23, self.player.gadget)    if self.player.gadget != None else self.writeVint(0)


        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeUInt8(0)
        if self.player.useGadget:
            self.writeUInt8(6)
        else:
            self.writeUInt8(0)

