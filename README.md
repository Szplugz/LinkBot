# LinkBot

A Discord Bot that creates Zoom and Google meeting links directly through Discord. As of now, the bot needs to be hosted locally on at least one user's machine, so you'll need to clone the repository and create a new bot application before you can invite the bot to your servers and use it. I plan to host it virtually in the near future and eliminate the need to clone the repo and create multiple bots.

## Setup

Clone the git repository, move into the repo's directory if necessary, and install the requirements (through the command line, as follows):
```shell
git clone https://github.com/Szplugz/LinkBot/
cd LinkBot
pip install -r requirements.txt
```
And make sure you have python 3 and ```pip``` installed.  
\
Next, you'll need to create a ```.env``` file in the bot's directory. The environment file will store your zoom authorization variables and the token for your Discord bot. You should start by [creating a bot account on discord](https://discordpy.readthedocs.io/en/latest/discord.html). Once you've invited the bot to your server and copied the token, paste it into the ```.env``` file.  
\
Finally, you need to grab your API Key and Secret from Zoom. Do this by going to https://developers.zoom.us and click on 'Build app'. Create a JWT app and from the 'App Credentials' tab, copy your API Key and API Secret and paste them into the ```.env``` file, which should now look like this:
```
token='your_discord_token'
key='your_api_key'
secret='your_api_secret'
```  
That's it! You can now run the program from the command line
```shell
python main.py
```
and you should see the bot come online in your server.

## Commands

The current commands are listed below:  
\
```$new zoom``` - generates a Zoom Meeting link.\
```$new gmeet``` - generates a Google Meet link.\
```$changeprefix {prefix}``` - changes the bot prefix to whichever character you type.  
\
~~I plan to add more functionality in the future.

Linkbot is deprecated. It will remain in this adolescent, unfulfilled state for eternity. There is nothing anyone can do about it.
