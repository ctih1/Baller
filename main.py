import discord
from discord.ext import commands
from discord.commands import Option
import random
import names
from datetime import date
from webserver import keep_alive
import os
import threading
from discord.ext.commands import has_permissions, MissingPermissions
import asyncio
import wikipedia
from discord.ext import tasks
import pickle
import datetime
import logging
import json
import time
from datetime import datetime
from pyrandmeme import *
from datetime import timedelta
from cryptography.fernet import Fernet
import requests
from googletrans import Translator
from os import system
import openai
import ascii
import string
from discord.ui import Select, Button, View


servers = [1005731721079165008]

#ÄLÄ LISÄÄ MUUTA!await interaction.response.send_message(content="Ostit V.I.P:n", ephemeral = True)
##################
logger = logging.getLogger('discord')
logger.setLevel(logging.INFO)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='a')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
##################

_1kk_vip_plus = 200
_3kk_vip_plus = 600
_6kk_vip_plus = 1200
_12kk_vip_plus = 2000
_1kk_vip_price = 100
_3kk_vip_price = 300
_6kk_vip_price = 600
_12kk_vip_price = 1000
openai.api_key = os.getenv("OPEN_AI_KEY")

fh = open("unimi.pkl", 'rb')
unimi = pickle.load(fh)



today = date.today()
TOKEN = "DISCORD_BOT_SECRET"

now = datetime.now()
d2 = today.strftime("%d/%m/%Y")
currentTime = now.strftime("%H:%M:%S")

intents = discord.Intents.all()


#capitals.get("1val")

#variables
from variables_load import swear, greg_list,xxx_tag, gg_tag,response

f = open("response.txt", 'r')
response_data = f.readlines()
response = []
for element in response_data:
  response.append(element.strip())
#d2 = today.strftime("%B %d, %Y")

#today = date.today()
vastaus_password = ["sufh731","cvhgs52ub","tosisalainensalasan","10d1596","84ll3rv4st4u5","fwkopaksoif"]

TOKEN = "DISCORD_BOT_SECRET"

bot = discord.Bot(intents=intents)

level_shop = [{"name":"V.I.P","price":100,"description":"Antaa V.I.P Roolin"}]

shop = [{"name":"S-Etukortti","price":100,"description":"S-Etukortti"},
  {"name":"RGB Valot","price":500,"description":"RGB Valot 5 Metriä"},
  {"name":"VR Lasit","price":4000,"description":"Oculus Quest 2"},
  {"name":"Kala","price":4000,"description":"Kala Rooli"},
  {"name":"VIP","price":10000,"description":"VIP-Rooli"}]
  
latest_command = "Ei viimeisimpiä komentoja!"

@bot.event
async def on_ready():
  print(f"Logged in as {bot.user}")
  asyncio.create_task(decrement_messages())
  while True:
    await bot.change_presence(activity=discord.Game(name=f"Viimeisin käytetti komento: {latest_command}"))
    await asyncio.sleep(5)
  await asyncio.sleep(3600)
  system("python restart_.py")
  system("kill 1")
  


  

channel_id = None

@bot.event
async def on_member_join(member):
  if member.id == 1041129066285244567:
    message.channel.send(f"<@{member.id}> On The Everything.")

deletes_counter = {}
bans_counter = {}
messages_per_min = {}
ignored_for = {}
on_cooldown = {}
reactions_1 = {}
l_f_m = False
@bot.event
async def on_guild_channel_delete(channel):
    user = None
    async for entry in channel.guild.audit_logs(action=discord.AuditLogAction.channel_delete):
        if entry.target.id == channel.id:
            user = entry.user
            break
    if user is None:
        return
      
    if user.id in deletes_counter:
      deletes_counter[user.id] += 1
    else:
      deletes_counter[user.id] = 1

    if deletes_counter[user.id] >= 3:
       await user.ban(reason="Grieffaus esto | Poisti yli 3 kanavaa")
    await asyncio.sleep(60)
    deletes_counter[user.id] -= 1

@bot.event
async def on_member_ban(guild, banned_user):
    async for entry in guild.audit_logs(limit=1, action=discord.AuditLogAction.ban):
        user = entry.user

        if user.id in bans_counter:
            bans_counter[user.id] += 1
        else:
            bans_counter[user.id] = 1
    if user.id in bans_counter:
        if bans_counter[user.id] >= 3:
            await guild.ban(user, reason="Grieffaus esto | Bännäsi yli 3 ihmistä")
            channel = guild.text_channels[0]
            await channel.send(f"@everyone käyttäjä <@{user.id}> bännättiin | Antigrief | Bännäsi liikaa ihmisiä ajassa!")
            bans_counter[user.id] = 0
        else:
            asyncio.create_task(decrement_counter(user.id))

async def decrement_counter(user_id):
    await asyncio.sleep(60*3)
    if user_id in bans_counter:
        bans_counter[user_id] -= 1
async def decrement_ignored(user_id):
    await asyncio.sleep(120)
    if user_id in ignored_for:
        ignored_for.pop(str(user_id))
async def decrement_messages():
    await asyncio.sleep(60)
    if not messages_per_min:
      pass
    else:
      messages_per_min.update((k, 0) for k in messages_per_min)

async def decrement_on_cooldown(user_id,guild_id):
  await asyncio.sleep(120)
  on_cooldown[str(guild_id)].pop(str(user_id))

@bot.event
async def on_guild_join(guild):
  default_channel = guild.text_channels[0]
  await default_channel.send("Kiitos että lisäsit Ballerin sinun serveriin!, Aloita tekemällä '/admin-kanava'! <- Tämä auttaa estämään esim grieffaamista. Ja jos haluat chattailla minun kanssa, tee '/kanava' @here")

@bot.event
async def on_raw_reaction_add(payload):
  global l_f_m, reactions_1
  emoji = payload.emoji

  if l_f_m == True:
    reactions_1[str(emoji)] += 1
  else:
    pass
