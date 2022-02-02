import os
import sys

import pymsteams

if __name__ == '__main__':
    if os.environ.get("WEBHOOK_URL") is None:
        print("WEBHOOK_URL environment variable is not set")
        sys.exit(1)

    myTeamsMessage = pymsteams.connectorcard(os.environ.get("WEBHOOK_URL"))

    if os.environ.get("MESSAGE_TITLE") is not None:
        myTeamsMessage.title(os.environ.get("MESSAGE_TITLE"))

    if os.environ.get("MESSAGE_COLOR") is not None:
        myTeamsMessage.color(os.environ.get("MESSAGE_COLOR"))

    myTeamsMessage.text(os.environ.get("MESSAGE_CONTENT"))
    myTeamsMessage.send()

