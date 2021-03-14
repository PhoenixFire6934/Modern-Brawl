from Logic.EventSlots import EventSlots


class LogicClientHome:

    def __init__(self):
        pass

    def encodeHome(self):
        # LOGIC CLIENT HOME #

        # sub_4558EC #
        self.writeVint(0)  # Timestamp
        self.writeVint(0)  # Timestamp

        self.writeVint(self.player.trophies)  # Trophies
        self.writeVint(self.player.trophies)  # Highes Trophies

        self.writeVint(0)
        self.writeVint(200)  # Trophy Road Reward

        self.writeVint(99999)  # Exp Points

        self.writeScId(28, self.player.thumbnail)  # Profile Icon
        self.writeScId(43, self.player.nameColor)  # Profile NameColor

        self.writeVint(0)  # array
        for x in range(0):
            pass

        # Selected Skins array
        self.writeVint(len(self.player.brawlers_skins))
        for brawler_id in self.player.brawlers_skins:
            self.writeScId(29, self.player.brawlers_skins[brawler_id] )

        # Unlocked Skins array
        self.writeVint(len(self.player.skinsID))
        for skin_id in self.player.skinsID:
            self.writeScId(29, skin_id)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeUInt8(0)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)

        self.writeBool(False)
        self.writeBool(False)

        self.writeUInt8(4)

        self.writeVint(2)
        self.writeVint(2)
        self.writeVint(2)

        self.writeVint(0)   # Name Change Cost
        self.writeVint(0)   # Name Change Timer

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)
        self.writeVint(0)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # Tickets
        self.writeVint(0)

        self.writeScId(16, self.player.homeBrawler)

        self.writeString("RO")
        self.writeString("Modern Brawl")

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # array
        for x in range(0):
            pass

        # Brawl Pass Array
        self.writeVint(1)
        for x in range(1):
            self.writeVint(1) # Current Season
            self.writeVint(0) # Pass Tokens
            self.writeVint(1) # Premium Pass Progress
            self.writeVint(1) # Free Pass Progress

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)

            self.writeInt8(1)
            for i in range(4):
                self.writeInt(4)


        self.writeVint(0)  # array
        for x in range(0):
            pass

        # Quests Array
        self.writeBoolean(True)
        if True:
            self.writeVint(1)
            for x in range(1):
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Unknown
                self.writeVint(1)     # Mission Type
                self.writeVint(2)     # Achieved Goal
                self.writeVint(8)     # Quest Goal
                self.writeVint(10)    # Tokens Reward
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Current level
                self.writeVint(0)     # Max level
                self.writeVint(1)     # Quest Type
                self.writeUInt8(2)    # Quest State
                self.writeScId(16, 0) # Brawler SCID
                self.writeVint(0)     # GameMode
                self.writeVint(0)     # Unknown
                self.writeVint(0)     # Unknown

        # Emotes Array
        self.writeBoolean(True)
        if True:
            self.writeVint(len(self.player.emotesID))
            for emote_id in self.player.emotesID:
                self.writeScId(52, emote_id)
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown
                self.writeVint(1)     # Unknown


        # sub_2CEABC #
        self.writeVint(0)   # Shop Timestamp
        self.writeVint(100) # Tokens for Brawl Box
        self.writeVint(10)  # Tokens for Big Box

        self.writeVint(30)
        self.writeVint(3)
        self.writeVint(80)

        self.writeVint(10)
        self.writeVint(40)
        self.writeVint(1000)

        self.writeVint(500)
        self.writeVint(50)
        self.writeVint(999900)

        self.writeVint(0)

        # LOGIC EVENTS #

        count = len(EventSlots.maps)

        self.writeVint(count + 1)  # Map slots count
        for i in range(count + 1):
            self.writeVint(i)

        self.writeVint(count)

        for map in EventSlots.maps:
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(EventSlots.maps.index(map) + 1)
            self.writeVint(map['Ended'])
            self.writeVint(EventSlots.Timer)

            self.writeVint(10)

            self.writeScId(15, map['ID'])

            self.writeVint(map['Status'])

            self.writeString()
            self.writeVint(0)
            self.writeVint(0)
            self.writeVint(0)

            self.writeBoolean(False)

            self.writeVint(0)
            self.writeVint(0)

        self.writeVint(0)

        self.writeVint(8)
        for i in [20, 35, 75, 140, 290, 480, 800, 1250]:
            self.writeVint(i)

        self.writeVint(8)
        for i in [1, 2, 3, 4, 5, 10, 15, 20]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [10, 30, 80]:
            self.writeVint(i)

        self.writeVint(3)
        for i in [6, 20, 60]:
            self.writeVint(i)

        self.writeVint(4)
        for i in [20, 50, 140, 280]:
            self.writeVint(i)

        self.writeVint(4)
        for i in [150, 400, 1200, 2600]:
            self.writeVint(i)

        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(0)
        self.writeVint(10)
        self.writeVint(0)
        self.writeUInt8(0)
        self.writeVint(0)
        self.writeVint(0)

        self.writeUInt8(1)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(1)  # array
        for x in range(1):
            self.writeInt(1)
            self.writeInt(41000014)

        self.writeVint(0)  # array
        for x in range(0):
            pass

        self.writeVint(0)  # array
        for x in range(0):
            pass
