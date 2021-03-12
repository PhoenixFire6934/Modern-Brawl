from Utils.Writer import Writer


class LoginOkMessage(Writer):
    def __init__(self, client, player):
        super().__init__(client)
        self.player = player
        self.id = 20104
        self.version = 1

    def encode(self):
        # AccountID, HomeID
        self.writeLong(self.player.ID)
        self.writeLong(self.player.ID)

        # Pass Token
        self.writeString(self.player.token)

        self.writeString() # GameCenter ID
        self.writeString() # Facebook ID

        self.writeInt(27)  # Major Version
        self.writeInt(140) # Build Version
        self.writeInt(1)   # Minor Version

        self.writeString("prod")  # Environment

        self.writeInt(0)    # Total Sessions
        self.writeInt(0)    # Played Time
        self.writeInt(0)    # Played Time in day

        self.writeString()  # FacebookApp ID
        self.writeString()  # Server Time
        self.writeString()  # Account Created Date

        self.writeInt(1)
