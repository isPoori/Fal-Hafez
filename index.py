# Developer : Pouria Hosseini #
# Telegram ID :@isPoori | CHANNEL : @OmgaDeveloper #

from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
import requests

def start(update: Update) -> None:
    update.message.reply_text("سلام! من ربات فال حافظ هستم. برای گرفتن فال، /fal را ارسال کنید.")

def fal(update: Update) -> None:
    try:
        response = requests.get("https://api.apieco.ir/emrani/hafez/api/hafez/fal")
        if response.status_code == 200:
            fal_text = response.json().get("text")
            update.message.reply_text(fal_text)
        else:
            update.message.reply_text("متاسفانه نمی‌توانم فال حافظ را بگیرم. لطفاً دوباره امتحان کنید.")
    except Exception:
        update.message.reply_text("خطا در ارتباط با وب‌سرویس. لطفاً دوباره امتحان کنید.")

def main() -> None:
    updater = Updater("TOKEN") # TOKEN
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("fal", fal))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