@bot.event
async def on_message(message):
  print(on_cooldown)
  username = str(message.author).split("#")[0]
  user_message = str(message.content)
  channel = str(message.channel.name)
  user = message.author
  with open("user_options.json","r") as f:
    global_config = json.load(f)
  guild_id = message.guild.id
  if user.bot == True:
    return
  if str(message.channel.id) == "1011623593295224843":
    if str(message.content).strip() != "???":
      await message.delete()
  if str(guild_id) not in on_cooldown:
    on_cooldown[str(guild_id)] = {} 


  else:
    pass
  if str(message.author.id) not in messages_per_min:
    if str(message.author.id) in ignored_for:
      pass
    else:
      messages_per_min[str(message.author.id)] = 1
  else:
    if str(message.author.id) in ignored_for:
      pass
    else:
      messages_per_min[str(message.author.id)] += 1
  if messages_per_min[str(message.author.id)] > 6:
    ignored_for[str(message.author.id)] = 120
    messages_per_min[str(message.author.id)] = 0
    asyncio.create_task(decrement_ignored(str(message.author.id)))

  if str(message.author.id) not in ignored_for and str(message.author.id) not in on_cooldown[str(message.guild.id)]:
      if len(message.content) > random.randint(12,16) and " " in message.content:
        if "http" in message.content:
          pass
        else:
          if "<:" in message.content:
            pass
          else:
            if len(message.content) < 250:
              await change_level(guild_id = message.guild.id,user_id = message.author.id,amount=1)
            else:
              await change_level(guild_id = message.guild.id,user_id = message.author.id,amount=1+len(message.content)//100)
            a = global_config.get(str(user.id),{}).get("cheese",True)
            on_cooldown[str(guild_id)][str(message.author.id)] = 10
            asyncio.create_task(decrement_on_cooldown(user_id=message.author.id,guild_id=message.guild.id))
            if a == True:
              await message.add_reaction("🧀")

  await create_settings(guild_id = message.guild.id)
  data = await check_settings(guild_id = message.guild.id,setting="chat_channel")
  if data == None:
    data = "Lol"
  max_lenght = await check_settings(guild_id = message.guild.id, setting = "max_lenght")
  story_channel = await check_settings(guild_id = message.guild.id,setting="story_channel")
  if story_channel == None:
    story_channel = "Lol"
  allow_spaces = await check_settings(guild_id = message.guild.id,setting="allow_spaces")
  if str(message.channel.id) in story_channel:
    if len(message.content) < int(max_lenght):
      with open("story.json","r") as f:
        current_story = json.load(f)

    else:
      await message.add_reaction("❌")
      return
    if allow_spaces == False and " " in message.content:
        await message.add_reaction("❌")
        return
    if str(message.channel.id) not in str(current_story):
      with open("story.json","w") as f:
        current_story[str(message.channel.id)] = "!res"
    if current_story[str(message.channel.id)] == "!res":
      current_story[str(message.channel.id)] = f"{message.content} "
      await message.add_reaction("✅")
      with open("story.json","w") as f:
        json.dump(current_story,f)
    else:
      current_story[str(message.channel.id)] += f"{message.content} "
      await message.add_reaction("✅")
      with open("story.json","w") as f:
        json.dump(current_story,f)
  

  

  
  if message.author == bot.user:
    return
  else:
    pass

  if str(message.channel.id) in data or message.content.startswith("<@1033278946093060116>"):
    async with message.channel.typing():  
      await asyncio.sleep(1)
      await message.channel.send(random.choice(response))
  else:
    pass
    
  print(f"{username}: {user_message}: ({channel})")
  bots_account = ("UnbelievaBoat#0000")
  block_save = ("Ota rahaa")
  if block_save in message.content and message.author != message.author.bot:
    return
  
  with open("messages.json","r") as f:
    messages = json.load(f)
  if str(message.author.id) in messages:
    if type(messages[str(message.author.id)]["message"]) == str:
      messages[str(message.author.id)]["message"] = [messages[str(message.author.id)]["message"]]
    messages[str(message.author.id)]["message"].append(str(message.content))
  else:
    messages[str(message.author.id)] = {"message": [str(message.content)]}
  with open("messages.json","w") as f:
    json.dump(messages,f)

async def create_level(guild_id,user_id):
  with open("level.json","r") as f:
    levels = json.load(f)
  if str(guild_id) not in levels:
    levels[str(guild_id)] = {}
    with open("level.json","w") as f:
      json.dump(levels,f)
      
  if str(user_id) not in levels[str(guild_id)]:
    levels[str(guild_id)][str(user_id)] = 0
    with open("level.json","w") as f:
      json.dump(levels,f)
  else:
    pass
async def check_level(guild_id,user_id):
  with open("level.json","r") as f:
    levels = json.load(f)
  return levels[str(guild_id)][str(user_id)]
async def change_level(guild_id,user_id,amount):
  await create_level(guild_id=guild_id,user_id =user_id)
  with open("level.json","r") as f:
    levels = json.load(f)
  levels[str(guild_id)][str(user_id)] += int(amount)
  with open("level.json","w") as f:
    json.dump(levels,f)
    
#--------------------------ONKO--------------------------#
@bot.slash_command(name="onko",description="Baller sanoo True Tai False")
async def baller(ctx, asia):
  global latest_command
  latest_command = "/onko"
  torf = ["Ei", "On"]
  torfrnd = random.choice(torf)
  await ctx.respond(f"{torfrnd}")


@bot.slash_command(name="lisää_juusto",description="Lisää juustopisteitä käyttäjälle")
async def add_cheese(ctx,user:discord.Member,määrä, salasana):
  with open("key.json","r") as f:
    passwords = json.load(f)
  if salasana not in passwords:
    embed = discord.Embed(color=0xe6ffff,title = f"Vastaus",description=f'Väärä salasana!')
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral = True)
    return
  if passwords[str(salasana)]["command"] != "juusto":
    embed = discord.Embed(color=0xe6ffff,title = f"Vastaus",description=f'Salasana ei ole tarkoitettu tälle komennolle!')
    with open("commands.json","a") as f:
      f.write(f"{ctx.author.id} (lisää raha) -> {user.id} (€{määrä})\n")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral = True)
    return
  await change_level(guild_id=ctx.guild.id,user_id=user.id,amount=määrä)
  embed = discord.Embed(color=0xe6ffff,title = f"Lisää Juusto",description=f'Lisättiin {määrä} juustoa käyttäjälle <@{user.id}>')
  with open("commands.json","a") as f:
    f.write(f"{ctx.author.id} (lisää raha) -> {user.id} (€{määrä})\n")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed, ephemeral = True)

@bot.slash_command(guild_ids = servers, name="tee_kauppa",description="Tekee VIP Kaupan")
async def make_shop(ctx):
  embed = discord.Embed(color=0xe6ffff, title="Kauppa", description=f"Tavarat:")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text="Eikö komento toimi? Tee /tee_kauppa")
  vip_button = Button(label="VIP",style=discord.ButtonStyle.green, emoji="💳")
  vip_plus_button = Button(label="VIP+",style=discord.ButtonStyle.green, emoji="💳")
  
  async def button_callback_vip(interaction):
    await msg.delete()
    await pituus_vip(ctx=ctx,tavara="V.I.P")
    
  async def button_callback_vip_plus(interaction):
    await msg.delete()
    await pituus_plus(ctx=ctx,tavara="V.I.P+")


  vip_button.callback = button_callback_vip
  vip_plus_button.callback = button_callback_vip_plus
  view = View(timeout=None)
  view.add_item(vip_button)
  view.add_item(vip_plus_button)
  msg = await ctx.send(embed=embed,view=view)

