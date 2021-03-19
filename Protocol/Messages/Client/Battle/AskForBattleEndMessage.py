from Protocol.Messages.Server.Battle.BattleEndMessage import BattleEndMessage

from Core.Utils.Reader import Reader


class AskForBattleEndMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client
        self.players = {}

    def decode(self):
        self.result   = self.readVint()  # Battle Result
        self.unk      = self.readVint()  # Unknown
        self.rank     = self.readVint()  # Player Rank
        self.mapID    = self.readScId()  # Map ID
        self.count    = self.readVint()  # Players Count

        # Players in Battle
        for player in range(self.count):
            self.brawler     = self.readScId()       # Player Skin SCID
            self.skin        = self.readScId()       # Player Skin SCID
            self.team        = self.readVint()       # Player Team
            self.unk         = self.readVint()       # Unknown
            self.username    = self.readString()     # Player Name

            self.players[player] = {f'Name': self.username, 'Team': self.team, 'Brawler': self.brawler[1], 'Skin': self.skin[1]}



    def process(self):
        if self.rank != 0:
            self.type = 5  if self.players[0]['Team'] == self.players[1]['Team'] else 2
        else:
            self.type = 0

        BattleEndMessage(self.client, self.player, self.type, self.result, self.players).send()
