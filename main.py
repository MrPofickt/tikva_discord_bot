import random
import asyncio
import discord
import discord.ext
from discord.ext import commands
from discord import app_commands
from datetime import datetime
import json
import time


intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)


bad_words = ['блять', 'сука', 'ебать', 'пиздец', 'нахуй', 'хуй', 'ебал', 'пидарас', 'пидар', 'мудак', 'муде']
cs_words = [' кс', ' ксго', ' кска', ' cs', ' кс:ка', ' кс:го', ' cs:go', ' кс2', ' cs2', ' кс 2']
smiles = ['7','🎱', '♥', '♠', '💰', '😈', '😎', '🤑', '👹', '☠', '👻', '🥶', '👽', '🧠']
win_slots = {
    '🎱🎱🎱': 50,
    '♥♥♥': 75,
    '♠♠♠': 75,
    '💰💰💰':100,
    '777': 200,
    '😈😈😈': 110,
    '😎😎😎': 120,
    '🤑🤑🤑': 130,
    '👹👹👹': 140,
    '☠☠☠': 150,
    '👻👻👻': 160,
    '🥶🥶🥶':170,
    '👽👽👽': 180,
    '🧠🧠🧠': 190
}


pwp_player = {}
stavka_pwp = {}
pwp_clans = {}
stavka_clans = {}
toaddclans = {}


with open('data.json', 'r') as fr:
    js = json.load(fr)

with open('clans.json', 'r') as clanes:
    cl = json.load(clanes)

on_dolg = 0
daily_a = 0
on_rozogrash = 0
#dop_roz = 0
#d_bosin = 0


#new_bas = 0


len_bs = len(js['users'])
print(len_bs)



def history(mes, mem):
    with open('history.txt', 'a', encoding='utf-8') as f:
        current_datetime = datetime.now()
        f.write(str(mes.content)+ ' ' + str(current_datetime) + str(mem) + '\n')


def sohr_on():
    global js
    with open('data.json', 'w') as fr:
        json.dump(js, fr, indent=4)
    with open('data.json', 'r') as fr:
        js = json.load(fr)

def clans_sohr():
    global cl
    with open('clans.json', 'w') as clanes:
        json.dump(cl, clanes, indent=4)
    with open('clans.json', 'r') as clanes:
        cl = json.load(clanes)



if daily_a != 0:
    for i in js["users"]:
        js["users"][i]["daily"] = 1
    with open('data.json', 'w') as fr:
        json.dump(js, fr, indent=4)
    time.sleep(0.1)
    with open('data.json', 'r') as fr:
        js = json.load(fr)

#if d_bosin == 1:
#    vin_chelik = random.randint(0, len_bs - 1)
#    cel_num = 0
#    for i in js["users"]:
#        if vin_chelik == cel_num:
#            vhil = js["users"][i]["name"]
#            print("+"+vhil)
#        cel_num += 1

if on_rozogrash == 1:
    vin_chel = random.randint(0, len_bs-1)
    cel_num = 0
    for i in js["users"]:
        if vin_chel == cel_num:
            js["users"][i]["coins"] += 100000
            vhi = js["users"][i]["name"]
            sohr_on()
            print("+"+vhi)
        cel_num += 1

if on_dolg == 1:
    for i in js["users"]:
        for g in js["users"][i]:
            if g == 'dolg':
                js["users"][i]["coins"] -= js["users"][i]["dolg"]
                js["users"][i]["dolg"] = 0
    sohr_on()


@bot.event
async def on_ready():
    global daily_a, vhi, d_bosin, js
    print('Бот запущен!')
    if daily_a == 1:
        for guild in bot.guilds:
            await guild.text_channels[0].send("!daily доступен")
    #if on_rozogrash == 1:
    #    for guild in bot.guilds:
    #        await guild.text_channels[0].send("Выйграл в розыгрыше:"+str(vhi))
    #if d_bosin == 1:
    #    for guild in bot.guilds:
    #        await guild.text_channels[0].send("Выйграл в дополнительном розыгрыше:"+str(vhil)+". Он выйграл StatTrak™ M4A4 | Полимерный рожок")
    #if d_bosin == 1:
    #    for i in js["users"]:
    #        if js["users"][i]["status"] == "admin":
    #            js["users"][i]["dbon"] = 1
    #    sohr_on()