async def pituus_vip(ctx,tavara):
  level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
  embed = discord.Embed(color=0xe6ffff, title="Kauppa", description=f"{tavara}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text="Eikö komento toimi? Tee /tee_kauppa")
  embed.add_field(name=f"1kk: {_1kk_vip_price} 🧀", value=f"",inline=True)
  embed.add_field(name=f"3kk: {_3kk_vip_price} 🧀", value=f"",inline=True)
  embed.add_field(name=f"6kk: {_6kk_vip_price} 🧀", value=f"",inline=True)
  embed.add_field(name=f"6kk: {_12kk_vip_price} 🧀", value=f"",inline=True)
  _1kk_button = Button(label="1kk",style=discord.ButtonStyle.green, emoji="1️⃣")
  _3kk_button = Button(label="3kk",style=discord.ButtonStyle.green, emoji="3️⃣")
  _6kk_button = Button(label="6kk",style=discord.ButtonStyle.green, emoji="6️⃣")
  _12kk_button = Button(label="12kk",style=discord.ButtonStyle.green, emoji="✨")
  ########### MUISTA RAHA CHECK ###########
  async def _1kk_button_callback_vip(interaction):
    if int(level) >= _1kk_vip_price:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_1kk_vip_price)
      await interaction.response.send_message(content="Ostit V.I.P:n (1 kuukausi)", ephemeral = True)
      await msg.delete()
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1041672104434745344)
      await ctx.author.add_roles(role,reason = "1kk V.I.P Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P (1kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
    
  async def _3kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _3kk_vip_price:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_3kk_vip_price)
      await interaction.response.send_message(content="Ostit V.I.P:n (3 kuukautta)", ephemeral = True)
      await msg.delete()
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1041672104434745344)
      await ctx.author.add_roles(role,reason = "3kk V.I.P Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P (3kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  async def _6kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _6kk_vip_price:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_6kk_vip_price)
      await interaction.response.send_message(content="Ostit V.I.P:n (6 kuukautta)", ephemeral = True)
      await msg.delete()
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1041672104434745344)
      await ctx.author.add_roles(role,reason = "6kk V.I.P Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P (6kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  async def _12kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _12kk_vip_price:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_12_kk_vip_price)
      await msg.delete()
      await interaction.response.send_message(content="Ostit V.I.P:n (12 kuukautta)", ephemeral = True)
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1041672104434745344)
      await ctx.author.add_roles(role,reason = "12kk V.I.P Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P (12kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  _1kk_button.callback = _1kk_button_callback_vip
  _3kk_button.callback = _3kk_button_callback_vip
  _6kk_button.callback = _6kk_button_callback_vip
  _12kk_button.callback = _12kk_button_callback_vip
  view = View(timeout=None)
  view.add_item(_1kk_button)
  view.add_item(_3kk_button)
  view.add_item(_6kk_button)
  view.add_item(_12kk_button)
  msg = await ctx.send(embed=embed,view=view)

async def pituus_plus(ctx,tavara):
  level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
  embed = discord.Embed(color=0xe6ffff, title="Kauppa", description=f"{tavara}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text="Eikö komento toimi? Tee /tee_kauppa")
  embed.add_field(name=f"1kk: {_1kk_vip_plus} 🧀", value=f"",inline=True)
  embed.add_field(name=f"3kk: {_3kk_vip_plus} 🧀", value=f"",inline=True)
  embed.add_field(name=f"6kk: {_6kk_vip_plus} 🧀", value=f"",inline=True)
  embed.add_field(name=f"6kk: {_12kk_vip_plus} 🧀", value=f"",inline=True)
  _1kk_button = Button(label="1kk",style=discord.ButtonStyle.green, emoji="1️⃣")
  _3kk_button = Button(label="3kk",style=discord.ButtonStyle.green, emoji="3️⃣")
  _6kk_button = Button(label="6kk",style=discord.ButtonStyle.green, emoji="6️⃣")
  _12kk_button = Button(label="12kk",style=discord.ButtonStyle.green, emoji="✨")
  ########### MUISTA RAHA CHECK ###########
  async def _1kk_button_callback_vip(interaction):
    if int(level) >= _1kk_vip_plus:
      level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_1kk_vip_plus)
      await interaction.response.send_message(content="Ostit V.I.P+:n (1 kuukausi)", ephemeral = True)
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1055815976370843648)
      await ctx.author.add_roles(role,reason = "1kk V.I.P+ Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P+ (1kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
    
  async def _3kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _3kk_vip_plus:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_3kk_vip_plus)
      await interaction.response.send_message(content="Ostit V.I.P+:n (3 kuukautta)", ephemeral = True)
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1055815976370843648)
      await ctx.author.add_roles(role,reason = "3kk V.I.P+ Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P+ (3kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  async def _6kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _6kk_vip_plus:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_6kk_vip_plus)
      await interaction.response.send_message(content="Ostit V.I.P+:n (6 kuukautta)", ephemeral = True)
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1055815976370843648)
      await ctx.author.add_roles(role,reason = "6kk V.I.P Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P+ (6kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  async def _12kk_button_callback_vip(interaction):
    level = await check_level(guild_id=ctx.guild.id,user_id=ctx.user.id)
    if int(level) >= _12kk_vip_plus:
      await change_level(guild_id = ctx.guild.id,user_id=ctx.user.id,amount=-1*_12_kk_vip_plus)
      await interaction.response.send_message(content="Ostit V.I.P+:n (12 kuukautta)", ephemeral = True)
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1055815976370843648)
      await ctx.author.add_roles(role,reason = "12kk V.I.P+ Osto.")
      channel = bot.get_channel(1009857795706867814)
      await channel.send(f"B!VIP <@{ctx.author.id}> osti V.I.P+ (12kk)")
    else:
      await interaction.response.send_message(content="Sinulla ei ole tarpeeksi rahaa!", ephemeral = True)
  _1kk_button.callback = _1kk_button_callback_vip
  _3kk_button.callback = _3kk_button_callback_vip
  _6kk_button.callback = _6kk_button_callback_vip
  _12kk_button.callback = _12kk_button_callback_vip
  view = View(timeout=None)
  view.add_item(_1kk_button)
  view.add_item(_3kk_button)
  view.add_item(_6kk_button)
  view.add_item(_12kk_button)
  await ctx.send(embed=embed,view=view)
#--------------------------ONKO--------------------------#
@bot.slash_command(name="gpt",description="Ottaa tietoa Chat GPT:stä")
async def ai(ctx,prompt):
  global latest_command
  latest_command = "/gpt"
  translator = Translator()
  finnish_text = prompt
  _prompt = translator.translate(finnish_text, src='fi', dest='en').text
  await ctx.defer()

  response = openai.Completion.create(engine="text-davinci-001",prompt=_prompt,max_tokens = 258)
  f_resp_ = (response["choices"][0]["text"])
  f_resp = translator.translate(f_resp_, src='en', dest='fi').text
  embed = discord.Embed(color=0xe6ffff, title="A.I (Chat GPT)", description=f"{f_resp}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text="Käännetty Google Translatella.")
  await ctx.respond(embed=embed)

@bot.slash_command(name="juusto_viesti",description="Valittajille ketkä ei halua juusto reaktioita")
async def cheese_message(ctx,tila:bool):
  with open("user_options.json","r") as f:
    options = json.load(f)
  if str(ctx.author.id) not in options:
    options[str(ctx.author.id)] = {}
    options[str(ctx.author.id)]["cheese"] = bool(tila)
  else:
    options[str(ctx.author.id)]["cheese"] = bool(tila)
  with open("user_options.json","w") as f:
    json.dump(options,f)
  embed = discord.Embed(color=0xe6ffff, title="Juusto Viesti", description=f"On nyt tilassa `{tila}`")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)
#--------------------------BLEVEL--------------------------   # 
@bot.slash_command(name="fakta",description="Antaa random faktan")
async def baller(ctx):
  global latest_command
  latest_command = "/fakta"
  async with ctx.typing():
    response = requests.get("https://uselessfacts.jsph.pl/random.json?language=en")
    fact = response.json()["text"]
    translator = Translator()
    fact_fi = translator.translate(fact, src='en', dest='fi').text
    await asyncio.sleep(1)
  
  embed = discord.Embed(color=0xe6ffff, title="Random Fakta:", description=f"{fact_fi}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text="Nämä on käännetty Google Translate:lla")
  await ctx.respond(embed=embed)
  
@bot.slash_command(name="level",description="Näyttää levelin")
async def level(ctx,user:discord.Member=None):
  if user == None:
    user = ctx.user
  level = await check_level(guild_id = str(ctx.guild.id), user_id = str(user.id))
  embed = discord.Embed(color=0xe6ffff, title=f"", description=f"<@{user.id}> On tasolla {level}")
  embed.set_footer(text=f"XP: {level}")
  await ctx.respond(embed=embed)
#--------------------------LAPPU--------------------------#
@bot.slash_command(name="lappu",description="Baller muuttaa viestin kauniimmaksi")
async def baller(ctx, aihe, selitys, vari: Option(required = False, default=hex(0xe6ffff))):
    global latest_command
    latest_command = "/lappu"
    try:
      embed = discord.Embed(color=int(vari, 16), title="", description="")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name=f"{aihe}", value=f"""{selitys}""",inline=True)
      await asyncio.sleep(1)
      await ctx.respond(embed=embed)

    except ValueError as e:
      
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await asyncio.sleep(1)
      await ctx.respond(embed=embed)
#--------------------------LAPPU--------------------------#

@bot.slash_command(name="broadcast",description="Baller muuttaa viestin kauniimmaksi")
@commands.has_permissions(administrator = True)
async def broadcast(ctx,message,salasana):
  
  if salasana != "qwerty123456":
    return
  else:
    
    with open("config.json","r") as f:
      data = json.load(f)
    admin_channels = []
    for key, value in data.items():
      if value['admin_channel']:
        admin_channels.append(value['admin_channel'])
    
    for admin_channel_id in admin_channels:
      try:
        print("try")

        channel = bot.get_channel(int(admin_channel_id))
        print("pre embed")

        embed = discord.Embed(color=0xe6ffff, title=f"Ilmoitus", description=f"{message}")
        
        print("post embed")
        await channel.send(embed=embed)
        print("post send")
      except Exception as e:
        pass
      
    
#--------------------------KIROSANA--------------------------#
@bot.slash_command(name="kirosana",description="Antaa random kirosanan")
async def baller(ctx):
  global latest_command
  latest_command = "/kirosana"
  await ctx.respond(f"{random.choice(swear)}")
#--------------------------KIROSANA--------------------------#
@bot.slash_command(name="restart",description="Käynnistää botin uudestaan")
async def restart(ctx):
  os.system("kill 1")
