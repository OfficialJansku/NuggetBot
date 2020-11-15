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
        myEmbed = discord.Embed(title="Current Version", description="This build is version 1.0.1", color=0x00ff00)
        myEmbed.add_field(name="Version Code:", value="1.0.1", inline=False)
        myEmbed.add_field(name="Date Released:", value="November 15th, 2020", inline=False)
        myEmbed.set_footer(text="If you want to try this bot, please type !sourcecode to clone or inspect this.")
        myEmbed.set_author(name="JANSKU")

        await context.message.channel.send(embed=myEmbed)


@client.command(name='react')
async def react(context):
    await context.message.channel.send('No Michael, unfortunately this not running on React you fkn nugget')

@client.command(name='sourcecode')
async def sourcecode(context):

        myEmbed = discord.Embed(title="NuggetBot.py", description="NuggetBot.py sourcecode on GitHub", color=0x00ff00)
        myEmbed.add_field(name="Github-link:", value="https://github.com/OfficialJansku/NuggetBot.git", inline=False)
        myEmbed.add_field(name="Bot version:", value="V1.0.1", inline=False)
        myEmbed.set_author(name="JANSKU")

        await context.message.channel.send(embed=myEmbed)

@client.command(name='commands')
async def commands(context):

    myEmbed = discord.Embed(title="Help for commands", description="All NuggetBot.py commands and description for them.", color=0x00ff00)
    myEmbed.add_field(name="`version`", value="```tells the build version of current NuggetBot.py version what its running on.```", inline=False)
    myEmbed.add_field(name="`sourcecode`", value="```Gives you link to Github-project page, where you can inspect the code or just clone it.```", inline=False)
    

    await context.message.channel.send(embed=myEmbed)


@client.command(name='bot')
async def bot(context):

    myEmbed = discord.Embed(title="BOT FAQ For newbies.", description="Help with setting up the bot on your server and for overall use", color=0x00ff00)
    myEmbed.add_field(name="`Installation`", value="```1. Download the bot sourcecode from github.\n 2. Add bot on Discord developer portal to your server (Don't forget to use Discord API permission calculator!) \n 3. Download VSCode, if you don't have it already. \n 4. Add necessary id's for the channels. \n 5. Debug and Enjoy.```", inline=False)
    myEmbed.add_field(name="`Using NuggetBot.py on other servers`", value="```Feel free to clone the project, ***but stealing it and calling it as your own work is strictly prohibited***```", inline=False)
    myEmbed.add_field(name="`Requirements for NuggetBot.py`", value='- Python3 installed to your system. \n Windows installation:', inline=False)
    myEmbed.add_field(name="Python3 link", value="https://www.python.org/downloads/windows/", inline=False)
    myEmbed.add_field(name="Linux installation", value="```$ sudo apt-get update \n $ sudo apt-get install python3```", inline=False)
    myEmbed.add_field(name="Extra packages", value="Python extensions installation for Windows", inline=False)
    myEmbed.add_field(name="Windows Installation", value="```pip3 install discord```", inline=False)
    myEmbed.add_field(name="Extra packages", value="Python extensions installation for Linux", inline=False)
    myEmbed.add_field(name="Linux Installation", value="```$ sudo pip3 install discord```", inline=False)
    myEmbed.add_field(name="Have difficulties with installation or in use?", value="DM me for more info or check Github page.", inline=False)
    

    await context.message.channel.send(embed=myEmbed)




@client.event
async def on_ready():

    # Do stuff

    await client.change_presence(status=discord.Status.do_not_disturb, activity=discord.Game('use !help for help with commands, and NuggetBot.py project can be found with !sourcecode'))


# ---------------

# Run the client on the server
client.run('your client id here')
# ---------------