@bot.event
async def on_message(message):
    global js, len_bs
    if message.author == bot.user:  # игнорируем сообщения от бота
        return
    #for word in bad_words:
    #    if word in message.content.lower():  # проверяем, содержит ли сообщение плохое слово
    #        await message.delete()  # удаляем сообщение
    #        await message.author.add_roles(discord.utils.get(message.guild.roles, name='Muted'))  # мьютим пользователя
    #        banes = js["users"][str(message.author.id)]["bans"]
    #        if banes == 2:
    #            await message.channel.send(f'{message.author.mention}, не используйте такие выражения! Ты получил мут на 5 минут.')
    #            js["users"][str(message.author.id)]["bans"] = 0
    #            sohr_on()
    #            await asyncio.sleep(300)
    #            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
    #        else:
    #            js["users"][str(message.author.id)]["bans"] += 1
    #            await message.channel.send(f'{message.author.mention}, не используйте такие выражения! Ты получил мут на 1у минуту.')
    #            await asyncio.sleep(60)
    #            await message.author.remove_roles(discord.utils.get(message.guild.roles, name='Muted'))
    #            sohr_on()
    #        history(message, message.author.mention)

    for word in cs_words:
        if word in message.content.lower():
            n = random.randint(1, 6)
            if n == 1:
                await message.channel.send('я пойду сейвить авик)')
            if n == 2:
                await message.channel.send('можно с вами в кс?]')
            if n == 3:
                await message.channel.send('ставлю пачку на миду')
            if n == 4:
                await message.channel.send('подождите Диму')
            if n == 5:
                await message.channel.send('Кидаю хаешку! Сорри, что попал в вас)')
            if n == 6:
                await message.channel.send('Кидаю смок и молик')
    users = {'дима': 'MrPofickt#5819',
             'саня': 'Tikvachka#5851, lebedev32#7464',
             'ваня': 'Кит#2469, 维拉斯德#9712',
             'лёша': 'Lobster(Alexu#2885)',
             'лёх': 'Lobster(Alexu#2885)',
             'леша': 'Lobster(Alexu#2885)',
             'лех': 'Lobster(Alexu#2885)',
             "егор": 'admin Murovei_31#5078',
             "матвей": 'OGYRETS#9296',
             "максим": 'Mikpl#8081',
             "макс ": 'Mikpl#8081',
             "леня": 'Nosorogg#1505',
             "лёня": 'Nosorogg#1505',
             "лёнь": 'Nosorogg#1505',
             "геор": "ᏦᏆᏞᏞ_ ՏͲᎪᎡ_#5590",
             "гоша": "ᏦᏆᏞᏞ_ ՏͲᎪᎡ_#5590",
             "гошу": "ᏦᏆᏞᏞ_ ՏͲᎪᎡ_#5590"
             }
    #for user, name in users.items():
    #    if user in message.content.lower():
    #        await message.channel.send(f'{user} = {name}')

    if message.content.startswith('!tackvachka'):
        await message.channel.send('Возможности: банить, мьютить, писать что-то про кс, мьютить за плохие слова и удалять сообщения.')

    if 'тыква' in message.content.lower() or 'тыкву' in message.content.lower():
        n = random.randint(1, 6)
        if n == 1:
            await message.channel.send('что нужно?')
        if n == 2:
            await message.channel.send('да, что надо?')
        if n ==3:
            await message.channel.send('приветик')
        if n == 4:
            await message.channel.send('я тут...')
        if n == 5:
            await message.channel.send('?')
        if n == 6:
            await message.channel.send('аюшки')


    for ids in js['users']:
        if message.author.id == ids:
            break
    else:
        app = {
            'id': message.author.id,
            'name': message.author.name,
            'status': 'user',
            'bans': 0,
            'id_bas': len_bs,
            'daily': 1,
            'coins': 10000
        }
        #js['users'] = set(js['users'])
        #js['users'] = list(set(js['users']))
        if str(message.author.id) in js['users']:
            pass
        else:
            js['users'][message.author.id] = app
        sohr_on()
        len_bs += 1

    print(message.content)

    await bot.process_commands(message)




