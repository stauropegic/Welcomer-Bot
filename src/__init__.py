# Made by rest
import os
import sys
import discord
from discord.ext import commands

def main(token, prefix, dm_user, welcome_channel_id):
    '''
    This is just version 1.0.0 of this tool
    Last updated  11/07/2026 13:50:00 AEST 
    '''
    intents = discord.Intents.default()
    intents.members = True
    intents.message_content = True

    bot = commands.Bot(
        command_prefix=prefix,
        intents=intents,
        help_command=None
    )

    def clear():
        os.system('cls' if os.name == 'nt' else 'clear')


    @bot.event
    async def on_ready():
        clear()
        print('Discord Welcomer  >>  made by Rest\n')
        print(f'Logged in as {bot.user}')
        print(f'Current prefix: {prefix}')
        print(f'Channel ID: {welcome_channel_id}')
        channel = bot.get_channel(welcome_channel_id)
        print(f'Channel Name: {channel}')


    @bot.event
    async def on_member_join(member):
        print(f'{member.name} joined!')

        channel = bot.get_channel(welcome_channel_id)

        if channel:
            await channel.send(
                f'Welcome {member.mention} to {member.guild.name}!'
            )
        else:
            print('error: Welcome channel not found.')

        if dm_user:
            try:
                await member.send(
                    f'Welcome to {member.guild.name}!'
                )
            except (discord.Forbidden, discord.HTTPException) as error:
                print(f'Could not DM {member}: {error}')
    
    @bot.command()
    async def help(ctx):
        await ctx.send(f'''
Hello {ctx.author}! 

If you would like some assistence, 
join discord.gg/vdWmnZW6Vc and open a ticket!

An admin or staff will be with you shortly. 
just explain the error and they can help.

- Rest
        ''')



    bot.run(token)