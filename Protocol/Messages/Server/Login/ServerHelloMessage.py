from Utils.Writer import Writer


class ServerHelloMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20100

    def encode(self):
        self.writeString("Modern Brawl")