@bot.command()
async def timeout(ctx, member: discord.Member, duration: int):
    print('+')
    if ctx.author.guild_permissions.administrator:
        role = discord.utils.get(ctx.guild.roles, name='Muted')
        await member.add_roles(role)
        await ctx.send(f'{member.mention} получил тайм-аут на {duration} минут(ы).')
        await asyncio.sleep(duration * 60)
        await member.remove_roles(role)
        await ctx.send(f'{member.mention} тайм-аут закончился.')
    else:
        await ctx.send('У вас нет прав на использование этой команды.')
@bot.command()
async def casino(ctx, stavka: int, coef: float):
    global js
    d = stavka*coef
    ds = d-stavka
    coins = js["users"][str(ctx.author.id)]["coins"]
    if coins >= stavka:
        vin = int(100/coef)
        if coef < 1:
            await ctx.send('Шанс выигрыша:'+str(vin)+'%'+"👶")
        elif coef >= 1 and coef <= 3:
            await ctx.send('Шанс выигрыша:' + str(vin) + '%' + "😀")
        elif coef > 3 and coef <= 10:
            await ctx.send('Шанс выигрыша:' + str(vin) + '%' + "😎")
        elif coef > 10 and coef <= 50:
            await ctx.send('Шанс выигрыша:' + str(vin) + '%' + "🥵")
        elif coef > 50 and coef <= 100:
            await ctx.send('Шанс выигрыша:' + str(vin) + '%' + "😈")
        else:
            await ctx.send('Шанс выигрыша:' + str(vin) + '%' + "😅")
        if coins > 1000000:
            a = random.randint(30, 101)
        if coins < 100000:
            a = random.randint(0, 75)
        else:
            a = random.randint(0, 90)
        print(a)
        await asyncio.sleep(1)
        if a <= vin:
            await ctx.send('Ты выйграл!'+'Сумма выигрыша:'+str(d))
            coins += ds
            js["users"][str(ctx.author.id)]["coins"] = coins
            sohr_on()
        else:
            await ctx.send('Ты проиграл 😥')
            coins -= stavka
            js["users"][str(ctx.author.id)]["coins"] = coins
            sohr_on()
    else:
        await ctx.send('нет денег)')

@bot.command()
async def balance(ctx):
    coins = js["users"][str(ctx.author.id)]["coins"]
    await ctx.send('ваш баланс:'+str(coins)+"койнов")


#@bot.command()
#async def help_cas(ctx):
#    await ctx.send('!help_cas - выдаёт список команд для казино; !balance - показывает ваш баланс; !casino - команда для казино, после которой идут 2 натуральных значения: сумма ставки, коэффициент ставки, пример, !casino 500 2 означает то, что вы играете в казино и ставите ставку в 500 койнов, коэффициент равен 2(шанс выигрыша 50%); !swop @пользователь кол.койнов - передаёт деньги @пользователю.')
@bot.command()
async def swop(ctx, member: discord.Member, money: int):
    global js
    coins = js["users"][str(ctx.author.id)]["coins"]
    if money > coins:
        await ctx.send('у вас нет столько денег для передачи!')
    else:
        js["users"][str(ctx.author.id)]["coins"] -= money
        js["users"][str(member.id)]["coins"] += money
        sohr_on()
        await ctx.send(str(ctx.author.mention)+" передал деньги "+str(member.mention))

