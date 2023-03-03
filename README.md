# Discotube

Discotube is a Python program that scrapes YouTube channels for new videos and sends notifications to Discord channels. It can be used to keep track of new video uploads from your favorite YouTube channels in real-time.

## Installation

1. Clone the repository to your local machine.
2. Make sure you have Python 3.6 or later installed on your system.
3. Create a new Discord bot by going to the [Discord Developer Portal](https://discord.com/developers/applications) and clicking on "New Application". Give your bot a name and click "Create".
4. Once you've created your application, click on "Bot" in the left-hand menu, then click "Add Bot". This will create a bot user for your application.
5. Click on the "Copy" button under "Token" to copy your bot's API token.
6. Edit the `discotube.py` file and replace `'YOUR_DISCORD_BOT_TOKEN_HERE'` with your Discord bot's API token.

## Usage

1. Open a terminal window in the directory where you cloned the repository.
2. Start the program by running the following command:

python discotube.py
3. The program will start scraping the specified YouTube channels and sending notifications to the associated Discord channels.
4. You can customize the YouTube channels and Discord channels by editing the `channel_ids.txt` file.
- Each line in the `channel_ids.txt` file corresponds to a YouTube channel and its associated Discord channel. The format of each line is as follows:
  ```
  <youtube_channel_id>,<discord_channel_id>,<youtube_channel_name>
  ```
- `youtube_channel_id` is the ID of the YouTube channel to be monitored. You can obtain this ID by going to the YouTube channel's page and looking at the URL. The ID is the string of letters and numbers after "channel/" in the URL.
- `discord_channel_id` is the ID of the Discord channel where notifications should be sent.
- `youtube_channel_name` is a human-readable name for the YouTube channel, which is used in the notification message.
## Contact

If you have any questions or need help getting set up, you can contact Vrilya on our Discord channel: [https://discord.gg/nRYSSkfbHD](https://discord.gg/nRYSSkfbHD).

