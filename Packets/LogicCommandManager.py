from Utils.Reader import Reader
from Packets.LogicCommandFactory import commands


class LogicCommandFactory(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()
        self.commandID = self.readVint()


    def process(self):
        if self.commandID in commands:
            command = commands[self.commandID]
            try:
                command.decode(self)
                command.process(self)
            except AttributeError:
                command(self.client, self.player).send() # Exception for OutOfSyncMessage

        elif self.commandID != -134217728:
            print(f'[INFO] Command not handled! ({self.commandID})')

