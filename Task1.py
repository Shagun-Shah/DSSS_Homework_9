from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

API_TOKEN = '7765799285:AAEspqbsgtbOOgb3anyDO7hqDNKT873RZHI'

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Hello! I am your AI assistant, how can I help you!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user_response = update.message.text
    await update.message.reply_text("I have received your message:  \"{}\"".format(user_response))

def main():
    # Creation of Application object
    application = Application.builder().token(API_TOKEN).build()

    # Command and message handlers
    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))

    # Start the bot
    application.run_polling()

if __name__ == '__main__':
    main()

