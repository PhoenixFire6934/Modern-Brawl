from Protocol.Messages.Server.Battle.BattleEndMessage import BattleEndMessage

from Utils.Reader import Reader


class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players = {}

    def decode(self):
        self.result   = self.readVint()
        self.unk      = self.readVint()
        self.rank     = self.readVint()
        self.mapID    = self.readDataReference()
        self.count    = self.readVint()

        for player in range(self.count):
            self.brawler     = self.readDataReference()
            self.skin        = self.readDataReference()
            self.team        = self.readVint()
            self.unk         = self.readVint()
            self.username    = self.readString()

            self.players[player] = {f'Name': self.username, 'Team': self.team, 'Brawler': self.brawler[1], 'Skin': self.skin[1]}



    def process(self):
        if self.rank != 0:
            self.type = 5  if self.players[0]['Team'] == self.players[1]['Team'] else 2
        else:
            self.type = 0

        BattleEndMessage(self.client, self.player, self.type, self.result, self.players).send()
