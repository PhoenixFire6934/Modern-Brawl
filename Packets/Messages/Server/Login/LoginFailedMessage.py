from Utils.Writer import Writer


class LoginFailedMessage(Writer):

    def __init__(self, client, player):
        super().__init__(client)
        self.id = 20103
        self.player = player


    def encode(self):
        self.writeInt(10)

        self.writeString() # Fingerprint
        self.writeString() # Server Host

        self.writeString() # Update URL
        self.writeString() # Patch URL
        self.writeString() # Message

        self.writeInt(3600)
        self.writeBoolean(False)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(3)

        self.writeString()
        self.writeString()

        self.writeInt(0)
        self.writeInt(0)

        self.writeBoolean(False)
        self.writeBoolean(False)



