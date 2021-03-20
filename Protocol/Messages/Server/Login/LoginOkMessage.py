from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        self.writeLong(self.player.ID)
        self.writeLong(self.player.ID)
        self.writeString(self.player.token)

        self.writeString() # GameCenter ID
        self.writeString() # Facebook ID

        self.writeInt(self.player.majorVersion)
        self.writeInt(self.player.minorVersion)
        self.writeInt(self.player.buildVersion)

        self.writeString("prod")
        self.writeInt(0)    # Sessions Count
        self.writeInt(0)    # Played Time
        self.writeInt(0)    # Days Since Started Playing

        self.writeString()  # FacebookApp ID
        self.writeString()  # Server Time
        self.writeString()  # Account Created Date

        self.writeInt(1)
