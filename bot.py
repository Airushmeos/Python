import telepot
from telepot.loop import MessageLoop
import time
import logging
import random
from datetime import datetime

# Deinen Bot-Token hier einfügen
BOT_TOKEN = '8061813065:AAGUI3xCQOOPDQRG7w-9NHda-ugwa00U_T0'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

# Quizfragen (optional)
quizfragen = [
    {"frage": "Wie viele Planeten hat unser Sonnensystem?", "antwort": "8"},
    {"frage": "Was ist die Hauptstadt von Österreich?", "antwort": "wien"},
    {"frage": "Wieviel ist 7 * 8?", "antwort": "56"}
]

# Begrüßung
def send_welcome_message(chat_id):
    message = (
        "Hey! Ich bin dein Bot. Hier sind ein paar Dinge, die ich kann:\n"
        "/hilfe - Zeigt alle Befehle\n"
        "ping - Ich sag Pong!\n"
        "echo [Text] - Ich wiederhole deinen Text\n"
        "/zufall - Ich gebe dir was Zufälliges\n"
        "/uhrzeit - Aktuelle Zeit und Datum\n"
        "/rechnen [Formel] - Rechne was für dich\n"
        "/quiz - Ich stelle dir eine Frage"
    )
    bot.sendMessage(chat_id, message)

# Hilfe anzeigen
def show_help(chat_id):
    help_text = (
        "Hier sind meine Befehle:\n"
        "/hilfe\n"
        "ping\n"
        "echo [Text]\n"
        "/zufall\n"
        "/uhrzeit\n"
        "/rechnen [Formel]\n"
        "/quiz"
    )
    bot.sendMessage(chat_id, help_text)

# Nachricht verarbeiten
def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '').strip().lower()

    logging.info(f"Nachricht erhalten: {text}")

    if text == '/start':
        send_welcome_message(chat_id)
    elif text == '/hilfe':
        show_help(chat_id)
    elif text == 'ping':
        bot.sendMessage(chat_id, 'Pong!')
    elif text.startswith('echo '):
        bot.sendMessage(chat_id, msg['text'][5:])
    elif text == '/zufall':
        random_response(chat_id)
    elif text == '/uhrzeit':
        send_current_time(chat_id)
    elif text.startswith('/rechnen'):
        formula = msg['text'][9:].strip()
        calculate(formula, chat_id)
    elif text == '/quiz':
        ask_quiz(chat_id)
    else:
        bot.sendMessage(chat_id, "Ich kenn das nicht. Probier mal /hilfe")

# Zufallsausgabe
def random_response(chat_id):
    antworten = [
        f"Zufallszahl: {random.randint(1, 100)}",
        "Spruch: 'Der frühe Vogel kann mich mal.'",
        "Witz: Warum können Geister so schlecht lügen? Weil man durch sie hindurchsieht!"
    ]
    bot.sendMessage(chat_id, random.choice(antworten))

# Aktuelle Zeit
def send_current_time(chat_id):
    now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
    bot.sendMessage(chat_id, f"Aktuelle Zeit: {now}")

# Rechnen
def calculate(formel, chat_id):
    try:
        ergebnis = eval(formel)
        bot.sendMessage(chat_id, f"{formel} = {ergebnis}")
    except:
        bot.sendMessage(chat_id, "Fehler beim Rechnen. Versuch z. B. /rechnen 5+3")

# Quizfrage stellen
def ask_quiz(chat_id):
    frage = random.choice(quizfragen)
    bot.sendMessage(chat_id, f"Quizfrage: {frage['frage']}\n(Schreib die Antwort einfach zurück.)")
    # Man könnte hier auch ein Memory speichern, aber für einfachen Einsatz reicht das

# Bot starten
def start_bot():
    global bot
    bot = telepot.Bot(BOT_TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    logging.info("Bot läuft...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_bot()