#--------------------------PANKKI--------------------------#
@bot.slash_command(name="bank",description="Näytää pankkitietosi")
async def pankki(ctx, user:Option(discord.Member, "Discord Käyttäjä", required = False, default = 'x1')):
  global latest_command
  latest_command = "/bank"
  async with ctx.typing():

    if user == "x1":
      user = ctx.author
    else:
      user = user
    await open_account(user)
    users = await get_bank_data()
  
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    
  embed = discord.Embed(color=0x70db70, title=f"")
  embed.add_field(name="Lompakko:",value=f"{wallet_amt}€",inline = True)
  embed.add_field(name="Pankki:",value=f"{bank_amt}€",inline = True)
  embed.add_field(name="Yhteensä:",value=f"{wallet_amt + bank_amt}€",inline = True)
  embed.set_author(name=f"{user.name}:n Pankki", icon_url = user.avatar)
  await ctx.respond(embed=embed)



async def open_account(user):
  users = await get_bank_data()
    
  if str(user.id) in users:
    return False
  else:
    users[str(user.id)] = {}  
    users[str(user.id)]["wallet"] = 50
    users[str(user.id)]["bank"] = 0

  with open("bank.json","w") as f:
    users = json.dump(users,f)
  return True

async def get_bank_data():
    with open("bank.json","r") as f:
      users = json.load(f)
    return users

async def update_bank(user,change = 0,mode = "wallet"):
  users = await get_bank_data()

  users[str(user.id)][mode] += change

  with open("bank.json","w") as f:
    json.dump(users,f)

  bal = [users[str(user.id)]["wallet"],users[str(user.id)]["bank"]]
  return bal
#--------------------------PANKKI--------------------------#  
  
#--------------------------RIKOS--------------------------#
@bot.slash_command(name="rikos",description="Tee rikos")
@commands.cooldown(1, 2700, commands.BucketType.user)
async def rikos(ctx):
  global latest_command
  latest_command = "/rikos"
  async with ctx.typing():
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
    
    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]
    all_amt = (wallet_amt + bank_amt)
  
  
  if all_amt < 100:
    embed = discord.Embed(color=0xff0000, title="Rikos", description=f"Tarvitset vähintään 100€, sinulla on {all_amt}")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    return
  
  amount = random.randint(100, 1000)
  
  random_chance = random.choice([True, False])
  if random_chance == False:
    embed = discord.Embed(color=0xff0000, title="Rikos", description=f"Jäit kiinni! Joudut maksamaan {amount}€")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  
    await update_bank(ctx.author,-1*amount,"bank")
    await ctx.respond(embed=embed)

  
  else:
    
    rikos = ["Varastit rahaa lapselta","Myit huumeita","Myit alkoholia lapsille","Varastit vanhan mummon laukun","Varastit leegoja S-Marketista","Varastit vanhan auton","Varasit polkupyörän","Varastit liikennevalot","Varastit liikennemerkin",""]
    embed = discord.Embed(color=0x70db70, title="Rikos", description=f"{random.choice(rikos)}, sait siitä {amount}€")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await update_bank(ctx.author,1*amount,"wallet")
    await ctx.respond(embed=embed)
    
@rikos.error
async def varoita_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(color=0xff0000, title=f"Sinun pitää odottaa {round(error.retry_after, 2)} sekunttia ennen kun voit suorittaa tämän komennon!", description=f"")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed, ephemeral=True)   
#--------------------------RIKOS--------------------------#

#--------------------------TYÖ--------------------------#  
@bot.slash_command(name="työ",description="Mene töihin")
@commands.cooldown(1, 600, commands.BucketType.user)
async def työ(ctx):
  global latest_command
  latest_command = "/työ"
  async with ctx.typing():
    have_account = await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()
  
    työ = ["Siivosit vessoja","Korjasit pianon","Menit ottamaan kelarahat","Sait kalan ja myit sen S-Marketille","Myit pommim al-qaedalle","Louhit hiiltä","Löysit rahaa tieltä","Hankit ilmaisia V-Buckseja","Voitit giveawayn","Keitit metamfetamiinia","Myit sielusi","Myit growtopia-tilisi","Pyysit hyvitystä discord nitrosta"]
    earnings = random.randrange(300)
  
    
  embed = discord.Embed(color=0x70db70, title="Työ", description=f"{random.choice(työ)}, sait siitä {earnings}€")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)
  
  users[str(user.id)]["wallet"] += earnings
  
  with open("bank.json","w") as f:
    users = json.dump(users,f)
    
@työ.error
async def varoita_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(color=0xff0000, title=f"Sinun pitää odottaa {round(error.retry_after, 2)} sekunttia ennen kun voit suorittaa tämän komennon!", description=f"")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed, ephemeral=True)
#--------------------------TYÖ--------------------------#

#--------------------------WITHDRAW--------------------------#
@bot.slash_command(name="withdraw",description="Nosta rahaa pankkitililtä")
async def withdraw(ctx,amount = None):
  global latest_command
  await open_account(ctx.author)
  latest_command = "/withdraw"
  if amount == None:
    embed = discord.Embed(color=0xe6ffff, title="Nosta", description=f"Et laittanut määrää!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    return

  bal = await update_bank(ctx.author)

  amount = int(amount)
  if amount>bal[1]:
    embed = discord.Embed(color=0xe6ffff, title="Nosta", description=f"Sinulla ei ole tarpeeksi rahaa!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral=True)
    return

  if amount<0:
    embed = discord.Embed(color=0xe6ffff, title="Nosta", description=f"Määrän pitää olla positiivinen")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral=True)
    return

  await update_bank(ctx.author,amount)
  await update_bank(ctx.author,-1*amount,"bank")

  embed = discord.Embed(color=0x70db70, title="Nosta", description=f"Nostit {amount}€ pankkitililtäsi")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(10)
  await ctx.defer(embed=embed, hidden = True)
#--------------------------WITHDRAW--------------------------#

#--------------------------RYÖSTÄ--------------------------#
@bot.slash_command(name="varasta",description="testi komento; :D 9/1/23")
@commands.cooldown(1, 3000, commands.BucketType.user)
async def steal(ctx, user: discord.Member):
  global latest_command
  latest_command = "/varasta"
  random_chance = random.randint(0,2)
  users = await get_bank_data()
  await open_account(ctx.author)
  await open_account(user)
 
  target_wallet_amt = users[str(user.id)]["wallet"]
  steal_wallet_amt = users[str(ctx.author.id)]["wallet"]
  steal_bank_amt = users[str(ctx.author.id)]["bank"]
  steal_cash = (steal_bank_amt + steal_wallet_amt)



  if user == ctx.author:
    embed = discord.Embed(color=0xff0000, title="Varasta", description=f"Et voi varastaa itseltäsi!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    return
  
  if steal_cash < 100:
    embed = discord.Embed(color=0xff0000, title="Varasta", description=f"Tarvitset vähintään 100€, sinulla on {steal_cash}")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    return
  
  if target_wallet_amt <= 3:
    amount = random.randint(100,steal_cash // 2)
    embed = discord.Embed(color=0xff0000, title="Varasta", description=f"Jäit kiinni! käyttäjällä ei ollut rahaa lompakossa!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.add_field(name=f"Sinun pitää maksaa {amount}€",value="‌")
    await ctx.respond(embed=embed)
    if steal_wallet_amt < amount:
      await update_bank(ctx.author,-1*steal_wallet_amt,"wallet")
      amount - steal_wallet_amt
      await update_bank(ctx.author,-1*amount,"bank")
      return
    else:
      await update_bank(ctx.author,-1*amount,"wallet")
      return
    
    
  if random_chance == 0 or 1:
    embed = discord.Embed(color=0xff0000, title="Varasta", description=f"Jäit kiinni!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.add_field(name=f"Sinun pitää maksaa {amount}€",value="‌")
    await ctx.respond(embed=embed)
    if steal_wallet_amt < amount:
      await update_bank(ctx.author,-1*steal_wallet_amt,"wallet")
      amount - steal_wallet_amt
      await update_bank(ctx.author,-1*amount,"bank")
  else:
  
    amount = random.randint(1, target_wallet_amt)
    await update_bank(user,-1*amount,"wallet")
    await update_bank(ctx.author,1*amount,"wallet")
    embed = discord.Embed(color=0x70db70, title="Varasta", description=f"Varastit {amount}€ {user.name}:lta")

    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    

@steal.error
async def varoita_error(ctx, error):
    if isinstance(error, commands.CommandOnCooldown):
      embed = discord.Embed(color=0xff0000, title=f"Sinun pitää odottaa {round(error.retry_after, 2)} sekunttia ennen kun voit suorittaa tämän komennon!", description=f"")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed, ephemeral=True)
#--------------------------RYÖSTÄ--------------------------#  
#--------------------------DEPOSIT--------------------------#
@bot.slash_command(name="deposit",description="Talleta pankkitilille")
async def withdraw(ctx,amount):
  global latest_command
  latest_command = "/deposit"
  try:
      
    await open_account(ctx.author)
    users = await get_bank_data()
  
  
    if amount == "all":
      amount = users[str(ctx.author.id)]["wallet"]
      await update_bank(ctx.author,-1*amount)
      await update_bank(ctx.author,amount,"bank")
      embed = discord.Embed(color=0x70db70, title="Talleta", description=f"Talletit {amount}€ pankkitiliisi")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
      return
      
    if amount == 0:
      embed = discord.Embed(color=0xe6ffff, title="Talleta", description=f"Et laittanut määrää!")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed,ephemeral=True)
      return
  
    bal = await update_bank(ctx.author)
  
    amount = int(amount)
    if amount>bal[0]:
      embed = discord.Embed(color=0xe6ffff, title="Talleta", description=f"Sinulla ei ole tarpeeksi rahaa!")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed, ephemeral=True)
      return
  
    if amount<0:
      embed = discord.Embed(color=0xe6ffff, title="Talleta", description=f"Määrän pitää olla positiivinen")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed, ephemeral=True)
      return
  
    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")
  
    embed = discord.Embed(color=0x70db70, title="Talleta", description=f"Talletit {amount}€ pankkitiliisi")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)

  except Exception as e:
    embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
    await ctx.respond(embed=embed)
