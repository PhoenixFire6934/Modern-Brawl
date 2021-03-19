from Utils.Writer import Writer


class OutOfSyncMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24104
        self.player = player

    def encode(self):
        self.writeInt(0)
