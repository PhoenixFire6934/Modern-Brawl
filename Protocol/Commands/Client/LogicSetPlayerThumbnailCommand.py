

from Core.Utils.Reader import Reader

class LogicSetPlayerThumbnailCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        for x in range(5):
            self.readVint()
        self.player.thumbnail = self.readVint()


    def process(self):
        self.player.updateAccount('Thumbnail', self.player.thumbnail)
