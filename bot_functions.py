import os
from datetime import datetime

# Meddelande som ska skickas till Discord-kanalen
MESSAGE = "Ingen ny rad hittades i någon .txt fil."

# Absolut sökväg till vår blacklist.txt-fil
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
BLACKLIST_FILE_PATH = os.path.join(SCRIPT_DIR, "blacklist.txt")

# Funktion som returnerar innehållet i vår channel_ids.txt-fil som en lista av rader
def get_channel_ids():
    channel_ids_file_path = os.path.join(SCRIPT_DIR, "channel_ids.txt")
    with open(channel_ids_file_path, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

# Funktion som returnerar en Discord-kanals ID baserat på ett YouTube-kanalnamn
def get_channel_id(channel_name):
    channel_ids = get_channel_ids()
    for line in channel_ids:
        parts = line.split(",")
        if parts[2] == channel_name:
            return int(parts[1])

# Funktion som kontrollerar om en rad finns i vår blacklist.txt-fil
def is_blacklisted(line):
    blacklist = get_blacklist()
    return line in blacklist

# Funktion som returnerar innehållet i vår blacklist.txt-fil som en lista av rader
def get_blacklist():
    with open(BLACKLIST_FILE_PATH, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

# Funktion som lägger till en rad till vår blacklist.txt-fil
def add_to_blacklist(line):
    with open(BLACKLIST_FILE_PATH, 'a', encoding='utf-8') as f:
        f.write(line + "\n")

# Funktion som kontrollerar om en fil är en .txt fil
def is_text_file(filename):
    return filename.endswith(".txt") and filename != "channel_ids.txt" and filename != "blacklist.txt"

# Funktion som returnerar innehållet i en .txt fil som en lista av rader
def get_text_file_contents(filepath):
    absolute_filepath = os.path.abspath(filepath)
    with open(absolute_filepath, 'r', encoding='utf-8') as f:
        return f.read().splitlines()

# Funktion som skannar alla .txt filer i mappen och skickar varje rad till Discord-kanalen
async def check_and_send(client):
    text_files = [filename for filename in os.listdir(SCRIPT_DIR) if is_text_file(filename)]

    for filename in text_files:
        channel_name = filename[:-4]
        channel_id = get_channel_id(channel_name)
        contents = get_text_file_contents(os.path.join(SCRIPT_DIR, filename))
        for line in contents:
            if not is_blacklisted(line):
                # Skapa datum- och tidssträng i formatet YYYY-MM-DD HH:MM:SS
                now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

                # Skicka meddelande till Discord-kanalen med datum- och tidsinformation
                channel = client.get_channel(channel_id)
                await channel.send(f"\u200B\n[{now}]\n{channel_name} has posted a new video:\u200B\nhttps://youtu.be/{line}")

                # Lägg till raden i blacklist.txt
                add_to_blacklist(line)

# Funktion som kontrollerar om blacklist.txt-filen finns eller inte och skapar den om den inte finns
def check_blacklist_file():
    if not os.path.exists(BLACKLIST_FILE_PATH):
        # Skapa en ny blacklist.txt-fil och fyll den med information från alla .txt-filer
        with open(BLACKLIST_FILE_PATH, 'w', encoding='utf-8') as f:
            for filename in os.listdir(SCRIPT_DIR):
                if is_text_file(filename):
                    contents = get_text_file_contents(os.path.join(SCRIPT_DIR, filename))
                    for line in contents:
                        f.write(line + "\n")