@bot.command()
async def slots(ctx, stavka: int):
    global js, smiles, win_slots, cl
    user = bot.get_user(ctx.author.id)
    win = False
    coins = js["users"][str(ctx.author.id)]["coins"]
    if stavka > coins:
        await ctx.send('у вас нет денег!')
    else:
        if coins > 1000000 and coins < 1500000:
            a = smiles[random.randint(0, 6)]
            b = smiles[random.randint(0, 6)]
            c = smiles[random.randint(0, 6)]
        elif coins > 800000 and coins < 1000000:
            a = smiles[random.randint(0, 6)]
            b = smiles[random.randint(0, 6)]
            c = smiles[random.randint(0, 6)]
        elif coins > 500000 and coins < 800000:
            a = smiles[random.randint(0, 5)]
            b = smiles[random.randint(0, 5)]
            c = smiles[random.randint(0, 5)]

        elif coins > 200000 and coins < 500000:
            a = smiles[random.randint(0, 5)]
            b = smiles[random.randint(0, 5)]
            c = smiles[random.randint(0, 5)]
        elif coins < 50000 and coins > 10000:
            a = smiles[random.randint(0, 4)]
            b = smiles[random.randint(0, 4)]
            c = smiles[random.randint(0, 4)]
        elif coins <= 10000:
            a = smiles[random.randint(0, 3)]
            b = smiles[random.randint(0, 3)]
            c = smiles[random.randint(0, 3)]
        elif coins >= 1500000 and coins < 2000000:
            a = smiles[random.randint(0, 7)]
            b = smiles[random.randint(0, 7)]
            c = smiles[random.randint(0, 7)]
        elif coins >= 2000000 and coins < 3000000:
            a = smiles[random.randint(0, 7)]
            b = smiles[random.randint(0, 7)]
            c = smiles[random.randint(0, 7)]
        elif coins >= 3000000:
            a = smiles[random.randint(0, 11)]
            b = smiles[random.randint(0, 11)]
            c = smiles[random.randint(0, 11)]
        else:
            a = smiles[random.randint(0, 4)]
            b = smiles[random.randint(0, 4)]
            c = smiles[random.randint(0, 4)]
        d  = a+b+c
        await ctx.send('ваши слоты:'+a+b+c)
        for i in win_slots:
            if i == d:
                await ctx.send('вы выйграли:'+str(win_slots[i]*stavka)+"😎")
                print("win = "+str(win_slots[i]*stavka))
                coins += win_slots[i]*stavka-stavka

                js["users"][str(ctx.author.id)]["coins"] = coins
                with open('data.json', 'w') as fr:
                    json.dump(js, fr, indent=4)
                time.sleep(0.1)
                with open('data.json', 'r') as fr:
                    js = json.load(fr)
                win = True
        if win == False:
            await ctx.send('вы ничего не выйграли 😣')
            js["users"][str(ctx.author.id)]["coins"] -= stavka
            with open('data.json', 'w') as fr:
                json.dump(js, fr, indent=4)
            time.sleep(0.1)
            with open('data.json', 'r') as fr:
                js = json.load(fr)

@bot.command()
async def help_slots(ctx):
    await ctx.send("'🎱🎱🎱': 50x,\n '♥♥♥': 75x,\n '♠♠♠': 75x,\n '💰💰💰':100x,\n'😈😈😈': 110,\n'😎😎😎': 120,\n'🤑🤑🤑': 130,\n'👹👹👹': 140,\n'☠☠☠': 150,\n'👻👻👻': 160,\n'🥶🥶🥶':170,\n'👽👽👽': 180,\n'🧠🧠🧠': 190,\n '777': 200x ")

