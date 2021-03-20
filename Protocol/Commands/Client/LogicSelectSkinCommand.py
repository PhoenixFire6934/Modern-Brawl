from Utils.Reader import Reader
from Files.CsvLogic.Cards import Cards

class LogicSelectSkinCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client


    def decode(self):
        for x in range(4):
            self.readVint()
        self.skinID = self.readDataReference()[1]
        for x in range(5):
            self.readVint()
        self.player.homeBrawler = self.readDataReference()[1]


    def process(self):
        self.player.brawlers_skins[str(self.player.homeBrawler)] = self.skinID
        self.player.starpower = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 4)
        self.player.gadget    = Cards.get_spg_by_brawler_id(self, self.player.homeBrawler, 5)

        self.player.updateAccount('Starpower', self.player.starpower)
        self.player.updateAccount('Gadget', self.player.gadget)
        self.player.updateAccount('HomeSkins', self.player.brawlers_skins)
        self.player.updateAccount('HomeBrawler', self.player.homeBrawler)