#--------------------------DEPOSIT--------------------------#

#--------------------------KAUPPA--------------------------#
@bot.slash_command(name="kauppa",description="Näyttää saatavilla olevat itemit")
async def kauppa(ctx):
  embed = discord.Embed(color=0xe6ffff, title="Kauppa")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  global latest_command
  latest_command = "/kauppa"
  
  for item in shop:
    name = item["name"]
    price = item["price"]
    description = item["description"]
    
    embed.add_field(name = name, value=f"***{price}€***")
  await ctx.respond(embed=embed)



@bot.slash_command(name="osta",description="Osta itemi")
async def buy(ctx,item,amount = 1):
    global latest_command
    latest_command = "/osta"
    await open_account(ctx.author)

    res = await buy_this(ctx.author,item,amount)

    if not res[0]:
        if res[1]==1:
            embed = discord.Embed(color=0xe6ffff, title="Osta", description=f"Itemiä ei ole olemassa!")
            embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
            await ctx.respond(embed=embed)
            return
        if res[1]==2:
            embed = discord.Embed(color=0xe6ffff, title="Osta", description=f"Sinulla ei ole tarpeeksi rahaa ostaa tätä!")
            embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
            await ctx.respond(embed=embed)
            return

    embed = discord.Embed(color=0xe6ffff, title="Osta", description=f"Ostit juuri {amount}x {item}!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
    if item =="vip":
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1041672104434745344)
      await ctx.author.add_roles(role)
      
    elif item =="kala":
      member = ctx.author
      role = discord.utils.get(member.guild.roles, id=1060872775432155177)
      await ctx.author.add_roles(role)


@bot.slash_command(name="tavarat",description="Näytää sinun inventorin")
async def bag(ctx):
    global latest_command
    latest_command = "/tavarat"
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    try:
        bag = users[str(user.id)]["bag"]
    except:
        bag = []


    em = discord.Embed(color=0xe6ffff,title = "Tavarat")
    for item in bag:
        name = item["item"]
        amount = item["amount"]
        if amount == 1:
          em.add_field(name = f"{name.capitalize()},",value = "‌") 
        else:
          em.add_field(name = f"{name.capitalize()}: x{amount},",value = "‌") 
           

    await ctx.respond(embed = em)    


async def buy_this(user,item_name,amount):
    item_name = item_name.lower()
    name_ = None
    for item in shop:
        name = item["name"].lower()
        if name == item_name:
            name_ = name
            price = item["price"]
            break

    if name_ == None:
        return [False,1]

    cost = price*amount

    users = await get_bank_data()

    bal = await update_bank(user)

    if bal[0]<cost:
        return [False,2]


    try:
        index = 0
        t = None
        for thing in users[str(user.id)]["bag"]:
            n = thing["item"]
            if n == item_name:
                old_amt = thing["amount"]
                new_amt = old_amt + amount
                users[str(user.id)]["bag"][index]["amount"] = new_amt
                t = 1
                break
            index+=1 
        if t == None:
            obj = {"item":item_name , "amount" : amount}
            users[str(user.id)]["bag"].append(obj)
    except:
        obj = {"item":item_name , "amount" : amount}
        users[str(user.id)]["bag"] = [obj]        

    with open("bank.json","w") as f:
        json.dump(users,f)

    await update_bank(user,cost*-1,"wallet")

    return [True,"Worked"]

#--------------------------LÄHETÄ--------------------------#
@bot.slash_command(name="lähetä",description="Lähetä rahaa jollekkin")
async def withdraw(ctx,member:discord.Member,amount = None):
  global latest_command
  latest_command = "/lähetä"
  await open_account(ctx.author)
  await open_account(member)

  if amount == None:
    embed = discord.Embed(color=0xe6ffff, title="Lähetä", description=f"Et laittanut rahamäärää!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral=True)
    return

  bal = await update_bank(ctx.author)

  amount = int(amount)
  if amount>bal[1]:
    embed = discord.Embed(color=0xe6ffff, title="Lähetä", description=f"Sinulla ei ole tarpeeksi rahaa!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral=True)
    return

  if amount<0:
    embed = discord.Embed(color=0xe6ffff, title="Lähetä", description=f"Laita positiivinen numero!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral=True)
    return

  await update_bank(ctx.author,-1*amount,"bank")
  await update_bank(member,amount,"bank")


  embed = discord.Embed(color=0x70db70, title="Lähetä", description=f"Annoit {amount}€ käyttäjälle <@{member.id}>")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)

#--------------------------LÄHETÄ--------------------------#
@bot.slash_command(name="avain",description="Anta ihmisille avaimet joita voi käyttää vain pari kertaa")
async def key(ctx,kk,avain,tila):
  if avain != "6424418891817288101033278946093060116":
    return
  with open("key.json","r") as f:
    keys = json.load(f)
  ascii = string.ascii_letters + string.digits
  key = "".join(random.choice(ascii)for i in range(12))
  keys[str(key)] = {}
  keys[str(key)]["amount"] = int(kk)
  keys[str(key)]["command"] = str(tila)
  with open("key.json","w") as f:
    json.dump(keys,f)
  await ctx.respond(key,ephemeral = True)
#--------------------------AUTTAJAT--------------------------#
@bot.slash_command(name="auttajat",description="Antaa listan auttajista")
async def baller(ctx):
  global latest_command
  latest_command = "/auttajat"
  embed = discord.Embed(color=0xe6ffff, title="Auttajat", description=f"<@1005597854590578759>, <@496298010637107220> ja <@791751178446176276>")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)
#--------------------------AUTTAJAT--------------------------#
  
#--------------------------MEEMI--------------------------#
@bot.slash_command(name="meemi",description="Laittaa meemin")
async def baller(ctx):
  latest_command = "/meemi"
  await ctx.respond(f"‎")
  emb = await ctx.send(embed=await pyrandmeme())
  await emb.add_reaction("👍")
  await emb.add_reaction("👎")
#--------------------------MEEMI--------------------------#
  
#--------------------------ÄÄNESTYS--------------------------#
@bot.slash_command(name="äänestys",description="Tekee äänestyksen")
async def aanestys(ctx,nimi,aihe, vari: Option(required = False, default=hex(0xe6ffff))):
  try:
    global latest_command
    latest_command = "/äänestys"
      
    embed = discord.Embed(color=int(vari, 16),title="", description="")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.add_field(name=f"{nimi}", value=f"{aihe}",inline=True)
    emb = await ctx.send(embed=embed)
    await emb.add_reaction("👍")
    await emb.add_reaction("👎")
  except ValueError as e:
    await ctx.respond('{vari} ei ole väri, käytä tätä mallia: "0x(hex koodi)"')
#--------------------------ÄÄNESTYS--------------------------#

#--------------------------DATAHAKU--------------------------#
@bot.slash_command(name="vanha-datahaku",description="Etsii tiedostoa")
async def datahaku(ctx, sana):
  global latest_command
  latest_command = "/datahaku"
  if sana == "upload.data()":
    await ctx.respond("Senpai tässä tiedostoni ;)", file=discord.File(f"messages.txt"),ephemeral=True)
  
  else:
    
    try:
  
      with open("messages.txt","r") as f:
        data = f.readlines()
  
      data = [element.lower() for element in data]
      lowersana = sana.lower()
      if len(sana) > 1000:
        sana = "Sana löytyi, mutta virkettä ei voida näyttää sanarajoituksen vuoksi"
      
      if any(f"{lowersana}" in s for s in data):
        embed = discord.Embed(color=0x00c900,title="Data Haku", description=f'Sana **"{sana}"** löytyi arkistosta.')
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      else:
        embed = discord.Embed(color=0xc90000,title="Data Haku", description=f'Sana **"{sana}"** ei löytynyt arkistosta.')
        embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
      
  
    except Exception as e:
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)
#--------------------------DATAHAKU--------------------------#

