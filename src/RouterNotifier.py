from TeamsNotifier import TeamsNotifier
from MailNotifier import MailNotifier


class RouterNotifier:
    def __new__(cls, name, **kwargs):
        if name == "Teams":
            return TeamsNotifier()
        if name == "Mail":
            return MailNotifier()

        raise Exception("Unknown notifier type: %s" % name)