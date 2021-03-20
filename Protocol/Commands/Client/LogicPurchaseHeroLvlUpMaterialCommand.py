from Logic.Shop import Shop
from Utils.Reader import Reader

class LogicPurchaseHeroLvlUpMaterialCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.readVint()
        self.readVint()
        self.readVint()
        self.readVint()
        self.gold = self.readVint()


    def process(self):
        self.player.resources[1]['Amount'] = self.player.resources[1]['Amount'] + Shop.gold[self.gold]['Amount']
        self.player.gems = self.player.gems - Shop.gold[self.gold]['Cost']
        self.player.updateAccount('Diamonds', self.player.gems)
        self.player.updateAccount('Resources', self.player.resources)




