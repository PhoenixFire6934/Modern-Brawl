from Protocol.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Core.Utils.Reader import Reader


class TeamUseGadgetMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.useGadget = self.readBool()

    def process(self):
        TeamMessage(self.client, self.player).send()