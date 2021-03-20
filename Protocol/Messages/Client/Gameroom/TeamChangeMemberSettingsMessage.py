from Protocol.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Cards import Cards
from Utils.Reader import Reader


class TeamChangeMemberSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.scID = self.readDataReference()
        if self.scID[0] == 0:
            self.scID = self.readDataReference()


    def process(self):
        if self.scID[0] == 29:
            self.player.homeBrawler = Characters.get_brawler_by_skin_id(self, self.scID[1])
            self.player.starpower   = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 4)
            self.player.gadget      = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 5)

        elif self.scID[0] == 23:
            type = Cards.check_spg_id(self, self.scID[1])
            if  type == '4':
                self.player.starpower = self.scID[1]
            elif type == '5':
                self.player.gadget = self.scID[1]


        self.player.updateAccount('Starpower', self.player.starpower)
        self.player.updateAccount('Gadget', self.player.gadget)
        self.player.updateAccount('HomeBrawler', self.player.homeBrawler)

        TeamMessage(self.client, self.player).send()