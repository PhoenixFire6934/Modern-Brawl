from Protocol.Commands.Server.LogicSetDoNotDistrubCommand import LogicSetDoNotDistrubCommand
from Utils.Reader import Reader


class SetDoNotDistrubMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.dnd = self.readVint()

    def process(self):
        LogicSetDoNotDistrubCommand(self.client, self.player).send()