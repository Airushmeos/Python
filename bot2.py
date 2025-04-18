import telepot
from telepot.loop import MessageLoop
import time
import requests
import sys

BOT_TOKEN = '8061813065:AAGUI3xCQOOPDQRG7w-9NHda-ugwa00U_T0'
PHP_API_URL = 'https://myfirstwebsite.lima-city.at/KI/chatbot3.php'

def handle(msg):
    chat_id = msg['chat']['id']
    text = msg.get('text', '').strip()

    if not text:
        return bot.sendMessage(chat_id, "Bitte sende mir eine Nachricht!")

    if text.lower() == "exit":
        bot.sendMessage(chat_id, "Bot wird beendet...")
        print("Beende Bot durch Benutzeranfrage...")
        sys.exit()

    try:
        response = requests.post(PHP_API_URL, json={"message": text})
        if response.status_code == 200:
            antwort = response.json().get("response", "Fehler bei der Antwort.")
        else:
            antwort = f"Fehler vom Server (Code {response.status_code})"
    except Exception as e:
        antwort = f"Fehler: {str(e)}"

    # Log in Datei speichern
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(f"Frage: {text}\nAntwort: {antwort}\n\n")

    bot.sendMessage(chat_id, antwort)

def start_bot():
    global bot
    bot = telepot.Bot(BOT_TOKEN)
    MessageLoop(bot, handle).run_as_thread()
    print("Bot läuft...")
    while True:
        time.sleep(10)

if __name__ == "__main__":
    start_bot()
