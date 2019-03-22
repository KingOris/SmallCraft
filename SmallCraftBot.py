import discord
import asyncio
from discord.ext import commands

Bot_Prefix = ("?", "~")
TOKEN = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"

client = commands.Bot(command_prefix=Bot_Prefix)
status = ['Msg1', 'Msg2', 'Msg2']
client.remove_command('help')


@client.event
async def on_ready():
    await client.change_presence(game=discord.Game(name='挂機修仙'))
    print("Ready")


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='DJ')
    await client.add_roles(member, role)


@client.event
async def on_message(message):
    author = message.author
    content = message.content
    print('{}:{}'.format(author, content))
    await client.process_commands(message)


@client.command()
async def ping():
    await client.say('Poing!')


@client.command()
async def echo(*args):
    output = ''
    for word in args:
        output += word
        output += ''
    await client.say(output)


@client.command(pass_context=True)
async def clear(ctx, amount=100):
    channel = ctx.message.channel
    messages = []
    async for message in client.logs_from(channel, limit=int(amount)):
        messages.append(message)
    await client.delete_messages(messages)
    await client.say('Message deleted.')


@client.command()
async def displayembed():
    embed = discord.Embed(
        title='Title',
        description='This is a description',
        colour=discord.Colour.blue()
    )
    embed.set_footer(text='This is a footer')
    embed.set_image(url='https://discordapp.com/channels/514313533454811136/514313533454811138/558349352272134156')
    embed.set_thumbnail(url='https://discordapp.com/channels/514313533454811136/514313533454811138/558349352272134156')
    embed.set_author(name='Name', icon_url='https://discordapp.com/channels/514313533454811136/514313533454811138/558349352272134156')
    embed.add_field(name='Field', value='Field Value', inline=False)
    embed.add_field(name='Field', value='Field Value', inline=True)
    embed.add_field(name='Field', value='Field Value', inline=True)

    await client.say(embed=embed)


@client.event
async def on_message_delete(message):
    author = message.author
    content = message.content
    channel = message.channel
    await client.send_message(channel, '{}:{}'.format(author, content))


@client.command(pass_context=True)
async def help(ctx):
    author = ctx.message.author

    embed = discord.Embed(
        color= discord.Color.orange()
    )

    embed.set_author(name='Help')
    embed.add_field(name='.', value='value', inline=True)

    await client.send_message(author, embed=embed)


@client.event
async def on_reaction_add(reaction, user):
    channel = reaction.message.channel
    await client.send_message(channel, '{} has added {} to the message:{}'.format(user.name, reaction.emoji, reaction.message.content))


@client.command(pass_context=True)
async def join(ctx):
    channel = ctx.message.author.voice.voice_channel
    await client.join_voice_channel(channel)


@client.command(pass_context=True)
async def at(ctx):
    user = ctx.message.author
    name = ctx.message.content
    message = name[4:]
    for i in range(10):
        await client.say(message)
        await asyncio.sleep(0.1)



@client.command(pass_context=True)
async def leave(ctx):
    server = ctx.message.server
    voice_client = client.voice_client_in(server)
    await voice_client.disconnect()

client.run(TOKEN)
