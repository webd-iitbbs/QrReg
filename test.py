import requests
import shutil
import json
import hashlib
import MySQLdb as db

HOST = "103.27.87.65"
PORT = 3306
USER = "esummiti_reg"
PASSWORD = "!nPiUFjr)&NE"
DB = "esummiti_register"

for i in range(1,2):

	REG_NO="1801"+str(i);
	CODE = hashlib.md5(REG_NO.encode('utf-8')).hexdigest()

	BASE="http://ca.e-summit-iitbbs.com/register/register.php?p="
	URL_DATA = BASE+CODE

	print(URL_DATA)

	URL = "http://api.qrserver.com/v1/create-qr-code/"

	PARAMS = {
		'data':URL_DATA,
		'size':"500x500",
		'color':"0-0-255"
	}

	r = requests.get(url = URL, params = PARAMS, allow_redirects=True)
	open(REG_NO+".png", 'wb').write(r.content)

    # try:
    #     connection = db.Connection(host=HOST, port=PORT,user=USER, passwd=PASSWORD, db=DB)
    #     dbhandler = connection.cursor()
    #     dbhandler.execute("INSERT INTO qr_code VALUES('NULL', 'REG_NO', 'CODE')")
    # except Exception as e:
    #     print (e)
    # finally:
    #     connection.close()
