<img width="964" height="477" alt="image" src="https://github.com/user-attachments/assets/66ff2822-5898-4ce3-b973-58960e7aeb63" />


# Discord Welcomer Bot

A simple Discord welcome bot made with Python and `discord.py`.

This bot automatically welcomes new members when they join your Discord server. It can:

* Send a welcome message in a chosen channel
* Send a welcome DM to new members (optional)
* Use custom prefixes

---


# Installation Guide

## 1. Requirements

Before installing, make sure you have:

### Python

Download Python from:

https://www.python.org/downloads/

During installation, make sure you tick:

```
Add Python to PATH
```

To check if Python installed correctly, open Command Prompt and run:

```bash
python --version
```

You should see something like:

```
Python 3.12.x
```

---

## 2. Download the Bot

Clone the repository:

```bash
git clone https://github.com/stauropegic/Welcomer-Bot.git
```

or download the repository as a ZIP file from GitHub.

Extract the files and open the folder.

---

## 3. Install Dependencies

Open Command Prompt / Terminal inside the bot folder.

Install the required Python packages:

```bash
pip install discord.py
```

---

# Discord Bot Setup

## 1. Create a Discord Application

Go to the Discord Developer Portal:

https://discord.com/developers/applications

Click:

```
New Application
```

Give your bot a name and create it.

---

## 2. Create the Bot User

Go to:

```
Bot -> Add Bot
```

Confirm the creation.

---

## 3. Enable Required Intents

In the Bot settings, enable:

```
Server Members Intent
Message Content Intent
```

These are required for:

* Detecting new members
* Reading commands

---

## 4. Invite the Bot

Go to:

```
OAuth2 -> URL Generator
```

Select:

### Scopes

```
bot
```

### Bot Permissions

Enable:

```
Send Messages
Read Message History
View Channels
```

For full functionality, you may also enable:

```
Manage Messages
```

Copy the generated URL and open it in your browser.

Select your server and invite the bot.

---

# Configuration

Open:

```
start.py
```

Find the section where the bot is started.

You will need:

* Bot token
* Command prefix
* Welcome channel ID
* DM settings

---

## Getting Your Bot Token

Go to:

```
Discord Developer Portal
-> Your Application
-> Bot
-> Reset Token
```

Copy the token.

---

## Getting a Channel ID

Enable Developer Mode in Discord:

```
User Settings
-> Advanced
-> Developer Mode
```

Then:

1. Right click your welcome channel
2. Click:

```
Copy Channel ID
```

Use that ID in your configuration.

---

# Running the Bot

Start the bot with:

```bash
python start.py
```

If everything is configured correctly, you should see:

```
Discord Welcomer >> made by Rest

Logged in as YourBotName
```

Your bot is now online.

---

# Troubleshooting

## "ModuleNotFoundError: No module named 'discord'"

Install dependencies again:

```bash
pip install -r requirements.txt
```

---

## Bot is online but does not welcome users

Check:

* Server Members Intent is enabled
* The bot has permission to send messages
* The channel ID is correct

---

## Command does not work

Check:

* Message Content Intent is enabled
* The prefix is correct
* The bot has permission to read messages

---

## Invalid Token Error

If you see:

```
discord.errors.LoginFailure
```

Your token is incorrect.

Generate a new token from the Discord Developer Portal.

---

# Updating the Bot

Download the latest changes:

```bash
git pull
```

Then reinstall dependencies:

```bash
pip install -r requirements.txt
```

---

# Contributing

Suggestions, bug reports, and improvements are welcome.

Open an issue or submit a pull request.

---

# License

This project is open source. Feel free to modify it for your own Discord server.

---

Made by Rest -> https://taunt.rest
