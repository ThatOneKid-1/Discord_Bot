import discord
from discord.ext import commands
import random

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix = '?', intents=intents)
#creates embed. ^is the prefix
frog = discord.Embed(title=':frog: Kermit :frog:')
poster = discord.Embed(title=':dollar: *CASH PRIZE* :dollar:')
monkee = discord.Embed(title= ':banana: :monkey: M O N K E')

@bot.event 
async def on_ready():
    print("Bot Online!")
    print(bot.user.name)
    print(bot.user.id)
    print('------')


@bot.command()
async def kermit_help(ctx):
    await ctx.send('Commands: \n?kermit, \n?wanted, \n?monke')

@bot.command()
async def kermit(ctx):
    await ctx.send('Fetching Kermit...')
    #Kermit pictures below
    frogs = ['https://cdn.discordapp.com/attachments/765612760478121999/769330175544000522/intro-1601411424.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330176622067742/KermitBeinGreenTMS.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330210792407040/kisspng-kermit-the-frog-miss-piggy-telegram-the-muppets-st-kermit-s-swamp-years-5b1b67b8b1cbf9.15637.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330174872256552/flat750x075f-pad750x1000f8f8f8.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330173417619506/evil-kermit-the-frog-meme-dark-side_2.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330171694022656/download-_1_.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330171022802973/91e4cefc-d8bc-47e5-be13-c0f226520569.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330170573619200/download.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330169776832514/220px-Kermit_the_Frog.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769330165125742632/7ad7094f6267512e8b486f85f9c9d9f2.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769327060636008498/Kermit-the-Frog-Featured.jpg', 
            'https://cdn.discordapp.com/attachments/765612760478121999/769327057574297620/intro-1601411424.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769386962473058354/kpic.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769386923566956574/KermitBeinGreenTMS.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769386899247726632/ezgif.com-gif-maker.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769386871591010324/26789e89c810065bcc629b15b42ba6f4.jpg',
            'https://cdn.discordapp.com/attachments/765612760478121999/769386397605167174/muppets-kermit-bar-700x300.jpg']
    frog.set_image(url=(random.choice(frogs)))
    #below sends embed
    await ctx.send(embed=frog)

@bot.command()
async def wanted(ctx):
    await ctx.send('Fetching Your Poster...')
        #Wanted posters
    posters = ['https://media.discordapp.net/attachments/775854085906890782/775856652418678834/image0.png?width=411&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854988672106496/image0.png?width=416&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854333098590258/image2.png?width=411&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854332822159370/image1.png?width=418&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854332590817315/image0.png?width=470&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854331114422272/image9.png?width=411&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854330850050058/image8.png?width=415&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854330577813514/image7.png?width=413&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854330292076574/image6.png?width=409&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854330095599646/image5.png?width=411&height=586',
            'https://media.discordapp.net/attachments/775854085906890782/775854329872515142/image4.png?width=418&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854329642090496/image3.png?width=420&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854329366052896/image2.png?width=415&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854329130254366/image1.png?width=415&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854328945967144/image0.png?width=416&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854285086785546/image9.png?width=410&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775854284591333407/image8.png?width=413&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854284205588540/image7.png?width=421&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854283660197918/image5.png?width=418&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775854282817667082/image2.png?width=421&height=586',
            'https://media.discordapp.net/attachments/775854085906890782/775854282569547776/image1.png?width=416&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775859099392409630/image0.png?width=420&height=584',
            'https://media.discordapp.net/attachments/775854085906890782/775859359573999676/image0.png?width=424&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775859462946816000/image0.png?width=419&height=585',
            'https://media.discordapp.net/attachments/775854085906890782/775860030132977684/image0.png?width=410&height=585',]
    poster.set_image(url=(random.choice(posters)))
    
    await ctx.send(embed=poster)

@bot.command()
async def monke(ctx):
    #monke gif(find way to make actual video at some point)
    #https://cdn.discordapp.com/attachments/806920676371333221/823637617525653544/gorilla.mp4
    monkee.set_image(url='https://media.giphy.com/media/IbGi9aRgaIWzm0WlaB/giphy.gif')

    await ctx.send(embed=monkee)

@bot.event
async def on_member_join(member):
    await member.send('This server built different\n...\nalso read the rules')



bot.run('NzY1NjExNTk3MTM2NjU4NDkz.X4XVXQ.-y6Itn3rskLtwItUfpEhlVjei20')