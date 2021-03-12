from Packets.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Files.CsvLogic.Characters import Characters
from Files.CsvLogic.Cards import Cards
from Utils.Reader import Reader


class TeamChangeMemberSettingsMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        self.csvID = self.readVint()
        if self.csvID == 23:
            self.skill = self.readVint()
        else:
            self.csvID = self.readVint()
            if self.csvID == 29:
                self.BrawlerSkinId = self.readVint()


    def process(self):
        if self.csvID == 29:
            self.player.homeBrawler = Characters.get_brawler_by_skin_id(self, self.BrawlerSkinId)
            self.player.starpower   = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 4)
            self.player.gadget      = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 5)

        elif self.csvID == 23:
            type = Cards.check_spg_id(self, self.skill)
            if  type == '4':
                self.player.starpower = self.skill
            elif type == '5':
                self.player.gadget = self.skill


        self.player.updateAccount('Starpower', self.player.starpower)
        self.player.updateAccount('Gadget', self.player.gadget)
        self.player.updateAccount('HomeBrawler', self.player.homeBrawler)

        TeamMessage(self.client, self.player).send()