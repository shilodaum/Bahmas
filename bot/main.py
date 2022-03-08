import json
import pandas as pd
import os
import re
import numpy as np
import vectorizer.unigram_user_vectorizer as uni_user
import vectorizer.bigram_user_vectorizer as bi_user
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup, InputMediaPhoto
from telegram.ext import Updater, CommandHandler, CallbackContext, MessageHandler, Filters, CallbackQueryHandler

# global variables
from searcher.searcher import InterpolationSearcher
from searcher.super_vector import SuperVector

IS_ESTIMATION = True

# Change the project directory
if 'Bahmas' in os.getcwd():
    if not os.getcwd().endswith('Bahmas'):
        os.chdir('..')
    directory = os.getcwd()
else:
    directory = "/app"

# Read the csv with the uni and bi vectors of the data
uni_world = pd.read_csv(os.path.join(directory, 'vectorizer', 'texts_vectors_unigrams.zip'), dtype=np.int8)
print('read uni world')
bi_world = pd.read_csv(os.path.join(directory, 'vectorizer', 'texts_vectors_bigrams.zip'), dtype=np.int8)
print('read bi world')

# Read the database from the JSON file
all_paths = pd.read_json(os.path.join(directory, 'createDB', 'paths_data.zip'))
print('read all paths')


def get_data(i):
    """
    Returns the path in index i
    """
    path = all_paths.iloc[i]

    return path['path_name'], path['path_links'], path['path_description'], path['images_links'], path['map_link'], \
           path['navigation']


def get_choice(update: Update, context: CallbackContext):
    """
    Send to the user the details of the chosen path
    """

    # Get the details of the chosen path from the database
    call_back_data = int(update.callback_query.data)
    name, sites, description, images_links, map_link, waze_link = get_data(call_back_data)

    update.callback_query.message.reply_text(name)
    update.callback_query.message.reply_text("אם את.ה רוצה עוד מידע על המסלול :")

    # Send the links to the hiking websites
    if len(sites[0]) > 0:
        update.callback_query.message.reply_text(sites[0], disable_web_page_preview=False)
    if len(map_link) > 0:
        update.callback_query.message.reply_text("החלטת? תתחיל.י לנווט :")
        update.callback_query.message.reply_text(waze_link)
        context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=map_link)

    # Send images to the user
    for i in range(min(len(images_links), 3)):
        context.bot.send_photo(chat_id=update.callback_query.message.chat_id, photo=images_links[i])

    # Send link to the forms
    if IS_ESTIMATION:
        update.callback_query.message.reply_text("נשמח אם תיתן.י לנו משוב :")
        update.callback_query.message.reply_text("https://forms.gle/6FnxZJem2VYeRUCM6", disable_web_page_preview=False)


def reply(update, context):
    """Send to the user the most recommended paths according to his query"""

    user_input = update.message.text
    update.message.reply_text("רק שניה...")

    print('----------------building user vectors----------------')
    uni_vector = uni_user.vector_of_user(user_input)
    bi_vector = bi_user.vector_of_user(user_input)

    print('----------------getting recommendations----------------')
    vector = SuperVector(uni_vector, bi_vector, "interp")
    searcher = InterpolationSearcher(vector, uni_world, bi_world)
    recommendations = searcher.search()

    # Create entries file
    if not os.path.isfile("entries.json"):
        with open("entries.json", 'w'):
            pass
    with open('entries.json', 'a') as f:
        to_write = [recommendations[j][i] for i in range(len(recommendations[0])) for j in range(2)]
        val = json.dumps([user_input, *to_write])
        f.write(val)

    # print recommendations
    rank = 1
    keyboard = []
    for i in recommendations[0][:5]:
        title, site, description, images_links, map_link, waze_link = get_data(i)
        title = re.split('[<>.:-]', title)[0]
        keyboard.append([InlineKeyboardButton(str(rank) + ") " + title, callback_data=int(i))])
        rank += 1
    reply_markup = InlineKeyboardMarkup(keyboard)
    update.message.reply_text('בחר.י מסלול לפירוט',
                              reply_markup=reply_markup)

    # handle choice of specific path
    dp = context.dispatcher
    dp.add_handler(CallbackQueryHandler(get_choice))


def start(update: Update, context: CallbackContext) -> None:
    """
    start the discussion with the bot
    """
    # start message and image
    update.message.reply_text(f'שלום {update.effective_user.first_name}')
    update.message.reply_photo("https://images.app.goo.gl/HkooWVK1gp22abs56")

    # get query from user
    update.message.reply_text(f'באיזה טיול את.ה מעוניין.ת?')
    dp = updater.dispatcher
    dp.add_handler(MessageHandler(Filters.text, reply))


# bot handling
updater = Updater("5117463685:AAGDzPkJxZ7whs36ZumgdkyifMO5OP51gIM")
print('created updater')
updater.dispatcher.add_handler(CommandHandler('start', start))
print('strat command')
updater.start_polling()
updater.idle()
