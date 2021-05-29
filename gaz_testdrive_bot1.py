import telebot

bot = telebot.TeleBot('1891118214:AAEPqgHluUvHj4_8TkAcr6WP4ywZrwM-sYw')

city = list()
center = list()
auto = list()

@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Здравствуйте! Я - бот-помощник от компании ГАЗ.Я помогу Вам записаться на тест-драйв нужного авто в Вашем городе. Пожалуйста, выберете город, в котором будет проходить тест-драйв: Нижний Новгород или Москва?')
	bot.register_next_step_handler(message, get_center)

def get_center(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if (message.text == "Нижний Новгород"):	
		bot.send_message(message.chat.id, 'Выберете необходимый дилерский центр: ТСС на Удмуртской или Проспект Ленина 88')
		bot.register_next_step_handler(message, get_auto)
	elif (message.text == "Москва"):
		bot.send_message(message.chat.id, 'Выберете необходимый дилерский центр: Авторитейл на МКАД 19км или Авторитэйл на Полярной 31')
		bot.register_next_step_handler(message, get_auto)
	else:	
		bot.send_message(message.chat.id, 'Ошибка. Введите название ещё раз')
		start(message)

def get_auto(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	if (message.text == "ТСС на Удмуртской"):	
		bot.send_message(message.chat.id, 'Выберете доступный автомобиль: Газель Next')
		bot.register_next_step_handler(message, get_auto)
	elif (message.text == "Проспект Ленина 88"):
		bot.send_message(message.chat.id, 'Выберете доступный автомобиль: Газель Next')
		bot.register_next_step_handler(message, get_auto)
	elif (message.text == "Авторитейл на МКАД 19км"):
		bot.send_message(message.chat.id, 'Выберете доступный автомобиль: Газель Next')
		bot.register_next_step_handler(message, get_auto)
	elif (message.text == "Авторитэйл на Полярной 31"):
		bot.send_message(message.chat.id, 'Выберете доступный автомобиль: Газель Next')
		bot.register_next_step_handler(message, get_auto)
	else:	
		bot.send_message(message.chat.id, 'Ошибка. Введите название ещё раз')
		start(message)


bot.polling()

	