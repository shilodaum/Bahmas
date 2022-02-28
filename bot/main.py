import json
import pandas as pd

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

from matcher.searcher import BaseSearcherInArray
from vectorizer.unigram_user_vectorizer import vector_of_user


def get_data(i):
    file = open('../createDB/paths_data.json')
    data = json.load(file)
    path = data[i]
    return path['path_name'], path['path_tiuli_link'], path['path_description'], path['images_links'], path['map_link']


def get_choice(update: Update, context: CallbackContext):
    call_back_data = int(update.callback_query.data)
    name, site, description, images_links, map_link = get_data(call_back_data)
    update.callback_query.message.reply_text(name)
    update.callback_query.message.reply_text("אם אתה רוצה עוד מידע על המסלול :")
    update.callback_query.message.reply_text(site, disable_web_page_preview=False)
    update.callback_query.message.reply_text("החלטת? תתחיל לנווט :")
    update.callback_query.message.reply_text(map_link, disable_web_page_preview=False)
    # update.callback_query.message.reply_text(images_links[0], disable_web_page_preview=False)
    for i in range(min(len(images_links), 3)):
        context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=images_links[i])
    # context.bot.sendMediaGroup(chat_id=update.callback_query.message.chat_id, media=InputMediaPhoto(images_links[0]))
    # update.message.reply_photo(photo)


def reply(update, context):
    """context.bot.delete_messages(chat_id=update.message.chat_id,
                               message_id=update.message.message_id)"""
    user_input = update.message.text
    update.message.reply_text("אתה מעוניין בטיול " + user_input)
    update.message.reply_text("אני ממליץ לך על הטיולים הבאים ")

    world = pd.read_csv('../vectorizer/texts_vectors_unigrams.csv').to_numpy()
    vector = vector_of_user(user_input)
    vector.apply_manipulation(pd.Series.to_numpy)
    searcher = BaseSearcherInArray(vector, world)
    recommendations = searcher.search()

    rank = 1
    keyboard = []
    for i in recommendations:
        title, site, description, images_links, map_link = get_data(i)
        title = title.split(":")[0]
        keyboard.append([InlineKeyboardButton(str(rank) + ") " + title, callback_data=i)])
        """update.message.reply_text(str(rank) + ") " + title)
        update.message.reply_text(site, disable_web_page_preview=False)"""
        # update.message.reply_photo(photo)
        rank += 1
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('לחץ על מסלול שאתה מתעניין בו',
                              reply_markup=reply_markup)

    dp = context.dispatcher
    dp.add_handler(CallbackQueryHandler(get_choice))


def start(update: Update, context: CallbackContext) -> None:
    """context.bot.delete_message(chat_id=update.message.chat_id,
                               message_id=update.message.message_id)"""
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
