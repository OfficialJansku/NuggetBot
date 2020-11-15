# Import packages
import discord
from discord.ext import commands
# ---------------

# Client for the bot

client = commands.Bot(command_prefix='!')
# ---------------

@client.command(name='version')
async def version(context):
        print('here')
        myEmbed = discord.Embed(title="Current Version", description="This build is version 1.0", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="1.0.0", inline=False)
        myEmbed.add_field(name="Date Released:", value="November 15th, 2020", inline=False)
        myEmbed.set_footer(text="If you want to try this bot, please type !sourcecode to clone this.")
        myEmbed.set_author(name="JANSKU")

        await context.message.channel.send(embed=myEmbed)


@client.command(name='react')
async def react(context):
    await context.message.channel.send('No Michael, unfortunately this not running on React you fkn nugget')

@client.command(name='sourcecode')
async def sourcecode(context):

        myEmbed = discord.Embed(title="NuggetBot.py", description="NuggetBot.py sourcecode on GitHub", color=0x00ff00)
        myEmbed.add_field(name="Github-link:", value="https://github.com/OfficialJansku/NuggetBot.git", inline=False)
        myEmbed.add_field(name="Bot version:", value="V1.0.0", inline=False)
        myEmbed.set_author(name="JANSKU")

        await context.message.channel.send(embed=myEmbed)


@client.event
async def on_ready():

    # Do stuff

    general_channel = client.get_channel('your channel id here')
    await general_channel.send('Hello World!')

# ---------------


# Run the client on the server
client.run('your client id here')
# ---------------