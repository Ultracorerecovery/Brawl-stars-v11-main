from Protocol.Messages.Client.ClientHelloMessage import ClientHelloMessage
from Protocol.Messages.Client.LoginMessage import LoginMessage
from Protocol.Messages.Client.KeepAliveMessage import KeepAliveMessage
from Protocol.Messages.Client.ChangeAvatarNameMessage import ChangeAvatarNameMessage
from Protocol.Messages.Client.GoHomeFromOfflinePractiseMessage import GoHomeFromOfflinePractiseMessage
from Protocol.Messages.Client.GoHomeMessage import GoHomeMessage
from Protocol.Messages.Client.AskForBattleEndMessage import AskForBattleEndMessage
from Protocol.Messages.Client.EndClientTurnMessage import EndClientTurnMessage
from Protocol.Messages.Client.StartGameMessage import StartGameMessage
from Protocol.Messages.Client.ClientInputMessage import ClientInputMessage

packets = {
    10100: ClientHelloMessage,
    10101: LoginMessage,
    10108: KeepAliveMessage,
    10212: ChangeAvatarNameMessage,
    10555: ClientInputMessage,
    14101: GoHomeMessage,
    14102: EndClientTurnMessage,
    14103: StartGameMessage,
    14109: GoHomeFromOfflinePractiseMessage,
    14110: AskForBattleEndMessage,
}