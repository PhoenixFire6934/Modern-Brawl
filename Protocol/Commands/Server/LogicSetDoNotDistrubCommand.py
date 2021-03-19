from Utils.Writer import Writer


class LogicSetDoNotDistrubCommand(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24111
        self.commandID = 213
        self.player = player

    def encode(self):
        self.writeVint(self.commandID)  # Command ID
        self.writeBool(self.player.dnd) # Do Not Disturb

        self.writeInt(0)                # Unknown
        self.writeVint(0)               # Unknown
