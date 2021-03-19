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
        self.player.ID    = self.readLong()   # AccountID
        self.player.token = self.readString() # Pass Token

        self.player.major = self.readInt()    # Client Major Version
        self.player.minor = self.readInt()    # Client Minor Version
        self.player.build = self.readInt()    # Client Build Version


    def process(self):
        self.player.getPlayerAccount()

        LoginOkMessage(self.client, self.player).send()
        OwnHomeDataMessage(self.client, self.player).send()