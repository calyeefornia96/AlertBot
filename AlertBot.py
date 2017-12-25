from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from threading import Timer
import re

TOKEN = "505605940:AAF0so7wX6XwKSrT6r44Q_Vz4kj9nK8KmR4"

stringHowItWorks = '''Format to create alerts:
/alert Time Text\n
\'Time\' is inserted in this format:
5m, 5h, 5d, or 5w\n
\'Text\' is what you want to be reminded of'''

def start(bot, update):
	update.message.reply_text("Hi!")
	update.message.reply_text(stringHowItWorks)

def help(bot, update):
	update.message.reply_text(stringHowItWorks)

def setAlert(bot, update):
	stringOfCommand = update.message.text.split(" ")
	if len(stringOfCommand) < 2:
		help(bot, update)
	time = stringOfCommand[1]
	lengthOfTime = calculateTime(time)

	toDo = ''
	for word in range(2, len(stringOfCommand)):
		toDo += stringOfCommand[word]
		toDo += " "

	countDownAlert = Timer(lengthOfTime, sendAlert, args=(bot,update,toDo))
	countDownAlert.start()

def calculateTime(time):
	toFindTime = re.compile('(\d+)(\w){1}', re.I)
	capturedTime = toFindTime.match(time)
	number = capturedTime.group(1)
	suffix = capturedTime.group(2)
	number = int(number)
	if suffix == 'm' or suffix == 'M':
		return number * 60
	elif suffix == 'h' or suffix == 'H':
		return number * 60 * 60
	elif suffix == 'd' or suffix == 'D':
		return number * 60 * 60 * 24
	elif suffix == 'w' or suffix == 'W':
		return number * 60 * 60 * 24 * 7
	else:
		return 0

def sendAlert(bot, update, msg):
	update.message.reply_text(msg)


def main():
	updater = Updater(TOKEN)
	
	dp = updater.dispatcher

	dp.add_handler(CommandHandler("start", start))
	dp.add_handler(CommandHandler("help", help))

	dp.add_handler(CommandHandler("alert", setAlert))

	updater.start_polling()

	


if __name__ == '__main__':
	main()