@bot.command()
async def ruletka(ctx, stavka: int, c: int):
    global js
    win_sod = 0
    win_c = random.randint(0, 36)

    if c == win_c:
        if c == 0:
            win_sod = stavka*36
            await ctx.send("Ты выйграл x100!"+str(win_sod)+' выйгрыш!')
            js["users"][str(ctx.author.id)]["coins"] += win_sod
            sohr_on()
        if c%2 == 0:
            win_sod = stavka*36
            await ctx.send("Ты выйграл x36 красная!"+str(win_sod))
            js["users"][str(ctx.author.id)]["coins"] += win_sod
            sohr_on()
        if c % 2 != 0:
            win_sod = stavka*36
            await ctx.send("Ты выйграл x36 чёрная!"+str(win_sod))
            js["users"][str(ctx.author.id)]["coins"] += win_sod
            sohr_on()
    else:
        await ctx.send("Ты проиграл!")
        js["users"][str(ctx.author.id)]["coins"] -= stavka
        sohr_on()

@bot.command()
async def daily(ctx):
    global js
    if js["users"][str(ctx.author.id)]["daily"] == 1:
        a = random.randint(500, 5000)
        js["users"][str(ctx.author.id)]["coins"] += a
        js["users"][str(ctx.author.id)]["daily"] = 0
        await ctx.send("Вы получили бонус:"+str(a))
        sohr_on()
    else:
        await ctx.send("Вы уже израсходовали бонус!")

@bot.command()
async def top(ctx):
    global js
    a = {}
    for i in js["users"]:
        b = js["users"][i]["name"]
        a[b] = js["users"][i]["coins"]
    sortedes = dict(sorted(a.items(), key=lambda item: item[1]))
    sortedes_1_ = list(sortedes)[-1]
    for i in a:
        if i == sortedes_1_:
            top = a[i]
    sortedes_2_ = list(sortedes)[-2]
    for i in a:
        if i == sortedes_2_:
            sec = a[i]
    sortedes_3_ = list(sortedes)[-3]
    for i in a:
        if i == sortedes_3_:
            tree = a[i]
    await ctx.send("топ1:" + str(sortedes_1_)+" - "+str(top)+'койнов'+'🤩')
    await ctx.send("топ2:" + str(sortedes_2_)+" - "+str(sec)+'койнов'+'🥰')
    await ctx.send("топ3:" + str(sortedes_3_)+" - "+str(tree)+'койнов'+'🤯')



@bot.command()
async def pwp(ctx, member: discord.Member, stavka: int):
    global pwp_player, js, stavka_pwp
    if js["users"][str(ctx.author.id)]["coins"] >= stavka:
        pwp_player[str(ctx.author.id)] = member.id
        await ctx.send(str(ctx.author.mention)+" пригласил "+str(member.mention)+". "+str(member.mention)+" напиши команду !go для начала pwp")
        stavka_pwp[str(ctx.author.id)] = stavka
    else:
        await ctx.send("у вас нет денег для ставки")


@bot.command()
async def go(ctx):
    global js, pwp_player, stavka_pwp
    for id in pwp_player:
        ids = pwp_player.get(id)
        if str(ids) == str(ctx.author.id):
            g = random.randint(0, 1)
            coins = stavka_pwp[str(id)]
            if coins <= js["users"][id]["coins"]:
                if g == 0:
                    await ctx.send("Выйграл "+str(ctx.author.mention))
                    js["users"][id]["coins"] -= coins
                    js["users"][str(ctx.author.id)]["coins"] += coins
                else:
                    print(5)
                    await ctx.send("Выйграл " + str(js["users"][id]["name"]))
                    js["users"][id]["coins"] += coins
                    js["users"][str(ctx.author.id)]["coins"] -= coins
            else:
                await ctx.send("У вас нет денег,"+str(ctx.author.mention))
@bot.command()
async def test(ctx):
    print(ctx)

@bot.command()
async def daily_admin(ctx):
    if str(ctx.author.id) == '676857729519845403' or js["users"][str(ctx.author.id)]["dbon"] == 1:
        js["users"][str(ctx.author.id)]["coins"] += 10000
        js["users"][str(ctx.author.id)]["dbon"] = 0
        await ctx.send(str(ctx.author.mention)+" получил бонус")
    else:
        await ctx.send("ты не админ или уже израсходовал бонус")

