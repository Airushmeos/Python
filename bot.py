import telepot
from telepot.loop import MessageLoop
import time

BOT_TOKEN = '8061813065:AAGUI3xCQOOPDQRG7w-9NHda-ugwa00U_T0'

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '')

    if text.lower() == '/start':
        bot.sendMessage(chat_id, 'Hey! Ich bin dein Telepot-Bot.')
    elif text.lower() == 'ping':
        bot.sendMessage(chat_id, 'Pong!')
    else:
        bot.sendMessage(chat_id, f'Du hast gesagt: {text}')

bot = telepot.Bot(BOT_TOKEN)
MessageLoop(bot, handle).run_as_thread()

print('Bot läuft...')

while True:
    time.sleep(10)
