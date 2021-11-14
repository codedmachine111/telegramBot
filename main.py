# -*- coding: utf-8 -*-
import random
import config
import responses as R
from telegram.ext import *

print("Bot ACTIVE..")

helpcommands = " Type : /new"

def start_command(update, context):
    update.message.reply_text("Type /new to generate pickuplines")

def help_command(update, context):
    update.message.reply_text("To get help contact me")

def handle_message(update, context):
    text= str(update.message.text).lower()
    response= R.sample_resources(text)

    update.message.reply_text(response)

def error(update, context):
    print("update"+str(update)+"caused "+str(context.error))

def new(update, context):
    update.message.reply_text("Hey check out my github at https://github.com/codedmachine111")

def main():
    updater = Updater(config.api_token, use_context=True)
    dp= updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_handler(CommandHandler("new", new))

    dp.add_error_handler(error)

    updater.start_polling(5)
    updater.idle()



main()
