import telegram
import logging
import json
import os

from telegram import ParseMode
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import Filters

#enable logging
logging.basicConfig(level=logging.INFO)

TOKEN = "Insert your bot token here" # Bot Token Dari @botfather
CreatorID = 0 # ID Anda


Variable = bool(os.environ.get('Var', False))
if Variable:
    TOKEN = os.environ.get('zb-token', False)
    CreatorID = os.environ.get('zb-id',False)

else:
    TOKEN = TOKEN
    CreatorID = CreatorID

bot = telegram.Bot(token=TOKEN)
updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher 

def Start(update, context):
    data = '/notif\
    Silahkan isi form dibawah\n\n• *Biodata Diri*\n Nama :\n Marga/boru :\n Mamak boru :\n Tempat tgl lahir :\n Kota Asal :\n Kota Sekarang :\n\n• *Media Sosial*(boleh ditambah)\nInstagram :\n\n• *Pesan* (jika ada)\n...\n\n@zonabatak @zonabatakid'
    update.message.reply_text(data, parse_mode=ParseMode.MARKDOWN)

def Reply(update, context):
    msg = update.message.text
    update.message.reply_text(msg)

def SendToCreator(update, context):
    name = update.effective_message.from_user.first_name
    msg = update.effective_message
    text = update.effective_message.text
    # Use replace method 
    # msg = msg.replace("/notif ", "") # Disabled
    # Use split method
    zb = text.replace("/notif", "") # Enabled
    chat_id = update.effective_chat.id
    message = "1 *Pesan baru* dari [{name}](tg://user?id={id}){message}".format(name=name, id=msg.from_user.id, message=zb)
    bot.sendMessage(CreatorID, message, parse_mode=ParseMode.MARKDOWN)
    update.effective_message.reply_text("Pesan telah terkirim!")

def Log(update, context):
    message = update.message
    eventdict = message.to_dict()
    jsondump = json.dumps(eventdict, indent=4)
    update.message.reply_text(jsondump)

start_handler = CommandHandler("start", Start)
reply_handler = CommandHandler("reply", Reply)
feedback_handler = CommandHandler("notif", SendToCreator)
logger_handler = CommandHandler("log", Log)

dispatcher.add_handler(start_handler)
dispatcher.add_handler(reply_handler)
dispatcher.add_handler(feedback_handler)
dispatcher.add_handler(logger_handler)

__log__ = logging.getLogger()
__log__.info("ZonaBatak_Databot Started..")
updater.start_polling()
