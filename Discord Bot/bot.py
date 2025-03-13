import discord
from discord.ext import commands
from database import get_db_connection

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f'Logged in as Bot {bot.user}.')

@bot.command()
async def add_task(ctx, *, description):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("INSERT INTO tasks (description, completed) VALUES (?, ?)", (description, 0))
    conn.commit()
    conn.close()
    await ctx.send(f'Task added! To list all tasks use !show_tasks')

@bot.command()
async def delete_task(ctx, task_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'Task {task_id} deleted.')

@bot.command()
async def show_tasks(ctx):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("SELECT * FROM tasks")
    tasks = c.fetchall()
    conn.close()
    if tasks:
        task_list = "\n".join([f"{task['id']}: {task['description']} (Completed: {'✅' if task['completed'] else '❌'})" for task in tasks])
        await ctx.send(f"Here is the list of tasks.\n{task_list}")
    else:
        await ctx.send("You have no tasks.")

@bot.command()
async def complete_task(ctx, task_id: int):
    conn = get_db_connection()
    c = conn.cursor()
    c.execute("UPDATE tasks SET completed = 1 WHERE id = ?", (task_id,))
    conn.commit()
    conn.close()
    await ctx.send(f'Task {task_id} marked as completed.')

bot.run('YOUR_DISCORD_BOT_TOKEN')