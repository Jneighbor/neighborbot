import discord
from discord.ext import commands

class custom:
        def __init__(self, bot):
        self.bot = bot
        
async def on_message(self, message):
    if message.content.startswith('Neighbor'):
        await self.send_message(message.channel, '@JNeighbor#0069')


        
def setup(bot):
    bot.add_cog(custom(bot))


    if message.content == '!activaterb':
        if rbcycle(message) == True:
            rbacstop = False
            print('Rainbow Role activated for Server \"' + str(message.server.name) + '\"')
            f = open(rbfn, "r")
            rbid = str(f.readlines())
            rbid = rbid.translate(trtlrunpass)
            for role in message.server.roles:
                if role.id == rbid:
                    f.close()
                    while rbcycle(message) == True and rbacstop == False:
                        try:
                            if role.color == rolered:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=roleorange)
                            if role.color == roleorange:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=roleyellow)
                            if role.color == roleyellow:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=rolegreen)
                            if role.color == rolegreen:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=roleblue)
                            if role.color == roleblue:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=rolepurple)
                            if role.color == rolepurple:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=rolered)
                            if role.color == roledefault:
                                time.sleep(0.3)
                                await client.edit_role(server=message.server, role=role, color=rolered)
                        except:
                            await client.send_message(message.server,"BonesBot does not have permissions to activate the rainbow effect (This is usually when the role is higher ranking than BonesBot)")
                            rbacstop = True