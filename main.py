import discord
import time
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
@client.event
async def on_ready():
    print(f'Hemos iniciado sesión como {client.user}')
    
@client.event
async def on_message(message):
    with open('cans/image.png','rb') as f:
        picture1 = discord.File(f)
    with open('cans/image2.png','rb') as f:
        picture2 = discord.File(f)
    with open('cans/image3.jpg','rb') as f:
        picture3 = discord.File(f)
    with open('cans/mario.jpg','rb') as f:
        picture4 = discord.File(f)
    with open('cans/star-good.jpg','rb') as f:
        picture5 = discord.File(f)
    with open('cans/star-bad.png','rb') as f:
        picture6 = discord.File(f)
    if message.author == client.user:
        return
    if message.content.startswith('hello'):
        await message.channel.send("Hi!, tell me what is your problem? (USE: My problem is:)")
    elif message.content.startswith('My problem is: I do not know how to reycle'):
        await message.channel.send("Ok first create three cans one green, one black and one white")
        await message.channel.send(file=picture1)
        await message.channel.send("This is the green can with this one you can recycle things about food...")
        await message.channel.send("Now is the white can, in this can you can throw bottles, plastic and those things")
        await message.channel.send(file=picture2)
        await message.channel.send("Finaly this is the black can, in this can you put all trash that is useless E.G: napkin")
        await message.channel.send(file=picture3)
    elif message.content.startswith('What is your name and how you help the planet?'):
        await message.channel.send("My name is CoCo and I'm your assistant to know things about planet")
    elif message.content.startswith('play'):
        await message.channel.send("Ok, let's start: (Now see the terminal please)")
        time.sleep(2)
        recycle = input("Which thing you want to recycle CHOOSE Food/Plastic/Trash: ")
        await message.channel.send("You Choose:")
        await message.channel.send(recycle)
        time.sleep (3)
        if recycle == "Food":
            answer = input("What bin you do think goes things about food? ")
            await message.channel.send("Your answer:")
            await message.channel.send(answer)
            await message.channel.send(file=picture4)
            time.sleep(3)
            if answer=="green can":
                await message.channel.send("correct!!!")
                await message.channel.send(file=picture5)
            else:
                await message.channel.send("incorrect!!!, The answer is green can")
                await message.channel.send(file=picture6)
        time.sleep (3)
        if recycle == "Plastic":
            answer = input("What bin you do think goes things about plastic? ")
            await message.channel.send("Your answer:")
            await message.channel.send(answer)
            await message.channel.send(file=picture4)
            time.sleep(3)
            if answer == "white" or "white can":
                await message.channel.send("correct!!!")
                await message.channel.send(file=picture5)
            else:
                await message.channel.send("incorrect!!!, The answer is green can")
                await message.channel.send(file=picture6)
        time.sleep (3)
        if recycle == "Trash":
            answer = input("What bin you do think goes things about trash? ")
            await message.channel.send("Your answer:")
            await message.channel.send(answer)
            await message.channel.send(file=picture4)
            time.sleep(3)
            if answer == "black" or "black can":
                await message.channel.send("correct!!!")
                await message.channel.send(file=picture5)
            else:
                await message.channel.send("incorrect!!!, The answer is green can")
                await message.channel.send(file=picture6)
    else:
        await message.channel.send("This word doesn't work try other")
client.run("Token")
