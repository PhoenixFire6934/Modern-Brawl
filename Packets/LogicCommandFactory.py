from Packets.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Packets.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Packets.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Packets.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

commands = {

    505: LogicSetPlayerThumbnailCommand,
    506: LogicSelectSkinCommand,
    527: LogicSetPlayerNameColorCommand,

    500: OutOfSyncMessage # Not implemented!

}
