import sys
import time
import datetime
import telepot
import requests
from bs4 import BeautifulSoup
from urllib.request import urlopen

def handle(msg):
    chat_id=msg['chat']['id']
    sentcommand=msg['text']
    error = "Sorry command not found. Type 'Help' for possible commands"
    
    commandlist = sentcommand.split(" ")
    command = commandlist[0]
    
    
    print ('Got command: %s' % command)
    
    if command == 'Help' or command == 'help':
        bot.sendMessage(chat_id, "Below are the possible commands \n 'Time' : for current time \n 'Movie <year> <Number of items>' : Lists top <number of items> movies from the year <Year>")
    
    elif command == 'time' or command == 'Time':
        bot.sendMessage(chat_id, str(datetime.datetime.now()))
        
    elif command == 'movie' or command == 'Movie':
        year = commandlist[1]
        count = int(commandlist[2])
        names = []
        
        parturl = "https://www.imdb.com/search/title?title_type=feature&release_date="
        range1 = "-01-01,"
        range2 = "-12-31&groups=top_1000&count=250&sort=user_rating,desc&languages=en"
        
        page = parturl+year+range1+year+range2
        print(page)
        
        uclient = urlopen(page)
        page_html = uclient.read()
        uclient.close()

        soup = BeautifulSoup(page_html,'html.parser')
        
        card_list_items = soup.find_all('div',{'class':'lister-item mode-advanced'})
        
        for i in range (count):
            element = card_list_items[i]
            name = element.h3.a.text
            bot.sendMessage(chat_id, str(name))
    
    else:
        bot.sendMessage(chat_id, str(error))
        
bot=telepot.Bot('713477296:AAHecCYvDFIQNqvscSyrpx_pqgBDA3I0meI')
bot.message_loop(handle)
print ('I am listening ...')

while 1:
    time.sleep(10)

