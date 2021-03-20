from Utils.Writer import Writer


class BattleEndMessage(Writer):

    def __init__(self, client, player, type, result, players):
        super().__init__(client)
        self.id = 23456
        self.player  = player
        self.type    = type
        self.result  = result
        self.players = players

    def encode(self):
        self.writeVint(self.type)
        self.writeVint(self.result)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(0)
        self.writeVint(32)
        self.writeVint(0)
        self.writeVint(1)

        self.writeVint(len(self.players))

        for player in self.players:
            self.brawler  = self.players[player]['Brawler']
            self.skin     = self.players[player]['Skin']
            self.team     = self.players[player]['Team']
            self.username = self.players[player]['Name']

            if self.type == 5:
                self.writeVint(player) if self.team == 0 else self.writeVint(2)
            else:
                self.writeVint(2 if self.team != 0 else 1) if self.type == 2 else self.writeVint(self.team if self.team != 1 else 2)

            self.writeDataReference(16, self.brawler)if self.brawler != -1 else self.writeVint(0)
            self.writeDataReference(29, self.skin)   if self.skin != -1 else self.writeVint(0)

            self.writeVint(99999)
            self.writeVint(99999)
            self.writeVint(10)

            self.writeBool(False)

            # sub_64DF74
            self.writeString(self.username)
            self.writeVint(100)
            self.writeVint(28000000)
            self.writeVint(43000000)
            self.writeNullVint()


        self.writeBool(False)
        self.writeBool(False)
        self.writeBool(False)

        self.writeDataReference(28, 0)

        self.writeBool(False)