#--------------------------ECONOMY--------------------------#

#--------------------------ECONOMY--------------------------#   
      
#--------------------------NIMI--------------------------#
@bot.slash_command(name="nimi",description="Tekee random nimen (female/male)")
async def baller(ctx, sukupuoli):
  global latest_command
  latest_command = "/nimi"
  embed = discord.Embed(color=0xe6ffff, title="Random Nimi", description=f"{names.get_full_name(gender=f'{sukupuoli}')}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)
#--------------------------NIMI--------------------------#

#--------------------------YLIKÄYTETTYTIKTOKLAULU--------------------------#
@bot.slash_command(name="ylikäytettytiktoklaulu",description="Antaa ylikäytetyn tiktok laulun")
async def baller(ctx):
  global latest_command
  latest_command = "/ylikäytettytiktoklaulu"
  from variables_load import random_laulu
  tt_laulu = random.choice(random_laulu)
  await ctx.respond(f"{tt_laulu}")

#--------------------------YLIKÄYTETTYTIKTOKLAULU--------------------------#

@bot.slash_command(name="vastaus",description="Testi")

async def vastaus(ctx, vastaus, salasana):
  global latest_command
  with open("key.json","r") as f:
    passwords = json.load(f)
  if salasana not in passwords:
    embed = discord.Embed(color=0xe6ffff,title = f"Vastaus",description=f'Väärä salasana!')
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral = True)
    return
  if passwords[str(salasana)]["command"] != "vastaus":
    embed = discord.Embed(color=0xe6ffff,title = f"Vastaus",description=f'Salasana ei ole tarkoitettu tälle komennolle!')
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral = True)
    return
  if passwords[str(salasana)]["amount"] == 0:
    embed = discord.Embed(color=0xe6ffff,title = f"Vastaus",description=f'Salasana on vanhentunut!')
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed, ephemeral = True)
    return
  passwords[str(salasana)]["amount"] -= 1
  with open("key.json","w") as f:
    json.dump(passwords,f)
    
  latest_command = "/vastaus"
  response.append(vastaus)
  
  with open("response.txt","a") as f:
    f.write(f"{vastaus}\n")
    
  embed = discord.Embed(color=0xe6ffff,title = f"Lisättiin vastaus",description=f'"**{vastaus}**"')
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.set_footer(text=f"{passwords[str(salasana)]['amount']} Käyttökertaa jäljellä")
  await ctx.respond(embed=embed, ephemeral = True)
@vastaus.error
async def chnick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)

#--------------------------GREG--------------------------#
@bot.slash_command(name="greg",description="Ottaa random Gregin")
async def baller(ctx):
  global latest_command
  latest_command = "/greg"
  gchoice = random.choice(greg_list)
  if gchoice == "gpengu":
    from variables_load import gpengu_link
    await ctx.respond(f"{gpengu_link}")

  elif gchoice == "gmonster":
    from variables_load import gmonster_link
    await ctx.respond(f"{gmonster_link}")

  elif gchoice == "gheffley":
    from variables_load import gheffley_link
    await ctx.respond(f"{gheffley_link}")

  elif gchoice == "gfamilyguy":
    from variables_load import gfamilyguy_link
    await ctx.respond(f"{gfamilyguy_link}")

  elif gchoice == "gdeer":
    from variables_load import gdeer_link
    await ctx.respond(f"{gdeer_link}")

  elif gchoice == "gggreg":
    from variables_load import gggreg_link
    await ctx.respond(f"{gggreg_link}")
#--------------------------GREG--------------------------#

#--------------------------SÄÄ--------------------------#
@bot.slash_command(name="sää",description="Tekee randomin sää ennusteen")
async def baller(ctx):
  global latest_command
  latest_command = "/sää"
  from variables_load import temp
  from variables_load import weat
  embed = discord.Embed(color=0xe6ffff, title="Random Sää", description=f"Huomenna {random.choice(weat)} ja lämpötila on {random.choice(temp)}°C")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------SÄÄ--------------------------#
@bot.slash_command(name="datahaku",description="Testi")
@commands.has_permissions(manage_messages = True)
async def datahaku(ctx,viesti):
  guild = ctx.guild
  oikea_id = None
  viesti.replace("ä","\u00e4")
  viesti.replace("Ä","\u00e4")
  viesti.replace("ö","\u00f6")
  viesti.replace("Ö","\u00f6")
  oikea_viesti = None
  with open("messages.json","r") as f:
    messages = json.load(f)
  for user_id, user_data in messages.items():
    for message in user_data["message"]:
      if viesti.lower() in message.lower():
        oikea_id = user_id
        oikea_viesti = user_data["message"]
        break
  if oikea_id is not None:
    kkk = "".join(oikea_viesti)
    if len(kkk) > 900:
      viesti = "Sana löytyi, mutta virkettä ei voida näyttää sanarajoituksen vuoksi"
    auth = guild.get_member(int(oikea_id))
    embed = discord.Embed(color=0x70db70,title=f'"{viesti}"')
    embed.set_author(name=f"{auth}", icon_url = auth.avatar)
    embed.add_field(name=f"Viesti:", value=kkk.replace(viesti,f'**"{viesti.upper()}"**'))
    embed.set_footer(text="Permission: administrator")
    await ctx.respond(embed=embed)
  else:
    embed = discord.Embed(color=0xff0000)
    embed.add_field(name=f"Viestiä ei löytynyt",value=f'"{viesti}"')
    embed.set_author(name=f"{ctx.author}", icon_url = ctx.author.avatar)
    embed.set_footer(text="Permission: administrator")
    await ctx.respond(embed=embed)
#--------------------------EMOJI--------------------------#
@bot.slash_command(name="emoji",description="Muuttaa tekstin emojeiksi")

async def baller(ctx, teksti: str):
  global latest_command
  latest_command = "/emoji"
  f_str = ""

  #paskaa * aikaa tuhlattu = ~2h
  from variables_load import cust_alphabet
  processed_teksti = teksti.replace("ä","a").replace("ö","o").replace("å","ao")
  for character in processed_teksti.lower():
    if character in cust_alphabet:
      f_str += f":regional_indicator_{character}: " 
    else:
      pass
   
  await ctx.respond(f_str)
#--------------------------EMOJI--------------------------#
  
#--------------------------Admin--------------------------#
@bot.slash_command(name="asetus-tarina_kanava",description="Muttaa tarina kanavan")
@commands.has_permissions(administrator = True)
async def asetus_tarina_kanava(ctx, kanava: discord.TextChannel):
  current_channel = await check_settings(guild_id = ctx.guild.id, setting = "story_channel")
  if str(kanava.id) == str(current_channel):
    await change_settings(guild_id=ctx.guild.id,setting="story_channel",mode=None)
    embed = discord.Embed(color=0xff0000,title=f"Poistettiin tarinakanava",description=f"<#{kanava.id}>")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)

  else:
    
    await change_settings(guild_id=ctx.guild.id,setting="story_channel",mode=str(kanava.id))
    embed = discord.Embed(color=0xe6ffff,title=f"Lisättiin tarinakanava",description=f"<#{kanava.id}>")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)

