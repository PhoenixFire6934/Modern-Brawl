

from Utils.Reader import Reader

class LogicSetPlayerNameColorCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        for x in range(5):
            self.readVint()
        self.player.nameColor = self.readVint()


    def process(self):
        self.player.updateAccount('NameColor', self.player.nameColor)
