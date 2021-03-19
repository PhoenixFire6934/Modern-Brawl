from Protocol.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Protocol.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Protocol.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Protocol.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

commands = {

    505: LogicSetPlayerThumbnailCommand,
    506: LogicSelectSkinCommand,
    527: LogicSetPlayerNameColorCommand,

    500: OutOfSyncMessage # Not implemented!

}
