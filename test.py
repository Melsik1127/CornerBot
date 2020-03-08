import requests
from bs4 import BeautifulSoup
import sys
import time
import telebot
from selenium import webdriver


done = 0
TOKEN = '1070470382:AAF82ZpThuB4xx_ic4MfBxrVQZm0bjsCcTg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def handle_start_help_one(message):
	bot.send_message(message.chat.id, 'Добро пожаловать на Corner_Bot, здесь вы можете отслеживать угловые в режиме реального времени. Для того что-бы начать введите команду /corner . Внимание! После ввода команды нужно немного подождать, пока идет загрузка данных с сайта 1xbet. ')


@bot.message_handler(commands=['start', 'corner'])
def handle_start_help(message):
	bot.send_message(message.chat.id, 'Мы оповестим вас, когда найдем матч...')
	j = True
	mass = []
	goal = []
	comm = []

	m = True
	if j == True:
		def trade_spiders (max_page):
		    url = 'https://1xbetua.com/live/Football'
		    source_code = requests.get(url)
		    soup = BeautifulSoup(source_code.text, 'html.parser')
		    main_title = soup.find_all('a', {"class": "c-events__name"})
		    for title in main_title:
		        a = title.text.strip()  # Первый элемент - название, второй - ссылка.
		        b = title.get('href')
		       	d = 'https://1xbetua.com/' + b
		       	mass.append(d)
		        comm.append(a)

		

	def trade_spiders2 ():
		for i in range(0, len(mass)-1):
			chromedriver = 'chromedriver.exe'
			driver = webdriver.Chrome(chromedriver)
			url = mass[i]
			driver.get(url)
			time.sleep(5)
			
				
			txt = '0'
			for i in driver.find_elements_by_class_name('c-tablo-event__item'):
				goal.append(i.text)
			for n in driver.find_elements_by_class_name('c-tablo__text'):
				if n.text == 'Перерыв':
					txt = n.text
			if ('Перерыв' in txt) and (goal[1] == '0' or goal[1] == '1') and (goal[9] == '0' or goal[9] == '1'):
				bot.send_message(message.chat.id, comm[0] + ':')
				bot.send_message(message.chat.id, 'Угловые: ' + ' ' + goal[1] + ' : ' + goal[9])
				done = 1
			goal.clear()
			del(comm[0])
					
			driver.quit()
				
				

	trade_spiders(1)
	trade_spiders2()
	if done == 0:
		bot.send_message(message.chat.id, 'Сейчас нет подобных матчей. Подождите немного, и попробуйте снова')
	comm = []
bot.polling()


        

