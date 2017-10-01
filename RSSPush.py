from os import system
import smtplib
import unidecode
import config

system('python rss.py >> rssfeed.txt')
str = open('rssfeed.txt','r').read()

message	= """From: {}
To: {}
Subject: Your daily RSS feed!
	
{}""".format(config.sender, config.reciever, str)
message = unidecode.unidecode(u'{}'.format(message))

server = smtplib.SMTP(config.server, config.port)
server.connect(config.server, config.port)
server.ehlo()
server.starttls()
server.ehlo()
server.login(config.sender, config.password)
server.sendmail(config.sender, config.reciever, message)
server.quit()

open("rssfeed.txt","w").close()
