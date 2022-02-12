from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters


def reply(update, context):
    user_input = update.message.text
    update.message.reply_text("אתה מעוניין בטיול " + user_input)
    update.message.reply_text("אני ממליץ לך על : ")

    titles = ["עין הנציב", "בריכת המשושים", "נחל כזיב"]
    site_urls = ["https://www.tiuli.com/points-of-interest/153/%D7%A2%D7%99%D7%9F-%D7%94%D7%A0%D7%A6%D7%99%D7%91-%D7%A2%D7%99%D7%9F-%D7%99%D7%94%D7%95%D7%93%D7%94",
                 "https://www.tiuli.com/tracks/124/%D7%96%D7%95%D7%95%D7%99%D7%AA%D7%9F-%D7%AA%D7%97%D7%AA%D7%95%D7%9F-%D7%95%D7%91%D7%A8%D7%99%D7%9B%D7%AA-%D7%94%D7%9E%D7%A9%D7%95%D7%A9%D7%99%D7%9D",
                 "https://www.tiuli.com/tracks/8/%D7%A0%D7%97%D7%9C-%D7%9B%D7%96%D7%99%D7%91"]
    photo_urls = ["https://images.app.goo.gl/KpJPWixSRH2bH8t76",
                  "https://images.app.goo.gl/9jSMP8K5YVwPw5fEA",
                  "https://images.app.goo.gl/E82JBrnYWVT1Yn498"]

    for i, (title, site, photo) in enumerate(zip(titles, site_urls, photo_urls)):
        update.message.reply_text(str(i+1) + ") " + title)
        update.message.reply_text(site, disable_web_page_preview=False)
        update.message.reply_photo(photo)


def start(update: Update, context: CallbackContext) -> None:
    # start message and image
    update.message.reply_text(f'שלום {update.effective_user.first_name}')
    update.message.reply_photo("https://images.app.goo.gl/HkooWVK1gp22abs56")

    # get query from user
    update.message.reply_text(f'באיזה טיול אתה מעוניין?')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))


updater = Updater("5117463685:AAGDzPkJxZ7whs36ZumgdkyifMO5OP51gIM")

updater.dispatcher.add_handler(CommandHandler('start', start))

updater.start_polling()
updater.idle()