@bot.slash_command(name="asetus-salli_välilyötni",description="Muttaa tarina kanavan")
async def asetus_tarina_kanava(ctx, salli:bool):
  await change_settings(guild_id=ctx.guild.id,setting="allow_spaces",mode=salli)
  embed = discord.Embed(color=0xe6ffff,title=f"Vaihdettiin `allow_spaces`",description=f"Se on nyt tilassa: `{salli}`")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await ctx.respond(embed=embed)
async def create_settings(guild_id):
  with open("config.json","r") as f:
    settings = json.load(f)
  if str(guild_id) in settings:
    return False
  else:
    settings[str(guild_id)] = {}
    settings[str(guild_id)]["story_channel"] = None
    settings[str(guild_id)]["chat_channel"] = None
    settings[str(guild_id)]["allow_spaces"] = False
    settings[str(guild_id)]["max_lenght"] = 10
    settings[str(guild_id)]["admin_channel"] = None
    with open("config.json","w") as f:
      json.dump(settings,f)
    return True

async def change_settings(guild_id,setting,mode):
  await create_settings(guild_id=guild_id)
  with open("config.json","r") as f:
    settings = json.load(f)
  settings[str(guild_id)][str(setting)] = mode
  with open("config.json","w") as f:
    json.dump(settings,f)

async def check_settings(guild_id,setting):
  await create_settings(guild_id=guild_id)
  with open("config.json","r") as f:
    settings = json.load(f)
  return settings[str(guild_id)][str(setting)]
@bot.slash_command(name="tarina",description="Näyttää tarinan")
async def tarina(ctx):
  global latest_command
  latest_command = "/tarina"
  with open("story.json","r") as f:
    current_story = json.load(f)
  kanava = ctx.channel
  if str(ctx.channel.id) in current_story:
    if current_story[str(ctx.channel.id)] == "!res":
      embed = discord.Embed(color=0xe6ffff,title=f"Tarina",description=f"Kanavalla <#{kanava.id}> ei ole tarinaa käynnissä!")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
      return
    else:

      embed = discord.Embed(color=0xe6ffff,title=f"Tarina",description=f'"*{current_story[str(ctx.channel.id)]}*"')
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      a = await check_settings(guild_id = ctx.guild.id,setting="max_lenght")
      b = await check_settings(guild_id = ctx.guild.id,setting="allow_spaces")
      embed.set_footer(text=f"Isoin viestin pituus: {a}, Salli välilyönnit: {b}")
      await ctx.respond(embed=embed)
  else:
    embed = discord.Embed(color=0xe6ffff,title=f"Tarina",description=f"Kanavalla <#{kanava.id}> ei ole tarinaa käynnissä!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)


@bot.slash_command(name="tarina-reset",description="Poistaa tarinan")
async def tarina(ctx):
  global active_
  global l_f_m
  global reactions_1
  max_react = 2
  global latest_command
  latest_command = "/tarina-reset"
  with open("story.json","r") as f:
    current_story = json.load(f)
  if str(ctx.channel.id) in current_story:

      
    embed = discord.Embed(color=0xe6ffff,title=f"Tarina",description=f"Poistetaanko tarina? (3 ääntä)")
    end_time = int(time.time() + 120)
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    message = await ctx.send(embed=embed)
    await message.add_reaction("✅")
    await message.add_reaction("❌")
    reactions = ["✅", "❌"]
    reactions_1["✅"] = 1
    l_f_m = True
    for i in range(120):
      await asyncio.sleep(1)
      print(reactions_1)
      if reactions_1["✅"] >= 3:
        l_f_m = False
        current_story[str(ctx.channel.id)] = "!res"
        with open("story.json","w") as f:
          json.dump(current_story,f)
        await ctx.send("Poistetiin tarina.")
        reactions_1["✅"] = 0
        l_f_m = False
        break
        
    
    
  else:
    await ctx.respond("Tarinaa ei ole olemassa!")
#--------------------------Admin--------------------------#
@bot.slash_command(name="admin-kanava",description="testi komento")
@commands.has_permissions(administrator = True)
async def admin_channel(ctx, kanava:discord.TextChannel):
  global latest_command
  latest_command = "/admin-kanava"
  current_channel = await check_settings(guild_id=ctx.guild.id,setting="admin_channel")
  if str(current_channel) == str(kanava.id):
    await change_settings(guild_id=ctx.guild.id,setting="admin_channel",mode=None)
    embed = discord.Embed(color=0xff0000,title=f"Poistettiin admin-kanava",description=f"<#{kanava.id}>")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
  else:
    await change_settings(guild_id=ctx.guild.id,setting="admin_channel",mode=str(kanava.id))
    embed = discord.Embed(color=0xe6ffff, title=f"Lisättiin admin-kanava",description=f"<#{kanava.id}>")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
#--------------------------ACTIVATE--------------------------#
@bot.slash_command(name="kanava",description="testi komento")
@commands.has_permissions(administrator = True)
async def activate(ctx, kanava: discord.TextChannel):
  global latest_command
  latest_command = "/kanava"
  current_channel = await check_settings(guild_id=ctx.guild.id,setting="chat_channel")


  if str(kanava.id) == str(current_channel):
    await change_settings(guild_id=ctx.guild.id,setting="chat_channel",mode=None)
    embed = discord.Embed(color=0xff0000,title=f"Poistettiin kanava <#{kanava.id}>")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.set_footer(text="Permission: administrator")
    await ctx.respond(embed=embed)
  else:
    await change_settings(guild_id=ctx.guild.id,setting="chat_channel",mode=str(kanava.id))
    embed = discord.Embed(color=0xe6ffff, title="Kanava", description=f"Kanava <#{kanava.id}> on lisätty!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)

@activate.error
async def chnick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)

#--------------------------BALLERDATA--------------------------#
@bot.slash_command(name="ballerdata",description="Ei baller keräile mitään :)")
async def ballerdata(ctx):
    global latest_command
    latest_command = "/ballerdata"
    try:
      with open(r"messages.txt", 'r') as fp:
        lines = len(fp.readlines())
        size = os.path.getsize('messages.txt')


      embed=discord.Embed(title="**```Ballerin Keräämät Tiedot```**", description="**Tätä tietoa ei myydä**", color=0xf8e45c)
      embed.add_field(name=f"Koko: {size} b", value="Koko on byteissä*", inline=True)
      embed.add_field(name=f"Linjoja: {lines}", value="1 Linja = 1 Viesti*", inline=True)

      await ctx.respond(embed=embed)
      
    except Exception as e:
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)

#--------------------------BALLERDATA--------------------------#
@bot.slash_command(name="top_juusto",description="Antaa listan top 10 isointa level")
async def toplevel(ctx):
  global latest_command
  latest_command = "/top_level"
  
  with open("level.json","r") as f:
    levels_ = json.load(f)
  target_guild = str(ctx.guild.id)
  if target_guild in levels_:
    target_guild_levels = levels_[target_guild]
    embed = discord.Embed(color=0xe6ffff, title="Top Level")
    sorted_levels = sorted(target_guild_levels.items(), key=lambda x: x[1], reverse=True)
    top_10 = sorted_levels[:10]
    for i,(person, level) in enumerate(top_10):
      if level == 0:
        break
      else:
        embed.add_field(name=f"#{i + 1}", value=f"<@{person}>: {level} 🧀", inline=True)
        embed.add_field(name='', value='', inline=False)
    await ctx.respond(embed=embed)
  else:
    embed = discord.Embed(color=0xe6ffff, title="Top Juusto",description="Kukaan ei ole saanut juustopisteitä")
    await ctx.respond(embed=embed)
      
  

  
  #for i, (person, levels) in enumerate(top_10.items()):
  #  
  #  
    
  #await ctx.respond(embed=embed)
