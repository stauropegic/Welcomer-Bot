# --------------------------------------------------------------------
# Welcome to Rests simple discord welcomer-bot!
# To setup just read the message with a "#" and follow what they say
# if you would like some help join discord.gg/vdWmnZW6Vc
# --------------------------------------------------------------------

import src


token = '' # --< Enter your discord bot token from https://discord.com/developers/home >--

prefix = '$' # --< Enter your custom prefix here. default $help >--

dm_user = True # --< Change this to true if you would like to dm people when they join >--

welcome_channel_id = 1234567890 # --< Replace numbers with the Channel ID from where you want the bot to message >--

src.main(token, prefix, dm_user, welcome_channel_id)
