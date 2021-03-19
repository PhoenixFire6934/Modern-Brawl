from Protocol.Messages.Server.Home.PlayerProfileMessage import PlayerProfileMessage
from Utils.Reader import Reader


class AskProfileMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.ID = self.readLong()


    def process(self):
        PlayerProfileMessage(self.client, self.player, self.ID).send()

