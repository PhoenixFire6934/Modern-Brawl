from Protocol.Commands.Server.LogicChangeAvatarNameCommand import LogicChangeAvatarNameCommand
from Protocol.Messages.Server.Home.AvatarNameChangeFailedMessage import AvatarNameChangeFailedMessage
from Core.Utils.Reader import Reader


class SetNameMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.username = self.readString()
        self.state = self.readVint()

    def process(self):
        if self.username != '':
            if len(self.username) >= 2 and len(self.username) <= 20:
                self.player.updateAccount('Name', self.username)
                self.player.updateAccount('NameSet', True)
                LogicChangeAvatarNameCommand(self.client, self.player, self.username, self.state).send()
            else:
                AvatarNameChangeFailedMessage(self.client, self.player).send()
        else:
            AvatarNameChangeFailedMessage(self.client, self.player).send()