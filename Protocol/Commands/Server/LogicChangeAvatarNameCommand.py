from Utils.Writer import Writer

class LogicChangeAvatarNameCommand(Writer):

    def __init__(self, client, player, username, state):
        super().__init__(client)
        self.id = 24111
        self.commandID = 201
        self.player = player
        self.username = username
        self.state = state

    def encode(self):
        self.writeVint(self.commandID)
        self.writeString(self.username)
        self.writeVint(self.state)
