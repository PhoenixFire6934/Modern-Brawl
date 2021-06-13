from Protocol.Messages.EndClientTurnMessage import EndClientTurnMessage

from Protocol.Messages.Client.Login.LoginMessage import LoginMessage
from Protocol.Messages.Client.KeepAliveMessage import KeepAliveMessage

from Protocol.Messages.Client.Home.SetNameMessage import SetNameMessage
from Protocol.Messages.Client.Home.AskProfileMessage import AskProfileMessage
from Protocol.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage

from Protocol.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Protocol.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Protocol.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Protocol.Messages.Client.Gameroom.TeamUseGadgetMessage import TeamUseGadgetMessage
from Protocol.Messages.Client.Home.SetDoNotDistrubMessage import SetDoNotDistrubMessage
from Protocol.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage

from Protocol.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Protocol.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage

from Protocol.Messages.Client.Login.ClientHelloMessage import ClientHelloMessage

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: SetNameMessage,

    14102: EndClientTurnMessage,

    14113: AskProfileMessage,
    14600: AvatarNameCheckRequestMessage,

    14350: TeamCreateMessage,
    14353: TeamLeaveMessage,
    14354: TeamChangeMemberSettingsMessage,
    14363: TeamSetLocationMessage,
    14372: TeamUseGadgetMessage,
    14777: SetDoNotDistrubMessage,

    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage


}
