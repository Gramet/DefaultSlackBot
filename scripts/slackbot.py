#!/usr/bin/env python

import sys
import json
import requests

# see README for directions on how to fill these variables
SLACK_WEBHOOK = ""


def postMessage(message):
    """
    Post the message to to Slack's API in the proper channel
    """
    payload = json.dumps(
        {
            "text": message,
        }
    )

    requests.post(
        SLACK_WEBHOOK, data=payload, headers={"Content-Type": "application/json"}
    )


def getMessage():
    """
    Get message to send
    """

    message = "Hello Slack!"

    return message


def main():
    """
    Main program loop
    """
    # make sure all variables are filled
    if SLACK_WEBHOOK == "":
        print(
            "Please update script variables before running script.\n\
                See README for details on how to do this."
        )
        sys.exit(1)

    message = getMessage()
    # send message to slack
    postMessage(message)


if __name__ == "__main__":
    main()
