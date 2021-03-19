from Utils.Writer import Writer
from Logic.Home.LogicClientHome import LogicClientHome
from Logic.Avatar.LogicClientAvatar import LogicClientAvatar


class OwnHomeDataMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 24101
        self.player = player

    def encode(self):
        LogicClientHome.encodeHome(self)
        LogicClientAvatar.encodeAvatar(self)

