from Protocol.Messages.Server.Home.AvatarNameCheckResponseMessage import AvatarNameCheckResponseMessage
from Utils.Reader import Reader


class AvatarNameCheckRequestMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.readString()

    def process(self):
        AvatarNameCheckResponseMessage(self.client, self.player, self.username).send()