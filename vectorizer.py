def dict_to_sorted_items(d):
    """
    convert dictionary of (word, num_of_occurrences) to sorted items list.
    :param d: dictionary of the words in the text and the number of their occurrences (word, num_of_occurrences)
    :return: sorted items list of the words
    """
    return sorted(list(d.items()), key=lambda item: item[1], reverse=True)


def get_stop_words(words_path='heb_stop_words.txt'):
    """
    get list of hebrew stop_words
    :param words_path: path to file with words list
    :return: list of hebrew stop_words
    """
    sent = ''
    with open(words_path, 'r') as f:
        sent = f.read()
    return sent.split()


def filter_hebrew(words_list, symbols):
    """
    filter out words not in hebrew
    :param words_list: list of words from text as [(word,count)...]
    :param symbols: symbols to delete
    :return: list of filtered words
    """
    words_dict = dict(words_list)

    for key, value in words_list:
        if len(key) <= 1:
            del words_dict[key]

        # delete numbers
        elif key.isnumeric():
            del words_dict[key]

        # sentence that ends with a symbol
        elif key[-1] in symbols.split():
            if all("\u0590" <= character <= "\u05EA" for character in key[:-1]):
                if key[:-1] in words_dict.keys():
                    words_dict[key[:-1]] += words_dict[key]
                else:
                    words_dict[key[:-1]] = words_dict[key]
            del words_dict[key]

        # sentence contains characters not in hebrew
        elif not all("\u0590" <= character <= "\u05EA" for character in key):
            del words_dict[key]

    return dict_to_sorted_items(words_dict)


def filter_prefixes(words_list, prefixes):
    """
    filter out prefixes from words
    :param words_list: list of words from text as [(word,count)...]
    :param prefixes: prefixes
    :return: filtered words
    """
    words_dict = dict(words_list)
    for pref in prefixes.split():
        for word, freq in words_list:
            if pref + word in words_dict.keys() and word in words_dict.keys():
                words_dict[word] += words_dict[pref + word]
                del words_dict[pref + word]

    return dict_to_sorted_items(words_dict)


def manage_prefixes(words_list, symbols='? - ! . , : ;', prefixes='ה ו ב ל ש מ כ וש שה מה לה בה וה'):
    """
    delete symbols and prefixes
    :param words_list: list of words from text
    :param symbols: symbols
    :param prefixes: prefixes
    :return: filtered word list
    """
    hebrew_buzzwords = filter_hebrew(words_list, symbols)
    buzzwords_prefixes = filter_prefixes(hebrew_buzzwords, prefixes)
    return buzzwords_prefixes
