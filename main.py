# -*- coding: utf-8 -*-
import random
import config
import responses as R
# from telegram.ext import *

print("Bot started..")
helpcommands = " Type : /new"

def generator():
    pickuplines=['Do you want to commit a sin for your next confessional?',
                'They say that kissing is a language of love, so would you mind starting a conversation with me?',
                'Is your name winter, Because you’ll be coming soon.',
                'I am not into watching sunsets, but I’d love to see you go down.',
                'Are you an exam? Because I have been studying you like crazy.'
                ]
    for i in range(0,4):
        print(pickuplines[i])
        break
        


generator()
# i= random.randint(0,4)
# print(pickuplines[i])

# def start_command(update, context):
#     update.message.reply_text("Type /new to generate pickuplines")

# def help_command(update, context):
#     update.message.reply_text("To get help contact me")

# def handle_message(update, context):
#     text= str(update.message.text).lower()
#     response= R.sample_resources(text)

#     update.message.reply_text(response)

# def error(update, context):
#     print("update"+str(update)+"caused "+str(context.error))

# def new(update, context):
#     update.message.reply_text(str(pickuplines[i]))

# def main():
#     updater = Updater(config.api_token, use_context=True)
#     dp= updater.dispatcher

#     dp.add_handler(CommandHandler("start", start_command))
#     dp.add_handler(MessageHandler(Filters.text, handle_message))
#     dp.add_handler(CommandHandler("new", new))

#     dp.add_error_handler(error)

#     updater.start_polling(5)
#     updater.idle()



# main()