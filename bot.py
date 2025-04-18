import telepot
from telepot.loop import MessageLoop
import time
import random
from datetime import datetime
import logging

BOT_TOKEN = 'DEIN_BOT_TOKEN_HIER'

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '').strip().lower()

    if text == '/start':
        bot.sendMessage(chat_id, "Hey! Gib /hilfe ein für eine Liste der Befehle.")
    elif text == '/hilfe':
        bot.sendMessage(chat_id, (
            "Hier sind meine Befehle:\n"
            "ping - Pong!\n"
            "echo [Text] - Ich wiederhole\n"
            "/zufall - Zufällige Antwort\n"
            "/uhrzeit - Aktuelle Uhrzeit\n"
            "/rechnen [Formel] - Rechnen\n"
            "/quiz - Stelle dir eine Frage\n"
            "/witz - Gib dir einen Witz\n"
            "/fakt - Fun Fact\n"
            "/motiv - Motivation\n"
            "/coin - Münzwurf\n"
            "/würfeln - Würfeln"
        ))
    elif text == 'ping':
        bot.sendMessage(chat_id, 'Pong!')
    elif text.startswith('echo '):
        bot.sendMessage(chat_id, msg['text'][5:])
    elif text == '/zufall':
        antworten = [
            "42 ist die Antwort auf alles.",
            "Zufallszahl: " + str(random.randint(1, 100)),
            "Zufallswort: Banane!"
        ]
        bot.sendMessage(chat_id, random.choice(antworten))
    elif text == '/uhrzeit':
        now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
        bot.sendMessage(chat_id, f"Aktuelle Zeit: {now}")
    elif text.startswith('/rechnen'):
        try:
            formel = msg['text'][9:].strip()
            result = eval(formel)
            bot.sendMessage(chat_id, f"{formel} = {result}")
        except:
            bot.sendMessage(chat_id, "Ungültige Formel!")
    elif text == '/witz':
        witze = [
            "Warum können Geister so schlecht lügen? Weil man durch sie hindurchsieht!",
            "Was ist orange und läuft durch den Wald? Eine Wanderine.",
            "Warum ging der Pilz auf die Party? Weil er ein Champignon war!"
        ]
        bot.sendMessage(chat_id, random.choice(witze))
    elif text == '/fakt':
        fakten = [
            "Ein Oktopus hat drei Herzen.",
            "Honig verdirbt nie.",
            "Die meisten Kühe haben beste Freundinnen.",
            "Banane ist eine Beere, Erdbeere nicht."
        ]
        bot.sendMessage(chat_id, random.choice(fakten))
    elif text == '/motiv':
        zitate = [
            "Du schaffst das!",
            "Glaub an dich!",
            "Träume groß, fang klein an.",
            "Sei du selbst – alle anderen gibt es schon."
        ]
        bot.sendMessage(chat_id, random.choice(zitate))
    elif text == '/coin':
        bot.sendMessage(chat_id, random.choice(["Kopf", "Zahl"]))
    elif text == '/würfeln':
        bot.sendMessage(chat_id, f"Du hast eine {random.randint(1, 6)} gewürfelt!")
    elif text == '/quiz':
        fragen = [
            ("Was ist 5+7?", "12"),
            ("Hauptstadt von Frankreich?", "paris"),
            ("Welche Farbe ergibt Rot + Blau?", "lila")
        ]
        frage, antwort = random.choice(fragen)
        bot.sendMessage(chat_id, f"Quizfrage: {frage} (Antwort: {antwort})")
    else:
        bot.sendMessage(chat_id, "Unbekannter Befehl. Versuch /hilfe")

# Bot starten
def start_bot():
    global bot
    bot = telepot.Bot(BOT_TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    logging.info("Bot läuft!")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_bot()
