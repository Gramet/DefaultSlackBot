# DefaultSlackBot
This repo contains placeholder code for a simple Slackbot that will send messages to a given channel.

It **does not** (yet) implements:
- Slash commands
- Interactive components
- Event subscriptions

# How to use

## Requirements
- Python 3 installed
- Admin rights on a Slack Workspace

## Setup

1. Connect on [Slack development interface](https://api.slack.com/apps) and create a new app
2. Create a new **Incoming Webhook** towards the channel you want
3. Update the `scripts/slackbot.py` file with the SLACK_WEBHOOK, BOT_USERNAME and ICON_EMOJI you want to use
4. Customize the `getMessage` function to create the message you want to send
5. (Make sure you already have run `pip install -r requirements.txt` and) run `python slackbot.py` to send a message to the Slack channel.

# Additional tips

## Automation
- It can be convenient to setup a [Cron Job](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) to automatically send messages at given times

