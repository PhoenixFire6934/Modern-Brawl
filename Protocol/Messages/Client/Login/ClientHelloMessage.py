from Protocol.Messages.Server.Login.ServerHelloMessage import ServerHelloMessage
from Utils.Reader import Reader

class ClientHelloMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        pass

    def process(self):
        ServerHelloMessage(self.client, self.player).send()
