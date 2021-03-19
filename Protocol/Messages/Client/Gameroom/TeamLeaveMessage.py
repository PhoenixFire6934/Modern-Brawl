from Protocol.Messages.Server.Gameroom.TeamLeftMessage import TeamLeftMessage
from Utils.Reader import Reader


class TeamLeaveMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        TeamLeftMessage(self.client, self.player).send()