#@bot.command()
#async def sendicate(ctx):
#    message = "Всем привет, кланы пришли! Каждый клан получает койн клана, когда его участник пишет команду !slots. Койн клана = 100 койнам!"
#    await ctx.send(message)
#    if ctx.author.guild_permissions.administrator:
#        for guild in bot.guilds:
#            await guild.text_channels[0].send(message)

@bot.command()
async def clans(ctx):
    global cl
    a = []
    for i in cl["clans"]:
        a.append(i)
    await ctx.send(a)

@bot.command()
async def clans_info(ctx, clan: str):
    global cl
    for i in cl["clans"]:
        if i == clan:
            await ctx.send(cl["clans"][i])
            return
    await ctx.send("нет информации о клане")

@bot.command()
async def clan_creat(ctx, clan_n: str):
    global cl, js
    if js["users"][str(ctx.author.id)]["coins"] >= 1500000:
        for i in cl["clans"]:
            if i == clan_n:
                await ctx.send("клан с таким именем есть")
                print(3)
                return
        cl["clans"][clan_n] = {
            "name": clan_n,
            "id": len(cl["clans"])+1,
            "coins-clan": 10000,
            "users": {"chapter": js["users"][str(ctx.author.id)]["name"]},
            "chapter": js["users"][str(ctx.author.id)]["name"],
            "win": 0
        }
        js["users"][str(ctx.author.id)]["coins"] -= 1500000
        sohr_on()
        clans_sohr()
    else:
        print(6)
        await ctx.send("у вас нет 1500000 койнов для создания клана")

@bot.command()
async def inclanadd(ctx, clan_n: str, member: discord.Member):
    global js, cl, toaddclans
    for i in cl["clans"]:
        if i == clan_n:
            if js["users"][str(ctx.author.id)]["name"] == cl["clans"][clan_n]["chapter"]:
                toaddclans[member.id] = clan_n
                await ctx.send("заявка отправлена, что бы принять, нужно чтобы "+member.name+" написал !inclan "+clan_n)
                return
            else:
                await ctx.send("вы не глава клана "+clan_n)
                return
    await ctx.send("нет клана "+clan_n)

@bot.command()
async def inclan(ctx, clan_n: str):
    global cl, js, toaddclans
    for id in toaddclans:
        if id == ctx.author.id:
            if toaddclans.get(id) ==clan_n:
                user = bot.get_user(ctx.author.id)
                username = user.name
                cl["clans"][clan_n]["users"][username] = username
                await ctx.send(str(username) + ' добавлен в клан ' + clan_n)
                sohr_on()
                clans_sohr()
                return
    await ctx.send("ошибка")


@bot.command()
async def expelclan(ctx, clan_n: str, member: discord.Member):
    global cl, js
    if js["users"][str(ctx.author.id)]["name"] == cl["clans"][clan_n]["chapter"]:
        for memb in cl["clans"][clan_n]["users"]:
            if memb == member.name:
                del cl["clans"][clan_n]["users"][memb]
                clans_sohr()
                await ctx.send("участник выгнан из клана")
                return
        await ctx.send("участник не найден")
    else:
        await ctx.send("вы не глава клана")




@bot.command()
async def war_clan(ctx, clan_n: str, clan_n_p: str, stavka: int):
    global pwp_clans, cl, stavka_clans, js
    print(1)
    if cl["clans"][clan_n]["coins-clan"] >= stavka:
        print(2)
        if js["users"][str(ctx.author.id)]["name"] == cl["clans"][clan_n]["chapter"]:
            print(3)
            pwp_clans[clan_n] = clan_n_p
            await ctx.send(str(ctx.author.mention) + " пригласил клан " + clan_n_p + ". " + cl["clans"][clan_n_p]["chapter"] + " напиши команду !gopwpclans "+clan_n+" для начала pwp")
            stavka_clans[clan_n] = stavka
            return
        else:
            await ctx.send("ты не глава клана")
    else:
        await ctx.send("у клана нет денег для ставки")

