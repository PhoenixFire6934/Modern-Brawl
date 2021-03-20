from Protocol.Messages.Server.Login.LoginOkMessage import LoginOkMessage
from Protocol.Messages.Server.Login.LoginFailedMessage import LoginFailedMessage
from Protocol.Messages.Server.Home.OwnHomeDataMessage import OwnHomeDataMessage

from Utils.Reader import Reader


class LoginMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.player.ID    = self.readLong()
        self.player.token = self.readString()

        self.player.majorVersion = self.readInt()
        self.player.minorVersion = self.readInt()
        self.player.buildVersion = self.readInt()


    def process(self):
        self.player.getPlayerAccount()

        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()