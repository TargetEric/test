import asyncio
from telegram import Update
from telegram.ext import ApplicationBuilder, MessageHandler, filters, ContextTypes

# Replace 'YOUR_BOT_TOKEN' with your bot's API token
BOT_TOKEN = '7546434205:AAGN7aIVMB8VI63eU_udN6PMB7nLzyllluw'

async def delete_edited_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Delete edited messages."""
    if update.edited_message:
        try:
            # Delete the edited message
            await context.bot.delete_message(chat_id=update.edited_message.chat_id,
                                              message_id=update.edited_message.message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")

async def main():
    """Start the bot."""
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    # Handle edited messages
    app.add_handler(MessageHandler(filters.UpdateType.EDITED_MESSAGE, delete_edited_message))

    # Start the Bot
    await app.run_polling()

if __name__ == '__main__':
    # Check if the event loop is already running
    try:
        asyncio.get_event_loop().run_until_complete(main())
    except RuntimeError as e:
        if str(e) == 'This event loop is already running':
            # If the event loop is already running, create a task for the main function
            asyncio.ensure_future(main())
        else:
            raise
