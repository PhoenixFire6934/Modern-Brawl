from Packets.LogicCommandManager import LogicCommandFactory

from Packets.Messages.Client.Login.LoginMessage import LoginMessage
from Packets.Messages.Client.KeepAliveMessage import KeepAliveMessage

from Packets.Messages.Client.Home.SetNameMessage import SetNameMessage
from Packets.Messages.Client.Home.AskProfileMessage import AskProfileMessage
from Packets.Messages.Client.Home.AvatarNameCheckRequestMessage import AvatarNameCheckRequestMessage

from Packets.Messages.Client.Gameroom.TeamCreateMessage import TeamCreateMessage
from Packets.Messages.Client.Gameroom.TeamLeaveMessage import TeamLeaveMessage
from Packets.Messages.Client.Gameroom.TeamSetLocationMessage import TeamSetLocationMessage
from Packets.Messages.Client.Gameroom.TeamUseGadgetMessage import TeamUseGadgetMessage
from Packets.Messages.Client.Home.SetDoNotDistrubMessage import SetDoNotDistrubMessage
from Packets.Messages.Client.Gameroom.TeamChangeMemberSettingsMessage import TeamChangeMemberSettingsMessage

from Packets.Messages.Client.Battle.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Packets.Messages.Client.Battle.AskForBattleEndMessage import AskForBattleEndMessage

packets = {

    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: SetNameMessage,
    14102: LogicCommandFactory,

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
