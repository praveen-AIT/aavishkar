import time
import urllib
import re
import urllib2
import cookielib
from getpass import getpass
import os
import sys

def message(num1, mess):
	username = '7798611564'
	passwd = 'pp123456'
	message = "Accident occured and victim is being taken to "+str(mess)
	number = num1

	message = "+".join(message.split(' '))


	    #Logging into the SMS Site

	url = 'http://site24.way2sms.com/Login1.action?'

	data = 'username='+username+'&password='+passwd+'&Submit=Sign+in'
	    

	    #For Cookies:

	cj = cookielib.CookieJar()

	opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))


	    # Adding Header detail:

	opener.addheaders = [('User-Agent','Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/37.0.2062.120 Safari/537.36')]


	try:

	    usock = opener.open(url, data)

	except IOError:

	    print "\n[-] CAN NOT CONNECT TO SERVER...CHECK USERNAME AND PASSWORD AND INTERNET CONNECTION ALSO"

	    raw_input("\n[-] PRESS ENTER TO EXIT")

	    sys.exit(1)



	jession_id = str(cj).split('~')[1].split(' ')[0]

	send_sms_url = 'http://site24.way2sms.com/smstoss.action?'

	send_sms_data = 'ssaction=ss&Token='+jession_id+'&mobile='+number+'&message='+message+'&msgLen=136'

	opener.addheaders = [('Referer', 'http://site25.way2sms.com/sendSMS?Token='+jession_id)]
	    

	try:

	    sms_sent_page = opener.open(send_sms_url,send_sms_data)

	except IOError:

	    print "\n[-] ERROR WHILE SENDING THE SMS...PLEASE UPDATE THE CONTACT LIST"

	    

	    sys.exit(1)

	print "\n\n\t[+] SMS SENT"

