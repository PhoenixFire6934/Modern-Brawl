from Utils.Writer import Writer


class PlayerProfileMessage(Writer):

    def __init__(self, client, player, ID):
        super().__init__(client)
        self.id = 24113
        self.player = player
        self.ID = ID

    def encode(self):
        self.writeVint(0)
        self.writeVint(self.ID)

        self.writeVint(0)

        self.writeVint(0)
        for x in range(0):
            pass

        self.writeVint(0)
        for x in range(0):
            pass

        # sub_64DF74
        self.writeString(self.player.name)
        self.writeVint(100)
        self.writeVint(28000000)
        self.writeVint(43000000)
        self.writeNullVint()

        self.writeBoolean(False)
        self.writeVint(0)


