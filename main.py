from telegram import Update
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext

# Replace 'YOUR_BOT_TOKEN' with your bot's API token
BOT_TOKEN = '7546434205:AAGN7aIVMB8VI63eU_udN6PMB7nLzyllluw'

def delete_edited_message(update: Update, context: CallbackContext) -> None:
    """Delete edited messages."""
    if update.edited_message:
        try:
            # Delete the edited message
            context.bot.delete_message(chat_id=update.edited_message.chat_id,
                                        message_id=update.edited_message.message_id)
        except Exception as e:
            print(f"Error deleting message: {e}")

def main():
    """Start the bot."""
    updater = Updater(BOT_TOKEN)

    # Get the dispatcher to register handlers
    dp = updater.dispatcher

    # Handle edited messages
    dp.add_handler(MessageHandler(Filters.update.edited_message, delete_edited_message))

    # Start the Bot
    updater.start_polling()

    # Run the bot until you send a signal to stop (Ctrl+C)
    updater.idle()

if __name__ == '__main__':
    main()
