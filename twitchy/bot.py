import irc.bot
import gi
gi.require_version('Notify', '0.7')
from gi.repository import Notify

class TwitchBot(irc.bot.SingleServerIRCBot):
    def __init__(self, user, oauth):
        if not oauth.startswith('oauth:'):
            oauth = 'oauth:' + oauth
        super().__init__([('irc.chat.twitch.tv', 6667, oauth)], nickname=user.lower(), realname=user)
        self.user = user

    def on_welcome(self, c, e):
        c.cap('REQ', 'twitch.tv/membership')
        c.cap('END')
        c.join('#'+self.user.lower())

    def on_join(self, c, e):
        self.notify(e.source.nick, "Joined {}".format(e.target), replyable=False)

    def on_privmsg(self, c, e):
        self.notify(e.source.nick, e.arguments[0])

    def on_pubmsg(self, c, e):
        self.notify(e.source.nick, e.arguments[0])

    def notify(self, usr, msg, *, replyable=True):
        print("<{}> {}".format(usr, msg))
        notification = Notify.Notification.new(usr, msg, "mail-message-new")
        if replyable:
            notification.add_action(
                "action_click",
                "Reply",
                self.reply,
                None
            )
        notification.show()

    def reply(self, usr):
        print("Reply", usr)