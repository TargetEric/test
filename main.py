from pyrogram import Client, filters
from datetime import datetime, timedelta
import config
app = Client(
    "delbot",
    config.API_ID,
    config.API_HASH,
    bot_token=config.BOT_TOKEN,
)
time_limit = 2
@app.on_edited_message()
async def delete_edits(client, msg):
    if datetime.now() - msg.date > timedelta(minutes=time_limit):
        await msg.delete()
        print(f"Deleted edited message from {msg.from_user.username}")
    else:
        print("Edit within 2 minutes; no action taken.")
if __name__ == '__main__':
    app.run()
    app.run_until_disconnected()
