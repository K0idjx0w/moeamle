#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#


#---------froms & imports-----------
import discord
import os
import datetime
import asyncio
from discord.ext import commands
#---------froms & imports-----------


#--------class cogs-----------
class mod(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
#--------class cogs-----------


#----------commands-----------


	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def clear(self, ctx, amount=6):
		await ctx.channel.purge(limit=amount)
		embed = discord.Embed(title=f"{amount} messages has been cleared!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
		await ctx.send(embed=embed)



	            
	@commands.command()
	@commands.has_permissions(manage_messages=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def mute(self, ctx, member: discord.Member, *, reason=None):
	    guild = ctx.guild
	    mutedRole = discord.utils.get(guild.roles, name="Muted")

	    if not mutedRole:
	        mutedRole = await guild.create_role(name="Muted")

	        for channel in guild.channels:
	            await channel.set_permissions(mutedRole, speak=False, send_messages=False, read_message_history=True, read_messages=False)
	    embed = discord.Embed(title="Muted", description=f"{member.mention} was muted ", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    embed.add_field(name="Reason:", value=reason, inline=False)
	    await ctx.reply(embed=embed)
	    await member.add_roles(mutedRole, reason=reason)


	@commands.command()
	@commands.cooldown(1, 5, commands.BucketType.guild)
	@commands.has_permissions(manage_messages=True)
	async def unmute(self, ctx, member: discord.Member):
	    mutedRole = discord.utils.get(ctx.guild.roles, name="Muted")

	    await member.remove_roles(mutedRole)
	    embed = discord.Embed(title="Unmute", description=f"Unmuted {member.mention}", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
	    await ctx.reply(embed=embed)

	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def kick(self, ctx, member: discord.Member, *, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Kicked!", description=f"{member.mention} has been kicked!!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.kick(user=member)


	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def ban(self, ctx, member: discord.Member, *, reason="No Reason"):
		if member == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)
		else:
			guild = ctx.guild
			embed = discord.Embed(title="Banned!", description=f"{member.mention} has been banned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			embed.add_field(name="Reason: ", value=reason, inline=False)
			await ctx.reply(embed=embed)
			await guild.ban(user=member)



	@commands.command()
	@commands.has_permissions(kick_members=True)
	@commands.cooldown(1, 5, commands.BucketType.guild)
	async def unban(self, ctx, user: discord.User):
		if user == None:
			embed = discord.Embed(f"{ctx.message.author}, Please enter a valid user!")
			await ctx.reply(embed=embed)

		else:
			guild = ctx.guild
			embed = discord.Embed(title="Unbanned!", description=f"{user.display_name} has been unbanned!", colour=discord.Colour.blue(), timestamp=datetime.datetime.utcnow())
			await ctx.reply(embed=embed)
			await guild.unban(user=user)

#----------commands-----------





#--------setup cogs---------
def setup(bot):
	bot.add_cog(mod(bot))
#--------setup cogs---------

#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#