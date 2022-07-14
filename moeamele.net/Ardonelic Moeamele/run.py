#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#
#-----------imports & froms-----------
from ast import Await
from cgi import test
from http import client
from pydoc import cli
from turtle import color, title
from unicodedata import name
from attr import has
from discord.ext import commands
from discord_components import Button, Select, SelectOption, ComponentsBot, interaction
from discord_components.component import ButtonStyle
import discord
import os
import datetime
from discord.ext import commands
import discord
from discord.ext import commands
from os import listdir
import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound, ChannelNotFound
from idna import check_nfc
import aiofiles
#-----------imports & froms-----------



#---------------CONFIG--------------
TOKEN = ""
PREFIX = "-"
#---------------CONFIG--------------



#--------------Client--------------
intents = discord.Intents.default()
client = ComponentsBot(f"{PREFIX}", intents=intents)
client.remove_command('help')
intents.members = True
#--------------Client--------------

#------------on_ready--------------
@client.event
async def on_ready():
    async with aiofiles.open("reaction_roles.txt", mode="a") as temp:
        pass
        
    async with aiofiles.open("reaction_roles.txt", mode="r") as file:
        lines = await file.readlines()
        for line in lines:
            data = line.split(" ")
            client.reaction_roles.append((int(data[0]), int(data[1]), data[2].strip("\n")))
    await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name=f"{PREFIX}""help"))
    print("bot is ready")
    print("coded by Ardonelic")
    print("for moamele.net")
#------------on_ready--------------

#-----------help command------------
@client.command()
async def help(ctx):
    embed = discord.Embed(title="how to use command !",color=0xFFFFFF)
    embed.add_field(name=f"{PREFIX}""ban (user)", value="this command for ban users", inline=True)
    embed.add_field(name=f"{PREFIX}""unban (user)", value="this command for unban users", inline=True)
    embed.add_field(name=f"{PREFIX}""kick (user)", value="this command for kick users", inline=True)
    embed.add_field(name=f"{PREFIX}""mute (user)", value="this command for mute users", inline=True)
    embed.add_field(name=f"{PREFIX}""unmute (user)", value="this command for unmute users", inline=True)
    embed.add_field(name=f"{PREFIX}""clear (amount)", value="this command for clear massages", inline=True)
    embed.add_field(name=f"{PREFIX}""ticket", value="this command for send a ticket embed", inline=True)
    embed.add_field(name=f"{PREFIX}""massage (text)", value="this command for send massage for announcement or reaction role massage", inline=True)
    embed.add_field(name=f"{PREFIX}""reaction (role name) (message id) (emoji)", value="this command for add reaction role to massages", inline=True)
    await ctx.send(embed = embed)
#-----------help command------------


#---------------ERROR---------------
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send("Please complete your message!")
    if isinstance(error, commands.MissingPermissions):
        await ctx.send("You do not have access to this command")
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send("Wait this command is in cooldown")
#---------------ERROR---------------


#-------------SelfRole---------

@client.command()
@commands.has_permissions(administrator=True)
async def message(ctx, *, massage):
    await ctx.send(massage)

client.reaction_roles = []
@client.command()
@commands.has_permissions(administrator=True)
async def reaction(ctx, role: discord.Role=None, msg: discord.Message=None, emoji=None):
    if role != None and msg != None and emoji != None:
        await msg.add_reaction(emoji)
        client.reaction_roles.append((role.id, msg.id, str(emoji.encode("utf-8"))))
        
        async with aiofiles.open("reaction_roles.txt", mode="a") as file:
            emoji_utf = emoji.encode("utf-8")
            await file.write(f"{role.id} {msg.id} {emoji_utf}\n")

        await ctx.channel.send("Reaction has been set.")
        
    else:
        await ctx.send("Invalid arguments.")

