import discord #importing stuff
from discord.ext import commands
from operator import itemgetter
import requests
import csv
import io
import functions
from bs4 import BeautifulSoup
    
def sort_array(array):
    from operator import itemgetter
    b = []
    for index in range(len(array)):
        b.append([array[index][0],int((array[index][1]).replace(',',''))])
    return sorted(b,key=itemgetter(1))[::-1]

client = commands.Bot(command_prefix='/') #Your command prefix

@client.event
async def on_ready(): #initializing the bot
    print('Bot started.')
    await client.change_presence(game=discord.Game(name="Build Battle"))

@client.command(name="bbhelp")
async def bbhelp():
    message="```fix\nCommands:\n/guild [username] - Find the guild of given username\n/score - Displays Top 10 Score\n/wins - Displays Top 10 Wins\n/solo - Displays Top 10 Solo Wins\n/teams - Displays Top 10 Teams Wins\n```"
    await client.say(message)

@client.command(name="hi")
async def hi():
    message='Hello there! Type /bbhelp to see what I can do!'
    await client.say(message)

@client.command(name="guild")
async def guild(user):
    r=requests.get('https://plancke.io/hypixel/guild/player/'+user)
    soup=BeautifulSoup(r.text,'html.parser')
    result=soup.find('div',attrs={'class':'card-box'})
    guild=result.contents[4]
    message='```fix\n'+guild+'```'
    await client.say(message)

@client.command(name='score') #12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo
async def score():
    ssd=functions.get_spreadsheet_data('12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo')
    message='```fix\nScore```\n```cpp\n'
    message+='#'.ljust(4)+'Player'.ljust(14)+'Score'.ljust(10)+'Deficit'.ljust(10)+'\n'
    for p in range(10):
        message+=(str(p+1)+'. ').ljust(4)+(functions.get_cell_with_data(ssd,2,3+p)).ljust(14)+(functions.get_cell_with_data(ssd,3,3+p)).ljust(10)+(functions.get_cell_with_data(ssd,4,3+p)).ljust(10)+'\n'
    message+='```'
    await client.say(message)

@client.command(name='coins')
async def coins():
    ssd=functions.get_spreadsheet_data('12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo')
    message='```fix\nCoins```\n```cpp\n'
    message+='#'.ljust(4)+'Player'.ljust(14)+'Coins'.ljust(12)+'Deficit'.ljust(10)+'\n'
    for p in range(10):
        message+=(str(p+1)+'. ').ljust(4)+(functions.get_cell_with_data(ssd,2,58+p)).ljust(14)+(functions.get_cell_with_data(ssd,3,58+p)).ljust(12)+(functions.get_cell_with_data(ssd,4,58+p)).ljust(10)+'\n'
    message+='```'
    await client.say(message)

@client.command(name='wins')
async def wins():
    ssd=functions.get_spreadsheet_data('12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo')
    message='```fix\nWins```\n```cpp\n'
    message+='#'.ljust(4)+'Player'.ljust(14)+'Wins'.ljust(10)+'Deficit'.ljust(10)+'\n'
    for p in range(10):
        message+=(str(p+1)+'. ').ljust(4)+(functions.get_cell_with_data(ssd,2,71+p)).ljust(14)+(functions.get_cell_with_data(ssd,3,71+p)).ljust(10)+(functions.get_cell_with_data(ssd,4,71+p)).ljust(10)+'\n'
    message+='```'
    await client.say(message)

@client.command(name='solo')
async def solo():
    ssd=functions.get_spreadsheet_data('12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo')
    message='```fix\nSolo Wins```\n```cpp\n'
    message+='#'.ljust(4)+'Player'.ljust(14)+'Wins'.ljust(10)+'Deficit'.ljust(10)+'\n'
    for p in range(10):
        message+=(str(p+1)+'. ').ljust(4)+(functions.get_cell_with_data(ssd,2,94+p)).ljust(14)+(functions.get_cell_with_data(ssd,3,94+p)).ljust(10)+(functions.get_cell_with_data(ssd,4,94+p)).ljust(10)+'\n'
    message+='```'
    await client.say(message)

@client.command(name='teams')
async def teams():
    ssd=functions.get_spreadsheet_data('12fwmoZHLxXR6x99Ja0JtCpV9bIQSt0Fo29VcjYXS2Jo')
    message='```fix\nTeams Wins```\n```cpp\n'
    message+='#'.ljust(4)+'Player'.ljust(14)+'Wins'.ljust(10)+'Deficit'.ljust(10)+'\n'
    for p in range(10):
        message+=(str(p+1)+'. ').ljust(4)+(functions.get_cell_with_data(ssd,2,117+p)).ljust(14)+(functions.get_cell_with_data(ssd,3,117+p)).ljust(10)+(functions.get_cell_with_data(ssd,4,117+p)).ljust(10)+'\n'
    message+='```'
    await client.say(message)

@client.command(name='stats')
async def stats(user):
    r=requests.get('https://namemc.com/profile/'+user)
    soup=BeautifulSoup(r.text,'html.parser')
    user=soup.find('title').text[:-29]
    r=requests.get('https://plancke.io/hypixel/player/stats/'+user)
    soup=BeautifulSoup(r.text,'html.parser')
    result=soup.find('div',attrs={'id':'collapse-2-3'})
    score=result.contents[1].contents[1].contents[0].contents[1]
    solo=result.contents[1].contents[2].contents[1].contents[1].text
    teams=result.contents[1].contents[2].contents[2].contents[1].text
    gtb=result.contents[1].contents[2].contents[3].contents[1].text
    pro=result.contents[1].contents[2].contents[4].contents[1].text
    solo=solo.replace(',','')
    teams=teams.replace(',','')
    gtb=gtb.replace(',','')
    pro=pro.replace(',','')
    solo=int(solo)
    teams=int(teams)
    gtb=int(gtb)
    pro=int(pro)
    wins=solo+teams+gtb+pro
    r=requests.get('https://hypixel.net/player/'+user)
    soup=BeautifulSoup(r.text,'html.parser')
    result=soup.find('div',attrs={'id':'stats-content-build-battle'})
    coins=result.contents[3].contents[3].contents[3].text[1:-1]
    message='```fix\nStats for: '+user+'```\n```cpp\nScore: '.ljust(9)+str(score)+'\nCoins:'.ljust(9)+str(coins)+'\nWins: '.ljust(9)+str(wins)+'\nSolo: '.ljust(9)+str(solo)+'\nTeams: '.ljust(9)+str(teams)+'\nGTB: '.ljust(9)+str(gtb)+'\nPro: '.ljust(9)+str(pro)+'```'
    await client.say(message)
        
client.run('NDUxMTExODIwNTM5NzIzNzk4.DfK0pw.hhQcDESgQ7PmtWBNC3k9Vl-VCxc
           ') #running the bot
