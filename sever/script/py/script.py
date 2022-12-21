import telegram
bot = telegram.Bot(token='5948498812:AAFoXd2FSxN4ROA-3MHB7QIB34hYwHyURGg')
print(bot.get_me())
import os
if os.access("/happa/backup/tmp/backup.zip", os.F_OK):
    file0 = '/happa/backup/tmp/backup.zip'
    bot.send_document(chat_id=-1001808912022, document=open(file0, "rb"))
    for i in range(1, 100):
        filename = "/happa/backup/tmp/backup.z%02d" % (i, )
        if os.access(filename, os.F_OK):
            bot.send_document(chat_id=-1001808912022,
                              document=open(filename, "rb"))
        else:
            break