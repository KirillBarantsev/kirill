import telebot
from telebot import types

bot = telebot.TeleBot('1891118214:AAEPqgHluUvHj4_8TkAcr6WP4ywZrwM-sYw')



@bot.message_handler(content_types=['text'])

def start(message):
	bot.send_message(message.from_user.id, 'Напишите Старт')
	bot.register_next_step_handler(message, get_city)

def get_city(message):
	if message.text == 'Старт':
		keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		city1 = types.KeyboardButton('Москва')
		city2 = types.KeyboardButton('Нижний Новгород')
		keyboard_markup.add(city1, city2)
		bot.send_message(message.chat.id, 'Выберите город', reply_markup = keyboard_markup)
		bot.register_next_step_handler(message, get_center)
	else:
		bot.send_message(message.from_user.id, 'Напишите Старт')

def get_center(message):
	if message.text == 'Москва':
		keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		center1 = types.KeyboardButton('Авторитейл на МКАД 19км')
		center2 = types.KeyboardButton('Авторитэйл на Полярной 31')
		keyboard_markup.add(center1, center2)
		bot.send_message(message.chat.id, 'Выберите дилерский центр', reply_markup = keyboard_markup)
		bot.register_next_step_handler(message, get_auto)
	else:
		keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
		center3 = types.KeyboardButton('ТСС на Удмуртской')
		center4 = types.KeyboardButton('Проспект Ленина 88')
		keyboard_markup.add(center3, center4)
		bot.send_message(message.chat.id, 'Выберите дилерский центр', reply_markup = keyboard_markup)
		bot.register_next_step_handler(message, get_auto)

def get_auto(message):
	if message.text == 'Авторитейл на МКАД 19км':
		center = 'Москва Авторитейл на МКАД 19км'
	elif message.text == 'Авторитэйл на Полярной 31':
		center = 'Москва Авторитэйл на Полярной 31'
	elif message.text == 'ТСС на Удмуртской':
		center = 'Нижний Новгород ТСС на Удмуртской'
	else:
		center = 'Нижний Новгород Проспект Ленина 88'
	keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
	auto1 = types.KeyboardButton('Газель Next')
	auto2 = types.KeyboardButton('Газель Business')
	keyboard_markup.add(auto1, auto2)
	bot.send_message(message.chat.id, 'Выберите доступную модель авто', reply_markup = keyboard_markup)
	bot.register_next_step_handler(message, get_name)

def get_name(message):
	if message.text == 'Газель Next':
		auto = 'Газель Next'
	else:
		auto = 'Газель Business'
	bot.send_message(message.chat.id, 'Пожалуйста, напишите ваше имя')
	bot.register_next_step_handler(message, get_name1)

def get_name1(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	name = message.text
	bot.register_next_step_handler(message, name)
	bot.send_message(message.chat.id, 'Пожалуйста, напишите ваш номер телефона')
	bot.register_next_step_handler(message, get_phone)

def get_phone(message):
	bot.send_chat_action(message.from_user.id, 'typing')
	phone = message.text
	bot.register_next_step_handler(message, final)

def final(message):
	res = ' '.join ((center, auto, name, phone)) 
	bot.send_message(message.chat.id, 'Спасибо! С Вами свяжется наш специалист в ближайшее время')


	

bot.polling()

	