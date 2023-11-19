import asyncio
import sys

import disnake
from disnake.ext import commands


bot = commands.Bot(command_prefix="/")


@bot.event
async def on_ready():
    channel = bot.get_channel(1171766578581356647)
    await channel.send("бот работает!")
    print("все работает!")
# @bot.slash_command(description="добавляет игрока в белый список")
# async def easywl(inter, username: str):
#     await inter.response.send_message(f"easywl add {username}")

# @bot.slash_command()
# async def easywl(self, ctx,member: disnake.Member, nik:str):
#     await member.edit(nick=nik)
#     await ctx.send(f"easywl add {nik}")

@bot.slash_command(description="добавляет игрока в белый список")
@commands.has_guild_permissions(administrator=True)
async def easywl(self,ctx, member: disnake.Member, nik: str):
    await member.edit(nick=nik)
    await ctx.send(f"easywl add {nik}")
    member = member or ctx.message.author
    guild = bot.get_guild(1170489938597380146)
    role = guild.get_role(1170761992445886626)
    await member.add_roles(role)
    channel = bot.get_channel(1171503861685571634)
    await channel.send(f"Пользователю {member.mention} одобрили заявку")

# @bot.slash_command(description="")
# async def returned_the_debt(ctx, игрок: disnake.Member, пострадавший: disnake.Member):
#     await ctx.send(f"игрок {игрок.mention} вернул штраф игроку {пострадавший.mention}")
#     a = 1
#     if a == 1:
#         return
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                             #Выдача штрафов#
#--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.slash_command(description="выдача штрафа")
@commands.has_guild_permissions(administrator=True)
async def penalty(ctx, игрок: disnake.Member, сумма_выплаты: int,причина: str,role: disnake.Role,пострадавший: disnake.Member, punishment: int):
    time_theft = 86400
    if punishment == 1:
        await ctx.send(f"{игрок.mention} получает штраф в размера {сумма_выплаты} алмаза по причина: {причина}. верните вещи игроку {пострадавший.mention}У вас есть 5 дней для выплаты налога")
        for i in range(5, -1, -1):
            @bot.slash_command(description="")
            async def returned_the_debt(ctx, игрок: disnake.Member, пострадавший: disnake.Member):
                await ctx.send(f"игрок {игрок.mention} вернул штраф игроку {пострадавший.mention}")
                a = 1
                if a == 1:
                    return
            print(f"до выплаты штрафа осталось {i} дней")
            await asyncio.sleep(time_theft)
            await ctx.send(f"Напоминание игроку {игрок.mention}.до выплаты штрафа осталось {i} дней")
        if i == 0:
            await ctx.send(f"ваше время вышло {игрок.mention} вы получаете {role.mention}!")
            await игрок.add_roles(role)
    elif punishment == 2:
        await ctx.send(
            f"{игрок.mention} получает {role.mention}. Причина: {причина}.Играйте в свое удовольствие и больше не нарушайте правила!")
        await игрок.add_roles(role)
    






bot.run("token")
