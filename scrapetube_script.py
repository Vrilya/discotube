import subprocess
import sys
import os
try:
    import scrapetube
except ImportError:
    subprocess.check_call([sys.executable, "-m", "pip", "install", "scrapetube"])
    import scrapetube
from datetime import datetime

# Sätt sökvägen till textfilen med kanaladresser och namn
channel_ids_file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), "channel_ids.txt"))


# Radera alla .txt filer i mappen (förutom channel_ids.txt och blacklist.txt)
for file_name in os.listdir(os.path.abspath(os.path.dirname(__file__))):

    if file_name.endswith(".txt") and file_name != "channel_ids.txt" and file_name != "blacklist.txt":
        os.remove(os.path.join(os.path.dirname(__file__), file_name))

# Läs in kanaladresser och namn från filen
channels = {}
with open(channel_ids_file_path, "r") as file:
    for line in file:
        channel_id, numbercode, name = line.strip().split(",", maxsplit=2)
        channels[name] = channel_id

# Iterera över kanalerna och hämta videor från varje kanal
for name, channel in channels.items():
    file_path = os.path.abspath(os.path.join(os.path.dirname(__file__), f"{name}.txt"))

    
    # Kontrollera om filen redan finns
    if os.path.exists(file_path):
        # Läs in alla befintliga video-ID från filen
        with open(file_path, "r") as file:
            existing_ids = set(line.strip() for line in file)
    else:
        existing_ids = set()

    videos = scrapetube.get_channel(channel, limit=2, sort_by='newest')

    # Öppna en fil i läge för att skriva och spara referensen till filen i en variabel
    with open(file_path, "a") as file:
        for video in videos:
            video_id = video['videoId']
            if video_id not in existing_ids:
                # Skriv ner video id i filen
                file.write(video_id + "\n")
                # Lägg till video id i uppsättningen av befintliga id
                existing_ids.add(video_id)
                # Skriv ut den nya video-ID:t i terminalen tillsammans med datum och tid
                now = datetime.now()
                dt_string = now.strftime("%Y-%m-%d %H:%M:%S")
                print(f"\u200B\n[New video posted by {name} at {dt_string}]\u200B\n https://youtu.be/{video_id}")
