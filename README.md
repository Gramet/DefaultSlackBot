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

1. Connect on [Slack development interface](https://api.slack.com/apps) and create a new app. You can customize the bot's Username and Icon here. If you need to use different icons/username with the same bot, check the additional tips.
2. Create a new **Incoming Webhook** towards the channel you want inside your app.
3. Update the `scripts/slackbot.py` file with the SLACK_WEBHOOK you just created.
4. Customize the `getMessage` function to create the message you want to send.
5. (Make sure you already have run `pip install -r requirements.txt` and) run `python slackbot.py` to send a message to the Slack channel.

# Additional tips

## Automation
- It can be convenient to setup a [Cron Job](https://ostechnix.com/a-beginners-guide-to-cron-jobs/) to automatically send messages at given times

## Webhooks and Name/Icon
- If you wish to override the `icon_emoji` or `username` of the bot when sending messages, you need to use a [simple webhook](https://slack.com/apps/A0F7XDUAZ-incoming-webhooks) and not one inside a Slack app as suggested in Step 1. For some reason, Slack doesn't allow to override the App's username and icon.