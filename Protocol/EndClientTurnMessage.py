from Core.Utils.Reader import Reader
from Protocol.LogicCommandFactory import commands


class EndClientTurnMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.client = client
        self.player = player

    def decode(self):
        self.readVint()
        self.readVint()
        self.readVint()
        self.tickCheck = self.readVint()
        if self.tickCheck != 0:
            self.commandID = self.readVint()


    def process(self):
        if self.tickCheck != 0:
            if self.commandID in commands:
                command = commands[self.commandID]
                try:
                    command.decode(self)
                    command.process(self)
                except AttributeError:
                    command(self.client, self.player).send() # Exception for OutOfSyncMessage

            else:
                print(f'[INFO] Command not handled! ({self.commandID})')