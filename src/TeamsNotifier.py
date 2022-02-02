import os
import sys

import pymsteams

class TeamsNotifier:
    def notification_type(self):
        return "Teams"

    def send(self, title, message):
        if os.environ.get("WEBHOOK_URL") is None:
            print("WEBHOOK_URL environment variable is not set")
            sys.exit(1)

        myTeamsMessage = pymsteams.connectorcard(os.environ.get("WEBHOOK_URL"))

        if title is not None:
            myTeamsMessage.title(title)

        if os.environ.get("MESSAGE_COLOR") is not None:
            myTeamsMessage.color(os.environ.get("MESSAGE_COLOR"))

        myTeamsMessage.text(message)
        myTeamsMessage.send()