@bot.command()
async def gopwpclans(ctx, clan_n: str):
    global pwp_clans, cl, stavka_clans
    print(1)
    for id in pwp_clans:
        print(2)
        if id == clan_n:
            print(3)
            stavka = stavka_clans.get(id)
            clan_aut = pwp_clans.get(id)
            if js["users"][str(ctx.author.id)]["name"] == cl["clans"][clan_aut]["chapter"]:
                print(4)
                if cl["clans"][clan_aut]["coins-clan"] >= stavka:
                    print(5)
                    g = random.randint(0, 1)
                    if g == 0:
                        await ctx.send("выйграл клан " + clan_aut)
                        cl["clans"][clan_aut]["coins-clan"] += stavka
                        cl["clans"][id]["coins-clan"] -= stavka
                    else:
                        await ctx.send("выйграл клан " + id)
                        cl["clans"][clan_aut]["coins-clan"] -= stavka
                        cl["clans"][id]["coins-clan"] += stavka
                    clans_sohr()
                    return
                else:
                    ctx.send("у клана нет койнов для войны")
                    return
            else:
                ctx.send("вы не глава клана")
                return
    ctx.send("неверно указан клан, или клан не вызывал вас на поединок")

@bot.command()
async def top_clan(ctx):
    global cl
    top_clcoins = 0
    topcl = ''
    for id in cl["clans"]:
        print(id)
        print(cl["clans"][id]["coins-clan"])
        if cl["clans"][id]["coins-clan"] > top_clcoins:
            top_clcoins = cl["clans"][id]["coins-clan"]
            topcl = cl["clans"][id]["name"]
    await ctx.send("топ1 клан:"+str(topcl))



@bot.command()
async def cointocoinclan(ctx, clan_n: str, stavka: int):
    global js, cl
    if stavka <= js["users"][str(ctx.author.id)]["coins"]:
        js["users"][str(ctx.author.id)]["coins"] -= stavka
        cl["clans"][clan_n]["coins-clan"] += stavka/100
        await ctx.send("вы перевели клану "+str(stavka/100)+" койнов клана")
    else:
        await ctx.send("нет денег")
    sohr_on()
    clans_sohr()

@bot.command()
async def clancoinstocoins(ctx, clan_n: str, stavka: int):
    if js["users"][str(ctx.author.id)]["name"] == cl["clans"][clan_n]["chapter"]:
        if cl["clans"][clan_n]["coins-clan"] >= stavka:
            cl["clans"][clan_n]["coins-clan"] -= stavka
            js["users"][str(ctx.author.id)]["coins"] += stavka*100
            await ctx.send("вы взяли из клана "+str(stavka*100)+"койнов")
            return
        else:
            await ctx.send("нет у клана столько койнов")
            return
    else:
        await ctx.send("вы не глава")

    sohr_on()
    clans_sohr()

@bot.command()
async def dolg(ctx, moneys: int):
    global js
    if moneys >51000:
        await ctx.send("большая сумма для долга")
        return
    for i in js["users"][str(ctx.author.id)]:
        if i == 'dolg':
            if js["users"][str(ctx.author.id)]["dolg"] > 0:
                await ctx.send("у вас уже есть долг")
                return
            js["users"][str(ctx.author.id)]["dolg"] += moneys
            js["users"][str(ctx.author.id)]["coins"] += moneys
            await ctx.send("ты взял в ДОЛГ")
            sohr_on()
            return
    js["users"][str(ctx.author.id)]["dolg"] = 0
    js["users"][str(ctx.author.id)]["dolg"] += moneys
    js["users"][str(ctx.author.id)]["coins"] += moneys
    sohr_on()
    await ctx.send("ты взял в ДОЛГ")

bot.run('ТОКЕН')