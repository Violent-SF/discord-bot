import discord
import random
import io
import safygiphy
import datetime
import requests
from bs4 import BeautifulSoup
import bs4
import urllib.request
from html.parser import HTMLParser
from urllib.request import urlopen



client = discord.Client()
apathyid = "398203613031170049"
jinid = "375938120711143425"
xtenid = "390961220913725440"
g = safygiphy.Giphy()

players = {"375986797701758986": "YOUTUBE_PLAYER", "KEYWORD": 5, "Hallo": "Hello"}



@client.event
async def on_ready():
    print('Eingeloggt als')
    print(client.user.name)
    print(client.user.id)
    print('-----------')
    #print(sys.version)



@client.event
async def on_message(message):

    hardshipbot = "408965212750872576"
    i = 0
    s = 0
    datum = {}
    name = {}
    mention = {}
    usar = {}
    anzeigename = {}
    channelname = {}
    tauschdatum = ""
    tauschname = ""
    vogel = ["4bK06.jpg", 'APKgM.jpg', 'KfjMo.jpg', 'FHlFQ.png', '5ZTTG.jpg', 'DVhG5.png', 'lT6jg.jpg', 'odGtW.jpg', 'wevfe.jpg', '7Ovpk.jpg', 'pakQ3.jpg', 's8Ad2.jpg', 'scorb.jpg', '3Mkdf.jpg', 'oBvDk.jpg', 'ZTWku.jpg', 'nanii.png', 'JMIyP.jpg', 'BPHoI.jpg', 'HQ61q.jpg', 'KaJsn.jpg', '18ttm.png', 'o1U0p.jpg', 'rvv5l.jpg', 'f3aq2.jpg', '4TJYG.jpg', 'VsfTW.jpg', '6S0ap.jpg', 'VFInY.jpg', 'VQsCr.jpg', 'pZxNq.jpg', 'WF4xW.jpg', 'CeE9j.jpg', '7j0Db.jpg', 'DhF1K.jpg', 'qH0GM.png', 'ehu5e.jpg', 'PNO3S.jpg', 'BSwVX.jpg', 'otfEo.jpg', '8xg7P.jpg', 'HlVjd.jpg', 'Uq14D.jpg', 'vKJHQ.jpg', 'owwoY.jpg', '6oH9o.jpg', 'OhWk2.jpg', 'YSbJ6.jpg', 'IHSpy.jpg', 'Yn1hS.jpg', 'KfeXt.jpg', 'QlTMv.jpg', 'S2pqj.jpg', '8aWd3.png', 'rU3KZ.jpg', 'eDRuj.jpg', 'BtXqx.jpg', 'vm09R.png', 'eXuUh.jpg', 'jQdMr.jpg', 'blerb.jpg', 'Cqq8h.jpg', 'ybuGM.jpg', 'd59U0.jpg', 'gu3K9.jpg', 'zHmeY.jpg', 'mc67B.jpg', 'MgZqv.jpg', 'smool.jpg', 'gjpzv.jpg', 'n8Zyq.jpg', 'hCFo5.jpg', 'Fj58w.png', 'r59mz.png', 'TDM1c.jpg', 'rWgdD.jpg', 'CSeoo.jpg', 'tfAer.jpg', 'Csr9T.jpg', 'KrTpt.jpg', 'uEL6i.jpg', '6eLxT.jpg', 'ITIuN.jpg', 'KYmD0.jpg', 'KC7D6.jpg', 'Pq53u.jpg', 'flsWa.jpg', 'HAQ3m.jpg', 'wU61L.jpg', 'myU5c.jpg', 'tpAqO.jpg', '7hDNc.jpg', 'tcWY9.jpg', 'vHtW9.jpg', '3o0qh.jpg', 'OjseH.jpg', 'R37AZ.jpg', 'EBQPX.jpg', '6YeiT.jpg', 'QKcy3.png', 'rOfHo.jpg', 'o1PKk.jpg', 'T1KgG.jpg', 'zpk0t.jpg', '3q221.png', 'hRGpM.jpg', '9wnTO.jpg', 'WtzSU.jpg', 'm5tha.jpg', 'DVNCS.jpg', '41vo6.jpg', 'lGwUk.jpg', 'HDkHq.png', 'PN5on.jpg', '08Dux.jpg', 'e2BRx.jpg', 'qLnlt.jpg', 'PUcUE.jpg', '9c4c1.jpg', 'BfAeJ.jpg', 'AXS3z.jpg', 'baBkv.png', 'SOiSK.jpg', 'sk5tl.jpg', 'wwnyK.png', '6LGJN.jpg', 'lraRw.jpg', 'fckdS.jpg', 'OnAyQ.jpg', 'hcEcH.jpg', 'a8Lrx.jpg', 'tv3eD.jpg', 'scaDn.jpg', '6RI3z.png', 'cOGrD.jpg', 'A9LPD.jpg', 'CipND.png', '4oB5J.jpg', 'DQG7f.jpg', '3PPFa.jpg', 'apmmW.jpg', 'VZYUf.jpg', 'hQ0U4.jpg', 'Obv4p.jpg', 'OVPqy.jpg', '3mFtf.png', 'XxNAa.jpg', 'yA3GA.jpg', 'VDVji.jpg', 'SXgZp.jpg', 'gN2eO.png', 't89l7.jpg', 'yTuOs.jpg', 'AcAZE.jpg', '1sGvE.jpg', 'badfa.jpg', '6boJq.jpg', 'kJBTm.jpg', 'l9M5w.jpg', 'TF2CK.jpg', '5EbEm.jpg', '1dERc.jpg']
    #162 !!

    if message.content.lower().startswith('!test'):
        await client.send_message(message.channel, "Test bestanden!!!!!")


    if message.content.startswith('!game') and message.author.id == apathyid or message.content.startswith('!game') and message.author.id == jinid:
        game = message.content[6:]
        await client.change_presence(game=discord.Game(name=game))


    if message.content.startswith('!gif'):
        gif_tag = message.content[5:]
        rgif = g.random(tag=str(gif_tag))
        response = requests.get(
            str(rgif.get("data", {}).get('image_original_url')), stream=True
        )
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='video.gif')

    if message.content.lower().startswith('!cat'):

        i = random.randint(1,1283)
        x = str(i)
        site = 'http://random.cat/view?i=' + x

        response = requests.get(site)

        soup = BeautifulSoup(response.text, 'html.parser')
        img_tags = soup.find_all('img')

        urls = [img['src'] for img in img_tags]

        url1 = str(urls).split("'")[1]

        richtigeurl = "http://random.cat/" + url1

        response = requests.get(richtigeurl, stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='bild.png')

    if message.content.lower().startswith('!bird'):

        i = random.randint(0,162)
        urlende = vogel[i]
        site = "https://random.birb.pw/img/" + urlende

        with open('vogel.jpg', 'wb') as handle:
            response = requests.get(site, stream=True)

            if not response.ok:
                print
                response

            for block in response.iter_content(1024):
                if not block:
                    break

                handle.write(block)

        with open('vogel.jpg', 'rb') as f:
            await client.send_file(message.channel, f)


    if message.content.lower().startswith('!dog'):

        gefunden = 0
        endung = "test"

        while gefunden == 0:

            site = 'https://random.dog/'
            response = requests.get(site)

            soup = BeautifulSoup(response.text, 'html.parser')
            img_tags = soup.find_all('img')

            urls = [img['src'] for img in img_tags]

            try:
                url1 = str(urls).split("'")[1]
                gefunden = 1
                endung = str(urls).split(".")[1]
            except:
                url1 = ""

            if endung == "gif']":
                gefunden = 0

            richtigeurl = "https://random.dog/" + url1

        response = requests.get(richtigeurl, stream=True)
        await client.send_file(message.channel, io.BytesIO(response.raw.read()), filename='bild.png')



    if message.content.startswith('?join'):
        try:
            channel = message.author.voice.voice_channel
            await client.join_voice_channel(channel)
            global test
            test = 1
        except discord.errors.InvalidArgument:
            await client.send_message(message.channel, "Kein Voice channel gefunden.")
        except Exception as error:
            await client.send_message(message.channel, "Ein Error: ```{error}```".format(error=error))

    if message.content.startswith('?quit'):
        try:
            voice_client = client.voice_client_in(message.server)
            await voice_client.disconnect()
        except AttributeError:
            await client.send_message(message.channel, "fehler")
        except Exception as Hugo:
            await client.send_message(message.channel, "Ein Error: ```{haus}```".format(haus=Hugo))


    if message.content.startswith('?play '):
        try:

            yt_url = message.content[6:]
            if client.is_voice_connected(message.server) and test == 2:
       #         print("fehler0")
                try:
                    voice = client.voice_client_in(message.server)
            #        print("fehler1")

                    players['375986797701758986'].stop()            #wenn 404 fehler dann diese zeile auskommentieren #das gleiche wie = player.stop()

            #        print("fehler2")
                    player = await voice.create_ytdl_player(yt_url)
              #      print("fehler3")
                    players[message.server.id] = player
                   # print("fehler4")
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))
                   # print("fehler5")

            if client.is_voice_connected(message.server) and test == 1:
               # print("fehler0")
                try:
                    voice = client.voice_client_in(message.server)
                    #print("fehler1")

                    player = await voice.create_ytdl_player(yt_url)
                    #print("fehler3")
                    players[message.server.id] = player
                    #print("fehler4")
                    player.start()
                    test = 2
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))
                   # print("fehler5")


            if not client.is_voice_connected(message.server):
                #print("fehler00")
                try:
                    channel = message.author.voice.voice_channel
                   # print("fehler11")
                    voice = await client.join_voice_channel(channel)
                   # print("fehler22")
                    player = await voice.create_ytdl_player(yt_url)
                  #  print("fehler33")
                    players[message.server.id] = player
                   # print("fehler44")
                    player.start()
                    test = 2
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
                   # print("fehler55")


        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))
            print("fehler100000")


    if message.content.startswith('!airhorn'):
        try:
            if client.is_voice_connected(message.server) and test == 2:
                try:
                    voice = client.voice_client_in(message.server)
                    players['375986797701758986'].stop()
                    player = voice.create_ffmpeg_player('music/airhorn.mp3')
                    players[message.server.id] = player
                    player.start()
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))
            if client.is_voice_connected(message.server) and test == 1:
                try:
                    voice = client.voice_client_in(message.server)
                    player = voice.create_ffmpeg_player('music/airhorn.mp3')
                    players[message.server.id] = player
                    player.start()
                    test = 2
                except Exception as e:
                    await client.send_message(message.server, "Error: [{error}]".format(error=e))
            if not client.is_voice_connected(message.server):
                try:
                    channel = message.author.voice.voice_channel
                    voice = await client.join_voice_channel(channel)
                    player = voice.create_ffmpeg_player('music/airhorn.mp3')
                    players[message.server.id] = player
                    player.start()
                    test = 2
                except Exception as error:
                    await client.send_message(message.channel, "Error: [{error}]".format(error=error))
        except Exception as e:
            await client.send_message(message.channel, "Error: [{error}]".format(error=e))
















    if message.content.startswith('?pause'):
        try:
            players[message.server.id].pause()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))
    if message.content.startswith('?resume'):
        try:
            players[message.server.id].resume()
        except Exception as error:
            await client.send_message(message.channel, "Error: [{error}]".format(error=error))


    if message.content.lower().startswith('ping'):
        await client.send_message(message.channel, "Pong!")

    if 'Prost ' in message.content and message.author.id != hardshipbot or ' Prost ' in message.content and message.author.id != hardshipbot or 'prost ' in message.content and message.author.id != hardshipbot or ' prost ' in message.content and message.author.id != hardshipbot or message.content == 'Prost' and message.author.id != hardshipbot or message.content == 'prost' and message.author.id != hardshipbot or ' prost!' in message.content and message.author.id != hardshipbot or ' prost?' in message.content and message.author.id != hardshipbot or ' prost.' in message.content and message.author.id != hardshipbot or ' Prost!' in message.content and message.author.id != hardshipbot or ' Prost?' in message.content and message.author.id != hardshipbot or ' Prost.' in message.content and message.author.id != hardshipbot or message.content == 'Prost.' and message.author.id != hardshipbot or message.content == 'Prost!' and message.author.id != hardshipbot or message.content == 'Prost?' and message.author.id != hardshipbot or message.content == 'prost.' and message.author.id != hardshipbot or message.content == 'prost!' and message.author.id != hardshipbot or message.content == 'prost?' and message.author.id != hardshipbot:
        await client.send_message(message.channel, 'Prost! :beers:')

    if message.content.startswith('!afk'):
        afkzahl = random.randint(1,4)
        if(afkzahl == 1):
            await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **geht nun von Bord und besorgt der Crew mehr Rum! :beers:**")
        if(afkzahl == 2):
            await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **geht nun von Bord und sucht einen Schatz! <:schatz:401902113577238549>**")
        if(afkzahl == 3):
            await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **geht nun von Bord und plündert eine Insel! :island:**")
        if(afkzahl == 4):
            await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **geht nun von Bord und beraubt ein paar Landratten! :moneybag:**")

       #await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **ist nun eine Weile damit beschäftigt das Deck zu schrubben!**")

    if message.content.startswith('!wd'):
        await client.send_message(message.channel, "<@!" + message.author.id + ">" + " **ist nun wieder an Deck! <:hs:377664754518327317>**")



    if message.content.lower().startswith('!umarmung') or message.content.lower().startswith('!hug'):
        if(message.content.lower().startswith('!umarmung')):
            string = message.content[10:]
        if(message.content.lower().startswith('!hug')):
            string = message.content[5:]
        deleted = await client.purge_from(message.channel, limit=1)

        if(string !=""):

            name = string.split(' ')[0]
            #nachricht = string.split(name)[1]
            author = "<@!" + message.author.id + ">"
            hardshipbot = '<@!408965212750872576>'

            if(name == author):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt " + name + " <:hug:400375066338000908>" + " ...das ist ein bisschen komisch.**")

            if(name != author and name != '@here' and name != '@everyone' and name != hardshipbot):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt " + name + " <:hug:400375066338000908>**")

            if(name == '@here'):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt jeden Anwesenden. <:hug:400375066338000908> - :point_left: @here**")

            if(name == '@everyone'):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt euch alle. <:hug:400375066338000908> - :point_left: @everyone**")

            if(name == hardshipbot):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt " + name + " <:hug:400375066338000908> awww danke :3**")

        if(string == ""):
            await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " umarmt sich selbst! <:hug:400375066338000908>" + " ...das ist ein bisschen komisch.**")



    if message.content.lower().startswith('!cookie') or message.content.lower().startswith('!keks'):
        if(message.content.lower().startswith('!cookie')):
            string = message.content[8:]
        if(message.content.lower().startswith('!keks')):
            string = message.content[6:]
        deleted = await client.purge_from(message.channel, limit=1)
        if(string !=""):

            name = string.split(' ')[0]
            author = "<@!" + message.author.id + ">"
            hardshipbot = '<@!408965212750872576>'

            if(name == author):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " behält alle Kekse für sich selbst! :cookie: wie gemein ist das denn...**")

            if(name != author and name != '@here' and name != '@everyone' and name != hardshipbot):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " gibt " + name + " einen Keks! :cookie:**")

            if(name == '@here'):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " gibt jeden Anwesenden einen Keks! :cookie: - :point_left: @here**")

            if(name == '@everyone'):
                await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " gibt euch allen einen Keks! :cookie: - :point_left: @everyone**")

            if(name == hardshipbot):
               await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " gibt " + name + " einen Keks. :cookie: Lecker, danke :3**")


        if(string == ""):
            await client.send_message(message.channel, "**<@!" + message.author.id + ">" + " behält alle Kekse für sich selbst! :cookie: wie gemein ist das denn...**")





    if  message.content.lower().startswith('!purge') and message.author.id == jinid or message.content.lower().startswith('!purge') and message.author.id == apathyid:
        zahl = message.content[7:]
        if(zahl!= "" and zahl!= "nfo"):
            zahl = int(zahl)
            deleted = await client.purge_from(message.channel, limit=zahl+1)

        if(zahl == ""):
            deleted = await client.purge_from(message.channel, limit=1)
            await client.send_message(message.channel, "**:package: Fracht erfolgreich versenkt!**"
                                                       "\nDer Nachrichten-Verlauf wurde gelöscht. Denk daran, dass deine letzte Nachricht womöglich von niemandem gesehen wurde und du sie eventuell nun erneut senden solltest.")
        if(zahl == "nfo"):
            deleted = await client.purge_from(message.channel, limit=1)
            await client.send_message(message.channel, "**:package: Es ist mal wieder Zeit, überflüssige Fracht von Bord zu werfen!**"
                                      "\nDas heißt, gleich wird der Nachrichten-Verlauf gelöscht. Denk daran, dass deine letzte Nachricht womöglich von niemandem gesehen wurde. Du hast jetzt einen kurzen Moment Zeit, sie zu kopieren und gleich erneut zu senden.")

    if message.content.lower().startswith('!user') and message.author.id == jinid or message.content.lower().startswith('!user') and message.author.id == xtenid or message.content.lower().startswith('!user') and message.author.id == apathyid:

            #user = message.mentions[0]
            username2 = message.content[6:]
            username = str(username2).split('.', 1)[0]

            i = 0
            anzahl = 0

            x = message.server.members
            for member in x:
                join = str(member.joined_at).split('.', 1)[0]

                datum[i] = join
                name[i] = member.display_name
                mention[i] = member.mention
                usar[i] = member

                speicher = str(member.display_name).split('[')[0]
                anzeigename[i] = speicher
                anzahl = anzahl +1

                i = i + 1

            for x in range(i):
                swapped = False
                for j in range(0, i - x - 1):
                    if datum[j] > datum[j + 1]:
                        datum[j], datum[j + 1] = datum[j + 1], datum[j]
                        name[j], name[j + 1] = name[j + 1], name[j]
                        mention[j], mention[j + 1] = mention[j + 1], mention[j]
                        usar[j], usar[j + 1] = usar[j + 1], usar[j]
                        anzeigename[j], anzeigename[j + 1] = anzeigename[j + 1], anzeigename[j]
                        swapped = True
                if swapped == False:
                    break

            if username[:3] != "<@!":
                ende = False
                zehler = 0
                while ende == False:
                    s = 0
                    gefunden = 0
                    zehler = zehler +1
                    merker = None
                    while s < i:
                        if name[s].lower()[:zehler] == username.lower()[:zehler]:
                            gefunden = gefunden +1
                            merker = s

                        s = s + 1

                    if(gefunden == 1):
                        username = name[merker]
                        ende = True

                    if(gefunden > 1):
                        ende = False

                    if(zehler > 20):
                        ende = True


            s = 0
            while s < i:

                if name[s].lower() == username.lower() or mention[s].lower() == username.lower():

                    userjoinedat = str(usar[s].joined_at).split('.', 1)[0]
                    userjoindat1 = str(userjoinedat).split(' ')[0]
                    userjoindat2 = str(userjoinedat).split(' ')[1]
                    usercreatedat = str(usar[s].created_at).split('.', 1)[0]
                    usercreatedat1 = str(usercreatedat).split(' ')[0]
                    usercreatedat2 = str(usercreatedat).split(' ')[1]

                    datum1 = str(userjoindat1).split('-')[0]
                    datum2 = str(userjoindat1).split('-')[1]
                    datum3 = str(userjoindat1).split('-')[2]
                    userjoindat1 = datum3 + "." + datum2 + "." + datum1

                    datum1 = str(usercreatedat1).split('-')[0]
                    datum2 = str(usercreatedat1).split('-')[1]
                    datum3 = str(usercreatedat1).split('-')[2]
                    usercreatedat1 = datum3 + "." + datum2 + "." + datum1

                    l = 0
                    rollenname = ""
                    rollenname2 = ""
                    rollenname3 = ""
                    und1 = ""
                    und2 = ""

                    for role in usar[s].roles:
                        if role.name != "" and role.name != "@everyone":
                            if (l == 0):
                                rollenname = role.name
                            if (l == 1):
                                rollenname2 = role.name
                                und1 = " und "
                            if (l == 2):
                                rollenname3 = role.name
                                und2 = " und "
                            l = l + 1


                    userembed = discord.Embed(
                        #title="Username: " + user.name,
                        color=usar[s].colour,
                        #description= "_\n"
                    )
                    userembed.add_field(
                        name="<:pp:377681559580442625> User Info über " + usar[s].name + "\n",
                        value="_"
                    )

                    userembed.set_thumbnail(
                        url= usar[s].avatar_url,
                    )

                    x = str(s+1)

                    userembed.add_field(
                        name = "\nHardShip-Beitritt:",
                        value= userjoindat1 + " - " + userjoindat2 + "  (#" + x + ")",
                        inline = False
                    )

                    userembed.add_field(
                        name = "Discord-Beitritt:",
                        value= usercreatedat1 + " - " + usercreatedat2,
                        inline=False
                    )

                    userembed.add_field(
                        name = "Rollen:",
                        value= rollenname3 + und2 + rollenname2 + und1 + rollenname,
                        inline=False
                    )

                    userembed.add_field(
                        name = "User ID:",
                        value= usar[s].id,
                        inline=False
                    )

                    #anz = anzahl der user
                    anzahl = anzahl-1

                    if s-3 == -3:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value= "**" + anzeigename[s] + "** > " + anzeigename[s + 1] + " > " + anzeigename[s + 2] + " > " + anzeigename[s + 3],
                            inline=False
                        )
                    if s-3 == -2:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value=anzeigename[s-1] + " > **" + anzeigename[s] + "** > " + anzeigename[s + 1] + " > " + anzeigename[s + 2] + " > " + anzeigename[s + 3],
                            inline=False
                        )
                    if s-3 == -1:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value=anzeigename[s-2] + " > " + anzeigename[s-1] + " > **" + anzeigename[s] + "** > " + anzeigename[s + 1] + " > " + anzeigename[s + 2] + " > " + anzeigename[s + 3],
                            inline=False
                        )
                    if s+3 == anzahl+3:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value=anzeigename[s-3] + " > " + anzeigename[s-2] + " > " + anzeigename[s-1] + " > **" + anzeigename[s] + "**",
                            inline=False
                        )
                    if s+3 == anzahl+2:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value=anzeigename[s-3] + " > " + anzeigename[s-2] + " > " + anzeigename[s-1] + " > **" + anzeigename[s] + "** > " + anzeigename[s+1],
                            inline=False
                        )
                    if s+3 == anzahl+1:
                        userembed.add_field(
                            name="Beitritts Reihenfolge:",
                            value=anzeigename[s-3] + " > " + anzeigename[s-2] + " > " + anzeigename[s-1] + " > **" + anzeigename[s] + "** > " + anzeigename[s+1] + " > " + anzeigename[s+2],
                            inline=False
                        )
                    if(s+3 <= anzahl and s-3 >=0):
                        userembed.add_field(
                            name = "Beitritts Reihenfolge:",
                            value= anzeigename[s-3] + " > " + anzeigename[s-2] + " > " + anzeigename[s-1] + " > **" + anzeigename[s] + "** > " + anzeigename[s+1] + " > " + anzeigename[s+2] + " > " + anzeigename[s+3],
                            inline=False
                        )

                    await client.send_message(message.channel, embed=userembed)
                    break
                s = s+1




    if  message.content.lower().startswith('!quote <') or message.content.lower().startswith('!zitat <'):
        if message.content.lower().startswith('!quote'):
            text = message.content[7:]
        if message.content.lower().startswith('!zitat'):
            text = message.content[7:]


        user = str(text).split(' ')[0]
        nachricht = str(text).split('> ')[1]


        x = message.server.members
        for member in x:
            if member.mention == user:
                user = member


        embed = discord.Embed(
            color=user.colour,
            description=nachricht
        )
        embed.set_author(
            name=user.display_name,
            icon_url=user.avatar_url,
        )

        await client.purge_from(message.channel, limit=1)
        await client.send_message(message.channel, embed=embed)



    if  message.content.lower().startswith('!quote 1') or message.content.lower().startswith('!quote 2') or message.content.lower().startswith('!quote 3') or message.content.lower().startswith('!quote 4') or message.content.lower().startswith('!quote 5') or message.content.lower().startswith('!quote 6') or message.content.lower().startswith('!quote 7') or message.content.lower().startswith('!quote 8') or message.content.lower().startswith('!quote 9') or message.content.lower().startswith('!quote 0') or message.content.lower().startswith('!zitat 1') or message.content.lower().startswith('!zitat 2') or message.content.lower().startswith('!zitat 3') or message.content.lower().startswith('!zitat 4') or message.content.lower().startswith('!zitat 5') or message.content.lower().startswith('!zitat 6') or message.content.lower().startswith('!zitat 7') or message.content.lower().startswith('!zitat 8') or message.content.lower().startswith('!zitat 9') or message.content.lower().startswith('!zitat 0'):
        if message.content.lower().startswith('!quote'):
            id = message.content[7:]
        if message.content.lower().startswith('!zitat'):
            id = message.content[7:]


        #name = message.author

        namezähler = 0

        for server in client.servers:
            for channel in server.channels:
                if channel.id == "398194384207609868" or channel.id == "376022574095663106" or channel.id == "376022018266497034" or channel.id == "409490585313869827":
                    channelname[namezähler] = channel
                    namezähler = namezähler+1

        s = 0
        test = ""

        while(s < namezähler):

            try:
                test = await client.get_message(channelname[s], id)

                if test != "":
                    s = s+1
            except:
                s = s+1


        if test == "":
            try:
                test = await client.get_message(message.channel, id)
            except:
                test = ""


        if test != "":


            datum8 = datetime.datetime.now()

