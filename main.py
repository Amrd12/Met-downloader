from cgitb import html
import requests
from bs4 import BeautifulSoup
import yt_dlp
import os
import json
import file
import server
import down
print("licence saved from amrd12 follow me on github : https://github.com/Amrd12")
#first need to check code version from server but save to later
#    file(get user pas fpath)  server( check(user&&pas)getand check and send(creddit))  down(user &pas &fpath &url)
s = requests.session()
file.create_file()# create file
info = file.get_info() # get user password info
user = info["user"] ; pas = info["pas"] ; fpath = info["fpath"]
futur = input("do you want to save data for future use? y/n ")
file.save( user ,pas  , fpath,futur )#save info to file
rem = input("do you want to remove save file? y/n ")# remove file
if rem == "y":   file.remove()
# now I have user pas fpath

url = input("please enter url to download from https://els-engmet.com/")#input url
fpath=fpath+"/"+str(url[31:-1])
if str(os.path.exists(fpath)) =="False":
 os.mkdir(fpath)# create folder in celected path
fpath=fpath+"/"+str(url[31:-1])# path to download and for text file
list = down.list(user , pas ,url, fpath, s)
download = input("do you want to down videos y/n ")
if download == "y":
  down.down(fpath , url ,list)