#--------------------------BALLERNIMI--------------------------#
@bot.slash_command(name="ballernimi",description="Muuttaa Ballerin nimen")
@commands.has_permissions(manage_nicknames = True)
async def chnick(ctx, nick):
    global latest_command
    latest_command = "/ballernimi"
    try:
      await ctx.guild.me.edit(nick=nick)
      embed = discord.Embed(color=0xe6ffff, title="Baller Nimi", description=f'Vaihdettiin nimi "{nick}"')
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await asyncio.sleep(1)
      await ctx.respond(embed=embed)
    except MissingPermissions as e:
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await asyncio.sleep(1)
      await ctx.respond(embed=embed)

@chnick.error
async def chnick_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)
#--------------------------BALLERNIMI--------------------------#

#--------------------------YP--------------------------#
@bot.slash_command(name="yp",description="Antaa ylläpitojen tarkoitukset (kilpailu @game_chicken1)")
async def baller(ctx):
  global latest_command
  latest_command = "/yp"
  from variables_load import yp_text
  embed = discord.Embed(color=0xe6ffff,title="Ylläpito", description=f"{yp_text}")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------YP--------------------------#

#--------------------------UNIMI--------------------------#
@bot.slash_command(name="unimi",description="Tekee randomin peli-nimen")
async def baller(ctx):
  global latest_command
  latest_command = "/unimi"
  ggtag = random.choice(gg_tag)
  xtag = random.choice(xxx_tag)
  if ggtag == 1:
    ggtagvar = "Gamer"
  else:
    ggtagvar = ""
  if xtag == 1:
    xtagvar = "xxx"
  else:
    xtagvar = ""

  

  embed = discord.Embed(color=0xe6ffff, title="Random Nimi", description=f"**```{xtagvar}{random.choice(unimi)}{ggtagvar}{random.randint(0,100)}{xtagvar}```**")
  embed.add_field(name="Lisää Nimi", value=f"Jos haluat lisätä nimen, tee se ```/uusinimi``` komennolla!",inline=True)
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------UNIMI--------------------------#

#--------------------------UUSINIMI--------------------------#
@bot.slash_command(name="uusinimi",description="Lisää nimen unimi komentoon")
@commands.has_permissions(manage_nicknames = True)

async def uusinimi(ctx, nimi):
  global latest_command
  latest_command = "/uusinimi"
  if nimi.lower() in unimi:
    embed = discord.Embed(color=0xe6ffff, title="Nimeä ei lisätty", description=f"**{nimi.lower()}** on jo olemassa!")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
    return
  try:
    fname = nimi.lower()
    unimi.append(fname)
    
    fh = open("unimi.pkl", 'wb')
    pickle.dump(unimi, fh)
    fh.close()
    embed = discord.Embed(color=0xe6ffff, title="Nimi On Lisätty!", description=f"Nimesi voi näyttää tältä: **xxx_{fname}Gamer66_xxx**")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
  except Exception as e:
    print(e)
    embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
  
  
@uusinimi.error
async def uusinimi_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      await ctx.respond(embed=embed)
#--------------------------UUSINIMI--------------------------#
          
#--------------------------AUTA--------------------------#
@bot.slash_command(name="auta",description="Antaa komento listan")
async def baller(ctx):
  global latest_command
  latest_command = "/auta"
  embed = discord.Embed(color=0xe6ffff, title="Auta", description=f"Apua löytyy täältä: <https://pastebin.com/KfSey12H>")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------AUTA--------------------------#
#--------------------------SANO--------------------------#
@bot.slash_command(name="sano",description="Lähetä viesti ballerina")
async def sano(ctx,viesti):
  global latest_command
  latest_command = "/sano"
  with open("commands.json","a") as f:
    f.write(f"{d2} | <@{ctx.author.id}> sanoi {viesti}\n")
  
  embed_eph = discord.Embed(color=0xe6ffff, title = "Sano", description =f"Lähetetään viestiä {viesti}")
  await ctx.respond(embed=embed_eph,ephemeral=True)
  await ctx.send(viesti)
#--------------------------RANDOM--------------------------#
@bot.slash_command(name="random",description="Antaa random numeron")
async def baller(ctx, minimi, maximi):
  global latest_command
  latest_command = "/random"
  embed = discord.Embed(color=0xe6ffff, title="Random Numero", description=f"Numerosi on: **{random.randint(int(minimi),int(maximi))}**")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------RANDOM--------------------------#

#--------------------------BALLERINFO--------------------------#
@bot.slash_command(name="ballerinfo",description="antaa tekijän nimen")
async def baller(ctx):
  global latest_command
  latest_command = "/ballerinfo"
  embed = discord.Embed(color=0xe6ffff, title="Ballerinfo", description=f"Baller on discord botti koodattuna pythonilla")
  embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
  await asyncio.sleep(1)
  await ctx.respond(embed=embed)
#--------------------------BALLERINFO--------------------------# 

#--------------------------SPAM--------------------------#
@bot.slash_command( name="spam", description="Spämmii")
@commands.has_permissions(administrator = True)
async def spam(ctx, sana, kertaa):
  global latest_command
  latest_command = "/spam"
  try:
    with open ("commands.json","a") as f:
      f.write(f"{d2} | <@{ctx.author.id}> spämmi {sana} {kertaa} kertaa\n")
    embed = discord.Embed(color=0xe6ffff, title="Spämmiminen", description=f"Spämmiminen on otettu pois käytöstä.")
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
    #for i in range(int(kertaa)):
   
      
  except Exception as e:
    embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
    embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
    
@spam.error
async def uusinimi_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
#--------------------------SPAM--------------------------#

#--------------------------POISTA--------------------------#
@bot.slash_command(name="poista",description="Poistaa tietyn määrän viestejä")
@commands.cooldown(1, 5, commands.BucketType.user)
@commands.has_permissions(manage_messages = True)
async def kuolema(ctx, messages: Option(int,description="Kuinka monta haluat poistaa?",required=True)):
  global latest_command
  latest_command = "/poista"
  try:
    f = open("commands.json", "a")
    f.write(f"{d2} | <@{ctx.author.id}> poisti {messages} viestejä\n")
    f.close()
    await ctx.defer()
    z = await ctx.channel.purge(limit=messages+1)
  
    await ctx.respond(f"Kuolema {len(z)}")
  except Exception as e:
    embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
    embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await asyncio.sleep(1)
    await ctx.respond(embed=embed)
    
@kuolema.error
async def uusinimi_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```Sinulla ei ole oikeuksia käyttää tätä komentoa!```")
      embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
#--------------------------POISTA--------------------------#

#--------------------------HAKU--------------------------#
@bot.slash_command(name="haku",description="Hakee jotain wikipediasta, | VIRKKEITÄ TARKOITTAA KUINKA **MONTA** VIRKETTÄ")
async def haku(ctx, hakutermi, virkkeitä):
  global latest_command
  latest_command = "/haku"
  try:
    wikipedia.set_lang("fi")
    anws = wikipedia.summary(f"{hakutermi}", sentences={virkkeitä})
    if "(" in anws:
      a = 1
      virk = int(virkkeitä) +a
      anws = wikipedia.summary(f"{hakutermi}", sentences={virk})
      embed = discord.Embed(color=0xe6ffff, title="Wikipedia Haku", description=f"```{anws}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)
    else:
      anws = wikipedia.summary(f"{hakutermi}", sentences={virkkeitä})
      await asyncio.sleep(1)
      embed = discord.Embed(color=0xe6ffff, title="Wikipedia Haku", description=f"```{anws}```")
      embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
      await ctx.respond(embed=embed)

  except Exception as e:
    
    print(e)
    embed = discord.Embed(color=0xff0000, title="Virhe!", description=f"```{e}```")
    embed.add_field(name="Bug Report", value=f" Bug report löytyy täältä: <https://tinyurl.com/ballerbugreport>",inline=True)
    await asyncio.sleep(1)
    embed.set_author(name=ctx.author.name, icon_url = ctx.author.avatar)
    await ctx.respond(embed=embed)
#--------------------------HAKU--------------------------#


def printit():
  threading.Timer(10.0, printit).start()
  print(f"\n")


keep_alive()

printit()
try:
  TOKEN = os.environ.get("DISCORD_BOT_SECRET")
  bot.run(TOKEN)



except discord.errors.HTTPException:
  print("429")

