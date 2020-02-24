import discord

client = discord.Client()


@client.event
async def on_ready():
    print(client.user.id)
    print("준비되었습니다!")
    game = discord.Game("GoGi NETWORK")
    await client.change_presence(status=discord.Status.online, activity=game)



@client.event
async def on_message(message):
    if message.content.startswith("!HoneyBOT"):
        await message.channel.send("허니가 직접 개발한 디스코드 봇 하지만 정말 저퀄리티이다.")
    if message.content == "안녕하세요":
        await message.channel.send("안녕하세요!")
    if message.content.startswith("!허니상태"):
        await message.channel.send("허니 계정은 살아있습니다. 삭제 안했어요.")



client.run("NjgwMDUwNzAxMDU2OTk5NDM5.Xk6Skg.k467eZCtSKi4x6ycfKbyZnk6vUE")