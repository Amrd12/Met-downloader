import os 
import json
#def ver():
import server
def create_file(): 
 if str(os.path.exists('info.json')) =="False":
   creat =  open("info.json","w")
   dic = {"futur" : "n"}
   creat.write(json.dumps(dic))
   creat.close()

def get_info():   
 file = open("info.json" , "r")
 user_info = json.loads(file.read())
 file.close()
 if user_info["futur"] == "y":
  user =   user_info["user"]
  pas =   user_info["pass"]
  fpath =   user_info["fpath"]
 else:
  user = input("enter user name ")
  pas = input("enter password ")
  if server.checkmet(user , pas) != "false":
    print("wroung user or pas")
    file.remove()
    os._exit()
  fpath = input("enter the path to save videos ")
 return { "user" : user ,   "pas": pas ,   "fpath": fpath}


def save(user,pas,fpath, futur):
  file = open("info.json" , "r")
  user_info = json.loads(file.read())
  file.close()  
  if futur =="y":
    user_info.update(   {"user"  :  user}     )
    user_info.update(   {"pass"  :  pas}     )
    user_info.update(   {"fpath"  :  fpath}     )
    user_info.update(   {"futur"  :  "y"}     )
    save =  open("info.json","w")
    save.write(json.dumps(user_info))
    save.close()

def remove():
    os.remove("info.json")
    

