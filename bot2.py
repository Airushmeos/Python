import telepot
from telepot.loop import MessageLoop
import time
import requests

BOT_TOKEN = '8061813065:AAGUI3xCQOOPDQRG7w-9NHda-ugwa00U_T0'
PHP_API_URL = 'https://myfirstwebsite.lima-city.at/chatbot3.php'  # Hier deine PHP-Datei eintragen

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '').strip()

    if not text:
        return bot.sendMessage(chat_id, "Bitte sende mir eine Nachricht!")

    try:
        # Anfrage an dein PHP-Script
        response = requests.post(PHP_API_URL, json={"message": text})
        if response.status_code == 200:
            antwort = response.json().get("response", "Fehler bei der Antwort.")
        else:
            antwort = f"Fehler vom Server (Code {response.status_code})"
    except Exception as e:
        antwort = f"Fehler: {str(e)}"

    bot.sendMessage(chat_id, antwort)

# Starte Bot
def start_bot():
    global bot
    bot = telepot.Bot(BOT_TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print("Bot läuft...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_bot()
