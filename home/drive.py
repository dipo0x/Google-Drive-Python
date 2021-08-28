from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive
import random

gauth = GoogleAuth()           
drive = GoogleDrive(gauth) 

upload_file_list = ['Kizz-Daniel-Wedding-Day-(JustNaija.com).mp3']
for upload_file in upload_file_list:

	numberList = [13, 32, 73, 54, 65, 63, 49, 38, 19, 47, 23, 20, 50, 
	1000, 650, 159, 18, 0 , 850, 560, 750, 673, 439, 639, 829, 12, 
	85, 299, 749, 283, 292, 189, 193, 879, 183]
	id = random.choice(numberList)

	gfile = drive.CreateFile({'parents': [{'id': '16WA6Upm9cuKQnglvd_tHmb6t_il5gdl3'}]})
	# Read file and set it as the content of this instance.
	gfile.SetContentFile(upload_file)
	gfile.Upload() # Upload the file.