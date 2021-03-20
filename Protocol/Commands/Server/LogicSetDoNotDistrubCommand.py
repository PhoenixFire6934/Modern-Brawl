from Utils.Writer import Writer


class LogicSetDoNotDistrubCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.commandID = 213
        self.player = player

    def encode(self):
        self.writeVint(self.commandID)
        self.writeBool(self.player.dnd)
        self.writeInt32(0)
        self.writeVint(0)
