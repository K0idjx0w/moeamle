#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#

#---------froms & imports-----------
import discord
from discord.ext import commands
#---------froms & imports-----------

#--------class cogs-----------
class Welcome(commands.Cog):
    def __init__(self, client):
        self.client=client
#--------class cogs-----------

#---------code--------------
    @commands.Cog.listener()
    async def on_member_join(self, member):
        guild = self.client.get_guild(995597152564809768)
        channel = discord.utils.get(member.guild.channels, id=995597153110065194)
        await channel.edit(name = f'member: {guild.member_count}')



    @commands.Cog.listener()
    async def on_member_leave(self, member):
        guild = self.client.get_guild(995597152564809768)
        channel = discord.utils.get(member.guild.channels, id=995597153110065194)
        await channel.edit(name = f'member: {guild.member_count}')
#---------code--------------


#--------setup cogs---------
def setup(client):
    client.add_cog(Welcome(client))
#--------setup cogs---------

#-------------------------------------#
#                                     #
#                                     #
#          CODE BY ARDONELIC          #
#                                     # 
#                                     #
# ------------------------------------#