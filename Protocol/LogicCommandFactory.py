from Protocol.Commands.Client.LogicSetPlayerThumbnailCommand import LogicSetPlayerThumbnailCommand
from Protocol.Commands.Client.LogicSetPlayerNameColorCommand import LogicSetPlayerNameColorCommand
from Protocol.Commands.Client.LogicPurchaseHeroLvlUpMaterialCommand import LogicPurchaseHeroLvlUpMaterialCommand
from Protocol.Commands.Client.LogicSelectSkinCommand import LogicSelectSkinCommand
from Protocol.Commands.Client.LogicPurchaseDoubleCoinsCommand import LogicPurchaseDoubleCoinsCommand
from Protocol.Messages.Server.OutOfSyncMessage import OutOfSyncMessage

commands = {

    505: LogicSetPlayerThumbnailCommand,
    506: LogicSelectSkinCommand,
    509: LogicPurchaseDoubleCoinsCommand,
    521: LogicPurchaseHeroLvlUpMaterialCommand,
    527: LogicSetPlayerNameColorCommand,

    500: OutOfSyncMessage # Command not implemented!

}
