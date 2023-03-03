import subprocess
try:
    import discord
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "discord"])
    import discord
import asyncio
from bot_functions import MESSAGE, BLACKLIST_FILE_PATH, check_and_send, check_blacklist_file, get_channel_id
import os

# Skapa en Discord-klient med standardavsikt
client = discord.Client(intents=discord.Intents.default())

async def run_scrapetube_script():
    print("Startar scrapetube...")
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "scrapetube_script.py"))
    process = subprocess.Popen(["python", script_path])
    process.wait()
    print("Avslutar scrapetube...")

async def send_message():
    # Hämta Discord-kanalens ID från channel_ids.txt-filen baserat på YouTube-kanalnamnet
    channel_name = "my_channel_name"  # Byt ut detta mot det faktiska kanalnamnet
    youtube_channel_name = channel_name.replace("_", " ")
    discord_channel_id = get_channel_id(youtube_channel_name)

    # Hitta kanalen med hjälp av dess ID
    channel = client.get_channel(discord_channel_id)

    # Skicka meddelandet från bot_functions
    await channel.send(MESSAGE)

async def my_background_task():
    check_blacklist_file()
    while True:
        print("Kör loopen...")
        # här under ska skriptet scrapetube_script.py starta
        await run_scrapetube_script()
        # ovanför den här raden ska scrapetube_script.py avslutas
        await check_and_send(client)
        await asyncio.sleep(60)

# Kör när klienten har anslutit
@client.event
async def on_ready():
    print('Boten har anslutit till Discord!')
    # Starta vår bakgrundsuppgift
    client.loop.create_task(my_background_task())

# Kör Discord-klienten med rätt token
client.run('YOUR_DISCORD_BOT_TOKEN_HERE')