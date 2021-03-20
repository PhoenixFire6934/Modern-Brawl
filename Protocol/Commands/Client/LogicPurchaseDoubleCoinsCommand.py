from Logic.Shop import Shop
from Utils.Reader import Reader

class LogicPurchaseDoubleCoinsCommand(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        self.player.gems = self.player.gems - Shop.token_doubler['Cost']
        self.player.updateAccount('Diamonds', self.player.gems)


