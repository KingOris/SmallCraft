from discord.ext.commands import Bot

Bot_Prefix = ("?", "~")
TOKEN = "NTQ3Nzg5NDc1NjE5NjY3OTY4.D074TA.prQuRmkUINB7jHe-4Uu6upRPD94"

client = Bot(command_prefix=Bot_Prefix)
guild_name_list = []

"""""
g_l_file = open("GuildName", "r")
gnames = g_l_file.readline()
while gnames:
    guild_name_list.append(gnames)
    gnames = g_l_file.readline()
g_l_file.close()
"""""

"""""
@client.command(name='hunting',
                description="Show bounty hunting list",
                brief="Show hunting list"
                )
#async def hunting():
    for HuntingDic in listHunting:
        await client.say('Guild' + ' ' + HuntingDic.guild + ' ' + 'CharacterName' + ' ' + HuntingDic.name)
"""""
client.run(TOKEN)
