# Code to get the qrcodes for different registration numbers,
# Save it and enter the required values in database

import requests
import shutil
import json
import hashlib
import MySQLdb as db
import os

# Credentials
HOST = "103.27.87.65"
PORT = 3306
USER = "esummiti_reg"
PASSWORD = "!nPiUFjr)&NE"
DB = "esummiti_register"

# Loop for the no of qr codes required (ex:500 here)
for i in range(1,501):

	# Basic info
	# start

	REG_NO="1801"+"{0:0=3d}".format(i)
	CODE = hashlib.md5(REG_NO.encode('utf-8')).hexdigest()

	BASE="http://ca.e-summit-iitbbs.com/register/register.php?p="
	URL_DATA = BASE+CODE

	#print(URL_DATA)

	# end

	# API endpoint (using get method)
	# start

	URL = "http://api.qrserver.com/v1/create-qr-code/"

	PARAMS = {
		'data':URL_DATA,
		'size':"300x300",
		'color':"0-0-255"
	}

	import os
	if not os.path.exists('qrcodes'):
	    os.makedirs('qrcodes')

	r = requests.get(url = URL, params = PARAMS, allow_redirects=True)
	open('qrcodes/'+REG_NO+".png", 'wb').write(r.content)

	# end

	# Making an sql insert command
	# start

	sql_query="INSERT INTO `qr_code`(`id`, `normal_value`, `hashed`) VALUES (\'NULL\',\'%s\',\'%s\');" % (REG_NO, CODE)
	print (sql_query)

	#end

# Could also write a piece of code to connect to remote sql and run the command.
# Else you can copy paste the ouput of the code later.
