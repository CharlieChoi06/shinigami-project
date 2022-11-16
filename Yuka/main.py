import os
import sys

import discord
from dotenv import load_dotenv
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


@client.event
async def on_ready():
  for guild in client.guilds:
    if guild.name == GUILD:
      break

    print(f'{client.user} has connected to server!')


@client.event
async def on_message(message):
  if message.author == client.user:
    return
  powitanie = ['Ohayo onii chan~']
  cytatkaguya = [
    '"How cute~"',
    '"If it’s true love, I’m prepared to even accept expulsion"',
    '"It’s not good to be excessively afraid of physical contact with other people. I guess that’s the dark side of modern society."'
  ]
  cytatkei = [
    '"In reality, she wants to speak to you normally, but she’s too embarrassed to do so. It happens all the time."',
  ]
  cytatmiko = [
    '"I want to convey those feelings of mine to the students through my campaign."',
  ]
  cytatishigami = [
    '"I think I’m coming down with Stockholm syndrome, so I’m heading home for the day."',
  ]
  cytatmiyuki = [
    '"When it comes to student council, school rules take priority over traffic rules!"',
    '"A love letter to Shinomiya? Some men really are fools for love. We’re talking about Shinomiya who usually passes the time looking at me. Does this fellow know, next to me, any other male in the vicinity would only register as a talking weed?"',
    '"What, the figure out what Shinomiya’s thinking and guess where she went game? Hmph, that was a hundred times easier than the usual ones"',
  ]
  cytathayasaka = [
    '"If you don’t put on an act, you won’t be loved"',
  ]
  cytatchika = [
    ' "I really like it when you laugh, Kaguya." ',
    '"It’s no fair to have girls’ talk without me! Please leave an issue like that to Love Detective Chika!"'
  ]
  zaproszenie = ['https://discord.gg/9tzBdpCH6u']
  simpon = ['SIMP DETECTED ARA ARA~ (:౦ ‸ ౦ :)']
  simpoff = ['Przestałeś simpować..? Szkoda ( ╥ω╥ )']
  baka = ['Baaaaka~ (￣ ￣|||)']
  help = [
    '!hello -> powitanie, !kaguyaquotes -> cytaty Kaguyi Shinomiya, !keiquotes -> cytaty Kei Shirogane, !mikoquotes -> cytaty Miko, !ishigamiquotes -> cytaty Ishigami Yu, !miyukiquotes -> cytaty Miyuki Shirogane, !hayasakaquotes -> cytaty Ai Hayasaki, !chikaquotes -> cytaty Chiki Fujiwary, !invite -> zaproszenie na wykurwisty serwer Dere Dere Cafe :3, !simpmodeon -> moshi moshi simp police desuka?~, !simpmodeoff -> no ni ma simpa, !baka -> czyli jak powiedzieć debilowi, że jest debilem, nie mówiąc mu, że jest debilem'
  ]
  kuba = ['Kubuś, sklej mleczaki']
  brakx = ['(─‿‿─)♡']
  cygan = ['Ależ ty mnie irytujesz (◕‿◕)']
  julcia = ['Nya~ kawaii senpai ara ara~!']
  sraka = ["No sraka, spójrz w lustro (żarcik, kc słonko)"]
  serwer = [
    "Tam jest taki prostokąt z klamką, to są drzwi wyjdziesz przez te drzwi do ogródka, troszeczkę sobie odetchniesz i wypierdalaj ... wypieralaj !"
  ]
  if message.content == '!hello':
    response = random.choice(powitanie)
    await message.channel.send(response)
  elif message.content == 'raise-exception':
    raise discord.DiscordException
  elif message.content == '!kaguyaquotes':
    response = random.choice(cytatkaguya)
    await message.channel.send(response)
  elif message.content == '!keiquotes':
    response = random.choice(cytatkei)
    await message.channel.send(response)
  elif message.content == '!mikoquotes':
    response = random.choice(cytatmiko)
    await message.channel.send(response)
  elif message.content == '!ishigamiquotes':
    response = random.choice(cytatishigami)
    await message.channel.send(response)
  elif message.content == '!miyukiquotes':
    response = random.choice(cytatmiyuki)
    await message.channel.send(response)
  elif message.content == '!hayasakaquotes':
    response = random.choice(cytathayasaka)
    await message.channel.send(response)
  elif message.content == '!chikaquotes':
    response = random.choice(cytatchika)
    await message.channel.send(response)
  elif message.content == '!invite':
    response = random.choice(zaproszenie)
    await message.channel.send(response)
  elif message.content == '!simpmodeon':
    response = random.choice(simpon)
    await message.channel.send(response)
  elif message.content == '!simpmodeoff':
    response = random.choice(simpoff)
    await message.channel.send(response)
  elif message.content == '!baka':
    response = random.choice(baka)
    await message.channel.send(response)
  elif message.content == '!help':
    response = random.choice(help)
    await message.channel.send(response)
  elif message.content == '!ząbkikubusia':
    response = random.choice(kuba)
    await message.channel.send(response)
  elif message.content == '!brakx':
    response = random.choice(brakx)
    await message.channel.send(response)
  elif message.content == '!cygan':
    response = random.choice(cygan)
    await message.channel.send(response)
  elif message.content == '!julcia':
    response = random.choice(julcia)
    await message.channel.send(response)
  elif message.content == '!sraka':
    response = random.choice(sraka)
    await message.channel.send(response)
  elif message.content == '!usunserwer':
    response = random.choice(serwer)
    await message.channel.send(response)


client.run(
  'MTA0MDY2NDYwNzM4NTE5NDUzOA.GboMm4.zvOJIzZsilxjbknVQxb8Ml3kdh1EpJ1fef3XFg')
