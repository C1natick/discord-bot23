import discord
from discord import app_commands
import os

TOKEN = os.environ.get("DISCORD_BOT_TOKEN")
ROLE_NAME = "🌱 Новичок"

intents = discord.Intents.default()
intents.members = True
intents.guilds = True

client = discord.Client(intents=intents)
tree = app_commands.CommandTree(client)


@client.event
async def on_ready():
    await tree.sync()
    print(f"Бот запущен: {client.user}")
    for guild in client.guilds:
        print(f"Подключён к серверу: {guild.name} (ID: {guild.id})")
        roles = [r.name for r in guild.roles]
        print(f"Роли на сервере: {roles}")
        target = discord.utils.get(guild.roles, name=ROLE_NAME)
        if target:
            print(f"Роль '{ROLE_NAME}' найдена!")
        else:
            print(f"[ОШИБКА] Роль '{ROLE_NAME}' НЕ найдена! Проверьте точное название роли выше.")


@client.event
async def on_member_join(member):
    print(f"Новый участник зашёл: {member.name}")
    guild = member.guild
    role = discord.utils.get(guild.roles, name=ROLE_NAME)

    if role is None:
        print(f"[ОШИБКА] Роль '{ROLE_NAME}' не найдена на сервере '{guild.name}'")
        return

    try:
        await member.add_roles(role)
        print(f"Роль '{ROLE_NAME}' выдана: {member.name}")
    except discord.Forbidden:
        print(f"[ОШИБКА] Нет прав выдавать роль '{ROLE_NAME}'. Убедитесь, что роль бота выше в иерархии.")
    except Exception as e:
        print(f"[ОШИБКА] {e}")


@tree.command(name="ban", description="Забанить участника сервера")
@app_commands.describe(member="Участник которого нужно забанить", reason="Причина бана")
@app_commands.checks.has_permissions(ban_members=True)
async def ban(interaction: discord.Interaction, member: discord.Member, reason: str = "Причина не указана"):
    if member == interaction.user:
        await interaction.response.send_message("Нельзя забанить самого себя!", ephemeral=True)
        return

    if member.top_role >= interaction.user.top_role:
        await interaction.response.send_message("Вы не можете забанить участника с такой же или более высокой ролью.", ephemeral=True)
        return

    try:
        await member.ban(reason=f"{reason} (забанил: {interaction.user})")
        await interaction.response.send_message(f"🔨 **{member.name}** забанен. Причина: {reason}")
        print(f"Забанен: {member.name} | Причина: {reason} | Кем: {interaction.user}")
    except discord.Forbidden:
        await interaction.response.send_message("У бота нет прав для бана. Убедитесь, что роль бота выше в иерархии.", ephemeral=True)
    except Exception as e:
        await interaction.response.send_message(f"Ошибка: {e}", ephemeral=True)


@ban.error
async def ban_error(interaction: discord.Interaction, error: app_commands.AppCommandError):
    if isinstance(error, app_commands.MissingPermissions):
        await interaction.response.send_message("У вас нет прав для бана участников.", ephemeral=True)


if not TOKEN:
    print("[ОШИБКА] Переменная DISCORD_BOT_TOKEN не задана!")
else:
    client.run(TOKEN)
