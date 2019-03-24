bot = ChatBot('Friend') #create the bot
bot.set_trainer(ListTrainer) # Teacher
#bot.train(conv) # teacher train the bot
for knowledeg in os.listdir('base'):
	BotMemory = open('base/'+ knowledeg, 'r').readlines()
	bot.train(BotMemory)