import telebot
import SeleiumPortal as sp

bot = telebot.TeleBot("Telegram Bot Token here")
keyboard1 = telebot.types.ReplyKeyboardMarkup()
keyboard1.row('Request', 'Bye')


@bot.message_handler(commands=['start'])
def start_message(message):
	bot.send_message(message.chat.id, 'Input your email', reply_markup=keyboard1)

email = ""
password = ""
sem = ""

@bot.message_handler(content_types=['text'])
def send_text(message):
	global email, password, sem
	if message.text.lower().startswith("email"):
		bot.send_message(message.chat.id, 'Email Etnered')
		email = message.text[6:]
	elif message.text.startswith("pass"):
		bot.send_message(message.chat.id, "Password entered")
		password = message.text[5:]
	elif message.text.lower().startswith("sem"):
		bot.send_message(message.chat.id, "Semester entered")
		sem = message.text[4:]
	elif message.text.lower() == "request":
		bot.send_message(message.chat.id, 'Requesting...')
		data = sp.main(email, password, sem)
		#bot.send_message(message.chat.id, f"<pre>{data}</pre>", parse_mode="HTML")
		bot.send_photo(message.chat.id, photo=open("img/test.png", 'rb'))


bot.polling()
