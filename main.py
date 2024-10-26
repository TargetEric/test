from pyrogram import Client, filters
from pyrogram.enums import ChatMemberStatus
from datetime import datetime, timedelta
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
app = Client(
    "delbot",
    6131334,
    '9514b24d20d23c06bae8a5c2b60fa0c7',
    bot_token="7546434205:AAGN7aIVMB8VI63eU_udN6PMB7nLzyllluw",
)
timelimit = 2
authorizedusers = set()
async def isadmin(client, chat_id, user_id):
    member = await client.get_chat_member(chat_id, user_id)
    return member.status in [ChatMemberStatus.OWNER, ChatMemberStatus.ADMINISTRATOR]
@app.on_message(filters.command("start"))
async def startmessage(client, msg):
    bot_username = (await client.get_me()).username
    keyboard = InlineKeyboardMarkup([
        [
            InlineKeyboardButton(
                "Add Me To Your Group",
                url=f"https://t.me/{bot_username}?startgroup=s&admin=delete_messages+invite_users"
            )
        ],
        [
            InlineKeyboardButton("Updates", url="https://t.me/Ak4ssh"),
            InlineKeyboardButton("Support", url="https://t.me/Ak4ssh")
        ]
    ])
    await msg.reply(
        "Hello! 👋 I'm your Edit Guardian Bot, here to maintain a secure environment for our discussions.\n\n"
        "🚫 *Edited Message Deletion*: I'll remove edited messages to maintain transparency.\n\n"
        "📢 *Notifications*: You'll be informed each time a message is deleted.\n\n"
        "🌟 *Get Started*:\n1. Add me to your group.\n2. I'll start protecting instantly.\n\n"
        "➡️ Click on 'Add Me To Your Group' to keep our group safe!",
        reply_markup=keyboard
    )
@app.on_message(filters.command("auth") & filters.reply | filters.command("auth"))
async def authorizeuser(client, msg):
    if not await isadmin(client, msg.chat.id, msg.from_user.id):
        await msg.reply("Only group admins can use this command.")
        return
    user = msg.reply_to_message.from_user if msg.reply_to_message else msg.from_user
    authorizedusers.add(user.id)
    await msg.reply(f"User {user.username or user.id} authorized successfully.")
@app.on_message(filters.command("unauth") & filters.reply | filters.command("unauth"))
async def unauthorizeuser(client, msg):
    if not await isadmin(client, msg.chat.id, msg.from_user.id):
        await msg.reply("Only group admins can use this command.")
        return
    user = msg.reply_to_message.from_user if msg.reply_to_message else msg.from_user
    if user.id in authorizedusers:
        authorizedusers.remove(user.id)
        await msg.reply(f"User {user.username or user.id} unauthorized successfully.")
    else:
        await msg.reply(f"User {user.username or user.id} was not authorized.")
@app.on_message(filters.command("authusers"))
async def listauthorizedusers(client, msg):
    if not await isadmin(client, msg.chat.id, msg.from_user.id):
        await msg.reply("Only group admins can use this command.")
        return
    if authorizedusers:
        users = "\n".join([str(user) for user in authorizedusers])
        await msg.reply(f"Authorized users:\n{users}")
    else:
        await msg.reply("No users are currently authorized.")
@app.on_edited_message()
async def deleteedits(client, msg):
    if msg.from_user.id in authorizedusers:
        return
    if datetime.now() - msg.date > timedelta(minutes=timelimit):
        await msg.delete()
        await client.send_message(
            msg.chat.id,
            f"{msg.from_user.mention} just edited a message and I deleted it. 🤡"
        )
    else:
        print("Edit within 2 minutes; no action taken.")
if __name__ == '__main__':
    app.run()
    app.run_until_disconnected()
