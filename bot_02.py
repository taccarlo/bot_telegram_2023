from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

frasi = {"buongiorno":["Goodmorning!","Buongiorno!"],"ciao":["Hello!", "Ciao!"]}

# IMPORTANTE: inserire il token fornito dal BotFather nella seguente stringa
with open("token.txt", "r") as f:
    TOKEN = f.read()
    print("Il tuo token è ", TOKEN)

def getMessage(update:Update, key):
    if(update.effective_user.language_code=="it"):
        return frasi[key][1]
    else:
        return frasi[key][0]

async def goodmorning(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    message = getMessage(update, "buongiorno")
    await update.message.reply_text(message)


async def hello(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    update.effective_user.language_code
    message = getMessage(update, "ciao") 
    await update.message.reply_text(message)


def main():
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("hello", hello))
    app.add_handler(CommandHandler("goodmorning", goodmorning))
    app.run_polling()


if __name__=='__main__':
   main()