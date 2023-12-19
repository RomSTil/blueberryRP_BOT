import asyncio
import disnake
from disnake.ext import commands
from disnake import TextInputStyle
from disnake.ui import Button, View

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    channel = bot.get_channel(1171766578581356647)
    await channel.send("бот работает!")
    print("все работает!")

# Subclassing the modal.
class MyModal(disnake.ui.Modal):
    def __init__(self):
        # The details of the modal, and its components
        components = [
            disnake.ui.TextInput(
                label="Игровой никнейм",
                placeholder="RomSTil",
                custom_id="Игровой никнейм",
                style=TextInputStyle.short,
                max_length=50,
            ),
            disnake.ui.TextInput(
                label="Дискорд никнейм",
                placeholder="Romstil",
                custom_id="Дискорд никнейм",
                style=TextInputStyle.short,
            ),
            disnake.ui.TextInput(
                label="версия игры. Джава Бедрок",
                placeholder="джава бедрок",
                custom_id="версия игры",
                style=TextInputStyle.short,
            ),
        ]
        super().__init__(title="У вас вылезет ошибка но это визуальны баг^^", components=components)

    # The callback received when the user input is completed.
    async def callback(self, ctx: disnake.ModalInteraction):
        embed = disnake.Embed(title="Заявка")
        channel = bot.get_channel(1171058457839931442)
        for key, value in ctx.text_values.items():
            embed.add_field(
                name=key.capitalize(),
                value=value[:1024],
                inline=False,
            )
        await channel.send(embed=embed)

# The slash command that responds with a message.
@bot.slash_command()
async def buttons(inter: disnake.ApplicationCommandInteraction):
    channel = bot.get_channel(1181617569707339838)
    await channel.send(
        embed = disnake.Embed(
        title="Добро пожаловать на blueberryRP",
        description="Чтоб играть на нашем сервере вам стоит подать заявку ",
        colour=0x4F86F7,
        ),
        components=[
            disnake.ui.Button(label="Подать заявку", style=disnake.ButtonStyle.success, custom_id="yes"),
        ],
    )

@bot.slash_command(description="добавляет игрока в белый список")
# @commands.has_any_role(role)
@commands.has_guild_permissions(administrator=True)
async def easywl(ctx, member: disnake.Member, nik: str):
    await member.edit(nick=nik)
    channel = bot.get_channel(1171085821059813457)
    await channel.send(f"easywl add {nik}")
    member = member or ctx.message.author
    guild = bot.get_guild(1170489938597380146)
    role = guild.get_role(1170761992445886626)
    await member.add_roles(role)
    channel = bot.get_channel(1171503861685571634)
    await channel.send(
        embed=disnake.Embed(
            title="Уведомление",
            description=f"Пользователю {member.mention} одобрили заявку",
            colour=0x4F86F7,
        )
    )
    await ctx.send("Команда сработала")
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                                       #Выдача штрафов#                                                                                              #
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.slash_command(description="выдача штрафа")
@commands.has_guild_permissions(administrator=True)
async def penalty(ctx, игрок: disnake.Member, сумма_выплаты: int, причина: str, role: disnake.Role, пострадавший: disnake.Member, наказание: int):
    time_theft = 86400
    if наказание == 1:
        await ctx.send(f"{игрок.mention}")
        await ctx.send(
        embed=disnake.Embed(
            title="Уведомление",
            description=f"{игрок.mention} получает штраф в размера {сумма_выплаты} алмаза по причина: {причина}. верните вещи игроку {пострадавший.mention}У вас есть 5 дней для выплаты налога",
            colour=0x4F86F7,
            )
        )
        for i in range(5, -1, -1):
            print(f"до выплаты штрафа осталось {i} дней")
            await asyncio.sleep(time_theft)
            await ctx.send({игрок.mention})
            await ctx.send(
            embed=disnake.Embed(
                title="Уведомление",
                description=f"Напоминание игроку {игрок.mention}.до выплаты штрафа осталось {i} дней",
                colour=0x4F86F7,
                )
            )
        if i == 0:
            await ctx.send(f"ваше время вышло {игрок.mention} вы получаете {role.mention}!")
            await игрок.add_roles(role)
    elif наказание == 2:
        await ctx.send(f"{игрок.mention}")
        await ctx.send(
            embed=disnake.Embed(
                title="Уведомление",
                description=f"{игрок.mention} получает {role.mention}. Причина: {причина}.Играйте в свое удовольствие и больше не нарушайте правила!",
                colour=0x4F86F7,
                )
            )
        await игрок.add_roles(role)
        
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
#                                                                                                       #Организации#                                                                                                 #
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
@bot.slash_command(description="Сделать игрока частью клана")
@commands.has_role(1186343882724745287)
async def give_player_in_organisation(ctx, игрок: disnake.Member, role_organisation: disnake.guild.Role):
    
    await ctx.send(f"{игрок.mention}")
    await ctx.send(
        embed=disnake.Embed(
            title="Уведомление",
            description=f"Глава клана {role_organisation} добавили игрока {игрок}",
            colour=0x4F86F7,
            )
        )
    await игрок.add_roles(role_organisation)
    
bot.run("token")
