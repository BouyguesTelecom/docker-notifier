import os

from RouterNotifier import RouterNotifier


if __name__ == '__main__':
    notifier = RouterNotifier(os.environ.get("NOTIFICATION_TYPE"))
    notifier.send(os.environ.get("MESSAGE_TITLE"), os.environ.get("MESSAGE_CONTENT"))


