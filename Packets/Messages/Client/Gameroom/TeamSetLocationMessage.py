from Packets.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Utils.Reader import Reader

class TeamSetLocationMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVint()
        self.player.mapID = self.readVint()


    def process(self):
        TeamMessage(self.client, self.player).send()