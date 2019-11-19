import discord
import asyncio
import segredo
import random

#from sklearn.svm import LinearSVC
#modelo = LinearSVC

tokenid = segredo.seu_token()
COR =0x690FC3
client = discord.Client()
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('BOT ONLINE')
    print(client.user.name)
    print(client.user.id)
    print('------------------------')

@client.event
async def on_message(message):
    if message.content.lower().startswith('?suki'):
        channel = message.channel
        await channel.send("I like you!.")

    if message.content.lower().startswith('?dado'):
        choice = random.randint(1,6)
        channel = message.channel
        enviar = channel.send
        num = choice
        up = 'UP!', num
        down = 'DOWN!', num
        if choice >= 4:
            await enviar(up)
        if choice <= 3:
            await enviar(down)

    if message.content.lower().startswith('?cargo'):
        embed =discord.Embed(
            title="I Like ?",
            color=COR,
            description="- Osu!Player 🕹\n"
                        "- OtakuFUDIDO! 💎\n"
                        "- +18! 🔞"
        )
        channel = message.channel
        enviar = channel.send
        botmsg = await enviar(embed=embed)
        await discord.Message.add_reaction(botmsg, "🕹")
        await discord.Message.add_reaction(botmsg, "💎")
        await discord.Message.add_reaction(botmsg, "🔞")

        global msg_id
        msg_id = botmsg.id
        global msg_user
        msg_user = message.author

#    if message.content.lower().startswith('!rodar'):
 #       # HighRank, Streamer, Noob
  #      player1 = [1,1,0]
   #     player2 = [1,0,0]
    #    player3 = [0,1,1]
     #   player4 = [0,0,0]
     #   #Player Bom, Player ruim
      #  teste_x= [player1, player2, player3, player4]
      #  teste_y= [1,1,0,0]
     #   modelo.fit(teste_x,teste_y)
    #    previsao = modelo.predict(teste_x)
   #     previsao
  #      channel = message.channel
 #       await channel.send(previsao)


#@client.event
#async def on_message(message):
#    if message.content.startswith('!entrar'):
#
 #       canal = message.author.voice.channel
  #      await channel.conect(canal)

client.run(tokenid)