#            newtime = test.timestamp + "01:00:00"
#            print(newtime)

            tagneu = test.timestamp + datetime.timedelta(0, 3600)

            tag = str(tagneu).split(' ')[0]
            tagneu11 = str(tag).split('-')[0]
            tagneu22 = str(tag).split('-')[1]
            tagneu33 = str(tag).split('-')[2]
            tagneu = tagneu33 + "." + tagneu22 + "." + tagneu11

            tag2 = str(datum8).split(' ')[0]
            tagneu1 = str(tag2).split('-')[0]
            tagneu2 = str(tag2).split('-')[1]
            tagneu3 = str(tag2).split('-')[2]
            tagneu2 = tagneu3 + "." + tagneu2 + "." + tagneu1


            neuezeit = test.timestamp + datetime.timedelta(0,3600) # 1 Stunde darauf gerechnet!

            müll12 = str(neuezeit).split(' ')[1]
            zeit44 = str(müll12).split(':')[0]
            zeit55 = str(müll12).split(':')[1]
            zeit = zeit44 + ":" + zeit55


            müll13 = str(datum8).split(' ')[1]
            zeit22 = str(müll13).split(':')[0]
            zeit33 = str(müll13).split(':')[1]
            zeit2 = zeit22 + ":" + zeit33

            wann = ""

            if tagneu == tagneu2:
                wann = "Heute um " + zeit
            if tagneu != tagneu2:
                wann = tagneu + " um " + zeit



            embed = discord.Embed(
                color=test.author.colour,
                description=test.content
            )
            embed.set_author(
                name=test.author.display_name,
                icon_url=test.author.avatar_url,
            )
            embed.set_footer(
                text = test.channel.name + " - " + wann
            )


            await client.purge_from(message.channel, limit=1)
            await client.send_message(message.channel, embed=embed)




    if message.content.lower().startswith('!echo ') or message.content.lower().startswith('!echo 1') or message.content.lower().startswith('!echo 2') or message.content.lower().startswith('!echo 3') or message.content.lower().startswith('!echo 4') or message.content.lower().startswith('!echo 5') or message.content.lower().startswith('!echo 6') or message.content.lower().startswith('!echo 7') or message.content.lower().startswith('!echo 8') or message.content.lower().startswith('!echo 9') or message.content.lower().startswith('!echo 0'):

        text = message.content[6:]
        nachricht = ""
        id = ""
        test = "123"

        if text.startswith('1') or text.startswith('2') or text.startswith('3') or text.startswith('4') or text.startswith('5') or text.startswith('6') or text.startswith('7') or text.startswith('8') or text.startswith('9') or text.startswith('0'):
            id = text
        if not text.startswith('1') and not text.startswith('2') and not text.startswith('3') and not text.startswith('4') and not text.startswith('5') and not text.startswith('6') and not text.startswith('7') and not text.startswith('8') and not text.startswith('9') and not text.startswith('0'):
            nachricht = text

        if id != "":
            namezähler = 0

            for server in client.servers:
                for channel in server.channels:
                    channelname[namezähler] = channel
                    namezähler = namezähler + 1

            s = 0
            test = ""

            while (s < namezähler):

                try:
                    test = await client.get_message(channelname[s], id)

                    if test != "":
                        s = s + 1
                except:
                    s = s + 1

            if test == "":
                try:
                    test = await client.get_message(message.channel, id)
                except:
                    test = ""

            if test != "":

                embed = discord.Embed(
                    color=message.author.colour,
                    description= test.content
                 )

        if test == "":
            nachricht = id

        if nachricht != "":

            embed = discord.Embed(
                color=message.author.colour,
                description= text
            )

        await client.purge_from(message.channel, limit=1)
        await client.send_message(message.channel, embed=embed)



    if  message.content.lower().startswith('!entscheide') or message.content.lower().startswith('!choose'):
        if message.content.lower().startswith('!entscheide'):
            text = message.content[12:]
        if message.content.lower().startswith('!choose'):
            text = message.content[8:]

        anzahl = text.count(" ")

        entscheide = {}
        i = 0

        while i <= anzahl:
            entscheide[i] = str(text).split(' ')[i]
            i = i+1

        x = i-1
        zufall = random.randint(0,x)

        if text == "":
            await client.send_message(message.channel, "Ich kann mich einfach nicht entscheiden.")

        if text != "" and anzahl == 0:
            await client.send_message(message.channel,"Eindeutig " + entscheide[zufall] + ". Was war daran jetzt so schwer?")

        if anzahl != 0:
            await client.send_message(message.channel,"Ich wähle " + entscheide[zufall] + " ")


    if  message.content.lower().startswith('!frage') or message.content.lower().startswith('!ask'):
        if message.content.lower().startswith('!frage'):
            text = message.content[7:]
        if message.content.lower().startswith('!ask'):
            text = message.content[5:]

        if text !="":
            zufall = random.randint(1,10)

            if zufall == 1:
                antwort = "Auf gar keinen Fall!"
            if zufall == 2:
                antwort = "Das ist sehr unwahrscheinlich."
            if zufall == 3:
                antwort = "Die Chancen dafür stehen nicht so gut."
            if zufall == 4:
                antwort = "Ich glaube nicht daran."
            if zufall == 5:
                antwort = "Eher nicht so."
            if zufall == 6:
                antwort = "Das ist durchaus möglich."
            if zufall == 7:
                antwort = "Ich glaube ja"
            if zufall == 8:
                antwort = "Das ist sehr wahrscheinlich."
            if zufall == 9:
                antwort = "Ich bin fest davon überzeugt!"
            if zufall == 10:
                antwort = "Ja! nichts ist eindeutiger als das!"

            await client.send_message(message.channel,antwort)

        if text == "":

            await client.send_message(message.channel,"Man kann auf keine Frage antworten wenn man die Frage nicht kennt.")







@client.event
async def on_member_join(member):
    await client.send_message(discord.Object("376022574095663106"), "**" + member.mention + " betritt das " + member.server.name + "!**")
    role = discord.utils.get(member.server.roles, name='Blinder Passagier')
    await client.add_roles(member, role)


@client.event
async def on_member_remove(member):
    await client.send_message(discord.Object("376022574095663106"), "**" + member.mention + " wurde über die Planke geschickt!**")







client.run(process.env.BOT_TOKEN)
