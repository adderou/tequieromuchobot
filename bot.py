import math

from telegram import InlineQueryResultArticle, InputTextMessageContent
from telegram.ext import InlineQueryHandler, Updater

BOT_TOKEN = "BOT_TOKEN"

def create_tqm_line(line_text):
    padding = (28 - len(line_text)) / 2
    created_line = "|" + " " * int(math.ceil(padding)) + line_text + int(math.floor(padding)) * " " + "|"
    return created_line

def create_tqm_body(text):
    text_array = text.split(" ")
    msg_body = []
    current_line = ""
    for word in text_array:
        if len(current_line) + len(word) <= 28:
            if len(current_line) != 0:
                current_line += " "
            current_line += word
        else:
            # Add the current line and create a new one.
            msg_body.append(create_tqm_line(current_line))
            if len(word) <= 26:
                # Add the word if it fits.
                current_line = word
    msg_body.append(create_tqm_line(current_line))
    return "\n".join(msg_body) + "\n"

def get_tqm(text):
    msg_head =  "|￣￣ ￣￣￣￣￣￣￣￣￣￣￣￣￣￣|\n" +\
                "|    hola te quiero mucho    |\n"

    msg_body = create_tqm_body(text)
    msg_foot =  "|____ _______________________|\n" +\
                "(\_/)  ||\n" +\
                "(•ㅅ•) ||\n" +\
                "/    づ\n"
    return "```\n" + msg_head + msg_body + msg_foot + "```"


def inline_tqm(bot, update):
 query = update.inline_query.query
 if not query:
     return
 results = list()
 results.append(
     InlineQueryResultArticle(
         id=query,
         title='Te quiero mucho',
         input_message_content=InputTextMessageContent(get_tqm(query), parse_mode="markdown")
     )
 )
 bot.answer_inline_query(update.inline_query.id, results)

updater = Updater(token='BOT_TOKEN')
dispatcher = updater.dispatcher
inline_caps_handler = InlineQueryHandler(inline_tqm)
dispatcher.add_handler(inline_caps_handler)

updater.start_polling()