import json
import pandas as pd
import os
import re

# os.chdir(os.path.join('.', 'bot'))
# print('dir', os.getcwd())
# if not os.getcwd().endswith('bot'):
#     # if 'Bahmas' in os.getcwd():
#     os.chdir('./bot/')
#     # print('new dir', os.getcwd())
#     print('dir', os.getcwd())
#     # insert at 1, 0 is the script path (or '' in REPL)
# import sys
#
# sys.path.insert(0, './bot')

import vectorizer.unigram_user_vectorizer as uni_user
import vectorizer.bigram_user_vectorizer as bi_user
import matcher.matcher as matcher

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# from searcher.searcher import BaseSearcherInArray
if 'Bahmas' in os.getcwd():
    directory = os.getcwd()
else:
    directory = "/app"

# TODO add path to bahmas
uni_world = pd.read_csv(os.path.join(directory, 'vectorizer', 'texts_vectors_unigrams.zip'))
bi_world = pd.read_csv(os.path.join(directory, 'vectorizer', 'texts_vectors_bigrams.zip'))


def get_data(i):
    file = pd.read_json(os.path.join(directory, 'createDB', 'paths_data.zip'))  # open('./createDB/paths_data.json')
    # data = json.load(file)
    path = file.iloc[i]
    return path['path_name'], path['path_links'], path['path_description'], path['images_links'], path['map_link']


def get_choice(update: Update, context: CallbackContext):
    call_back_data = int(update.callback_query.data)
    name, sites, description, images_links, map_link = get_data(call_back_data)
    update.callback_query.message.reply_text(name)
    update.callback_query.message.reply_text("אם אתה רוצה עוד מידע על המסלול :")
    if len(sites[0]) > 0:
        update.callback_query.message.reply_text(sites[0], disable_web_page_preview=False)
    if len(map_link) > 0:
        update.callback_query.message.reply_text("החלטת? תתחיל לנווט :")
        context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=map_link)
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

    # TODO: change it
    # uni_world = pd.read_csv('../vectorizer/texts_vectors_unigrams.zip')
    # bi_world = pd.read_csv('../vectorizer/texts_vectors_bigrams.zip')

    print('----------------building user vectors----------------')
    uni_vector = uni_user.vector_of_user(user_input)
    bi_vector = bi_user.vector_of_user(user_input)

    print('----------------getting recommendations----------------')
    recommendations = matcher.get_recommendation(uni_world, bi_world, uni_vector, bi_vector)

    # vector.apply_manipulation(pd.Series.to_numpy)
    # searcher = BaseSearcherInArray(vector, world)
    # recommendations = searcher.search()

    rank = 1
    keyboard = []
    for i in recommendations:
        title, site, description, images_links, map_link = get_data(i)
        # TODO use regex split to delete all -:., symbols
        title = re.split('[.:,-]', title)[0]
        keyboard.append([InlineKeyboardButton(str(rank) + ") " + title, callback_data=int(i))])
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
    # TODO לשון פניה
    update.message.reply_text(f'באיזה טיול אתה מעוניין?')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))


updater = Updater("5117463685:AAGDzPkJxZ7whs36ZumgdkyifMO5OP51gIM")
updater.dispatcher.add_handler(CommandHandler('start', start))
updater.start_polling()
updater.idle()
