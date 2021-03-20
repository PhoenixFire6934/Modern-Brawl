from Protocol.Messages.Server.Gameroom.TeamMessage import TeamMessage
from Utils.Reader import Reader
from Utils.Helpers import Helpers
from Logic.EventSlots import EventSlots


class TeamCreateMessage(Reader):
    def __init__(self, client, player, initial_bytes):
        super().__init__(initial_bytes)
        self.player = player
        self.client = client

    def decode(self):
        self.mapSlot  = self.readVint()
        self.mapID    = self.readVint()
        self.roomType = self.readVint()

    def process(self):
        self.player.mapID  = EventSlots.maps[self.mapSlot - 1]['ID'] if self.mapSlot != -64 else 269
        self.player.roomID = Helpers.randomMapID(self)

        TeamMessage(self.client, self.player).send()