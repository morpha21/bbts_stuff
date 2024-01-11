import requests
from bs4 import BeautifulSoup
from datetime import datetime

from datatools import validate
from datatools import extract
from datatools import message

#------------------# variables:
#----------------------------------------------------#
format = "%d/%m/%Y" #--------------------------------# date format we will use;
last_time_checked = "" #-----------------------------# last time the code runned;
novelty_file = 'last_time' #-------------------------# file name;
url = 'https://conhecimento.fgv.br/concursos/bbts23' # url we're scraping data from;
msg = "" #-------------------------------------------# message the bot will sent via telegram.
#----------------------------------------------------#


#----------------------# reads last_time_checked from the file:
#--------------------------------------------------------------------#
with open(novelty_file, 'r') as f: #                                 #
	last_time_checked = f.read().strip()                             #
	last_time_checked = datetime.strptime(last_time_checked, format) #
#--------------------------------------------------------------------#

#---------# makes the request to the url
#---------# and checks if it was successfull.
#---------------------------------------------------#
resp = requests.get(url) #--------------------------# response we get from the request;
if resp.status_code == 200:                         #
	soup = BeautifulSoup(resp.text, 'html.parser')  #
else:                                               # if failed to
	msg = f'failed to obtain data from {url}'       # make the request,
	message.send(msg)                               # sends message and
	exit()                                          # finishes the execution.
#---------------------------------------------------#


div_class = "field__item" #-------------------------# div class we're interested in;
divs = soup.find_all('div', {'class': div_class})#--# the actual divs.


# list of divs with date in it's content
#---------------------------------------#
#----------------------------------------------------------------#
conteudo_divs = [                                                #
	div.text.strip()                                             #
	for div in divs                                              #
	if validate.date(div.text.strip()[:10], format=format)       #
	]                                                            #
#----------------------------------------------------------------#


# gets the most recent dates and it's content
#--------------------------------------------#
#----------------------------------------------------------------#
news = [                                                         #
	( date[:10], extract.novelty(date) )                         #
	for date in conteudo_divs									 #
	if datetime.strptime(date[:10], format) >= last_time_checked #
	and len(extract.novelty(date)) > 0							 #
	]                                                            #
#----------------------------------------------------------------#


# if there are no news,
#----------------------------------#
if len(news) == 0:                 #
	msg = "there are no news..."   #
	message.send(msg)              # sends message, and
	exit()                         # finishes the execution.
#----------------------------------#


# compiles the message and...
#-------------------------------------#
for i in news:                        #
	msg = msg+i[0]+":\t"+i[1]+"\n\n"  #
message.send(msg)                     # ...sends it. 
#-------------------------------------#


#----------------# updates the file with the
#-----------# last time we checked for news:
#--------------------------------------------#
today = datetime.now().strftime("%d/%m/%Y")  #
with open(novelty_file, 'w') as f:           #
	f.write(today)                           #
#--------------------------------------------#