@client.event
async def on_raw_reaction_add(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            await payload.member.add_roles(client.get_guild(payload.guild_id).get_role(role_id))
            return

@client.event
async def on_raw_reaction_remove(payload):
    for role_id, msg_id, emoji in client.reaction_roles:
        if msg_id == payload.message_id and emoji == str(payload.emoji.name.encode("utf-8")):
            guild = client.get_guild(payload.guild_id)
            await guild.get_member(payload.user_id).remove_roles(guild.get_role(role_id))
            return
#-----------Self-Role--------------



#------------ticket-------------------
id_category = 995597153110065193
id_channel_ticket_logs = 996688107317502014
embed_color = 0xfcd005 


@client.command()
@commands.has_permissions(administrator=True)
async def ticket(ctx):
    await ctx.message.delete()


    embed = discord.Embed(title ='Tickets', description ='Welcome to Ardonelic tickets system.', color=embed_color) 


    embed.set_image(url='https://cdn.discordapp.com/attachments/995358672932843530/996853302006386768/reaxo_cover2.png')

    await ctx.send(
        embed = embed,

        components = [
            Button(
                custom_id = 'Ticket',
                label = "Create a ticket",
                style = ButtonStyle.green,
                emoji ='🔧')
        ]
    )


@client.event
async def on_button_click(interaction):

    canal = interaction.channel
    canal_logs = interaction.guild.get_channel(id_channel_ticket_logs)

    if interaction.component.custom_id == "Ticket":
        await interaction.send(

            components = [
                Select(
                    placeholder = "How can we help you?",
                    options = [
                        SelectOption(label="Question", value="question", description='If you have a simple question.', emoji='❔'),
                        SelectOption(label="Help", value="help", description='If you need help from us.', emoji='🔧'),
                        SelectOption(label="Report", value="report", description='To report a misbehaving user.', emoji='🚫'),
                    ],
                    custom_id = "menu")])



    elif interaction.component.custom_id == 'close_ticket':

        embed_cerrar_ticket = discord.Embed(description=f"⚠️ Are you sure you want to close the ticket?", color=embed_color)
        await canal.send(interaction.author.mention, embed=embed_cerrar_ticket, 
                        components = [[
                        Button(custom_id = 'close_yes', label = "Yes", style = ButtonStyle.green),
                        Button(custom_id = 'close_no', label = "No", style = ButtonStyle.red)]])


    elif interaction.component.custom_id == 'close_yes':

        await canal.delete()
        embed_logs = discord.Embed(title="Tickets", description=f"", timestamp = datetime.datetime.utcnow(), color=embed_color)
        embed_logs.add_field(name="Ticket", value=f"{canal.name}", inline=True)
        embed_logs.add_field(name="Closed by", value=f"{interaction.author.mention}", inline=False)
        embed_logs.set_thumbnail(url=interaction.author.avatar_url)
        await canal_logs.send(embed=embed_logs)


    elif interaction.component.custom_id == 'close_no':
        await interaction.message.delete()

@client.event
async def on_select_option(interaction):
    if interaction.component.custom_id == "menu":

        guild = interaction.guild
        category = discord.utils.get(interaction.guild.categories, id = id_category)


        if interaction.values[0] == 'question':

            channel = await guild.create_text_channel(name=f'❔┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)
                                                

            await interaction.send(f'> The {channel.mention} channel was created to solve your questions.', delete_after= 3)

            embed_question = discord.Embed(title=f'Question - ¡Hi {interaction.author.name}!', description='In this ticket we have an answer to your question.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question,
            

             components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])


        elif interaction.values[0] == 'help':

            channel = await guild.create_text_channel(name=f'🔧┃{interaction.author.name}-ticket', category=category)
            

            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)



            await interaction.send(f'> The {channel.mention} channel was created to help you.', delete_after= 3)

            embed_question = discord.Embed(title=f'Help - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with whatever you need.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)


            await channel.send(interaction.author.mention, embed=embed_question, 

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])



        elif interaction.values[0] == 'report':


            channel = await guild.create_text_channel(name=f'🚫┃{interaction.author.name}-ticket', category=category)


            await channel.set_permissions(interaction.guild.get_role(interaction.guild.id),
                            send_messages=False,
                            read_messages=False)
            await channel.set_permissions(interaction.author, 
                                                send_messages=True,
                                                read_messages=True,
                                                add_reactions=True,
                                                embed_links=True,
                                                attach_files=True,
                                                read_message_history=True,
                                                external_emojis=True)


            await interaction.send(f'> The {channel.mention} channel was created to report to the user.', delete_after= 3)


            embed_question = discord.Embed(title=f'Report - ¡Hi {interaction.author.name}!', description='In this ticket we can help you with your report.\n\nIf you cant get someone to help you, Only 1 time mention the staff for `🔔 Call staff`.', color=embed_color)
            embed_question.set_thumbnail(url=interaction.author.avatar_url)

            await channel.send(interaction.author.mention, embed=embed_question, 
            

            components = [[
                    Button(custom_id = 'close_ticket', label = "Close ticket", style = ButtonStyle.red, emoji ='🔐')]])
#------------ticket-------------------



#-----------cogs and run------------
for fn in os.listdir('./cogs'):
	if fn.endswith('.py'):
		client.load_extension(f"cogs.{fn[:-3]}")

client.run(TOKEN)
#-----------cogs and run------------

#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#