#import telebot
import psutil
import time

# Замените 'YOUR_BOT_TOKEN' на токен вашего бота
#bot = telebot.TeleBot('YOUR_BOT_TOKEN')

# ID чата, куда будут отправляться уведомления
#chat_id = 'YOUR_CHAT_ID'

def check_battery():
    battery = psutil.sensors_battery()
    return battery.power_plugged

#@bot.message_handler(commands=['start'])
#def send_welcome(message):
#    bot.reply_to(message, "Привет! Я буду уведомлять тебя, когда телефон будет поставлен на зарядку.")

def notify_charging():
    while True:
        if check_battery():
            #bot.send_message(chat_id, "Телефон поставлен на зарядку!")
            print("Телефон поставлен на зарядку!")
            time.sleep(60)  # Проверка каждые 60 секунд

if __name__ == '__main__':
    #bot.polling(none_stop=True)
    notify_charging()

