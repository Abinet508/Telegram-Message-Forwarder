from calendar import weekday
from hashlib import new
from telethon import TelegramClient
from datetime import datetime
from flask import jsonify
import csv
import time, os,sys
import csv
from decouple import AutoConfig

"""
```
Save your API_ID and API_HASH in Creditential/.env with the following format:
 API_ID="12345678" 
 API_HASH="12345678abcdefghijklmnopqrstuvwxyz" .

 ```
"""
config = AutoConfig('Credential/.env')
API_ID = config('API_ID')
API_HASH = config('API_HASH')
client = TelegramClient('Credential/anon',API_ID,API_HASH)  # your session will be stored in a file called anon.session
Weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
now = time.localtime()
now1 = time.strftime("%I:%M %p")
weekday_index = now.tm_wday
Today=["Monday"]
client.start()

"""
```
@HandleJobTitle: Handle Job title from channel
@channelname: Channel name where the job title is present
@Mode: Mode of the file, in this case it is either "a+" or "w+"
```
"""
async def HandleJobTitle(channelname,Mode):
  FavList=[]
  Characters=["/","and","or","(",","]
  async with client.takeout() as takeout:
    async for message in takeout.iter_messages(str(channelname), wait_time=10): 
      for mes in  str(message.message).splitlines():
        if "Job Title" in mes:
          newdata=mes.replace("Job Title:"," ").strip().lower()
          for ch in Characters:
            if ch in newdata:
              newdata=mes.replace("Job Title:"," ").strip().split(ch)
              if newdata[0] in FavList or newdata[0]=="internship" or newdata[0]=="intern" or newdata[0]=="paid" or newdata=="":
                pass
              else:
                  FavList.append(newdata[0])
              if newdata[1] in FavList or newdata[0]=="internship" or newdata[0]=="intern" or newdata[0]=="paid" or newdata=="":
                pass
              else:
                FavList.append(newdata[1])
            else:
              if newdata in FavList or newdata=="":
                pass
              else:
                FavList.append(newdata)        
          if newdata in FavList:  
            pass
          else:
            FavList.append(newdata)
  Handlewritecsv(FavList,"JobTitles",Mode)                      

"""
```
@Handlewritecsv: HandleWrite Data to {FileName}.txt file Mode =="w+" or "a+"

```
"""                        
def Handlewritecsv(FileName,FavList,mode,Type=None ):
  if Type ==None:
    for line in FavList:
        file1 = open("{}.txt".format(FileName),"{}".format(mode),encoding="utf-8")
        data= csv.writer(file1,lineterminator="\n")
        data.writerow([line])
        file1.close()
  else:
    file1 = open("{}.txt".format(FileName),"{}".format(mode),encoding="utf-8")
    data= csv.writer(file1,lineterminator="\n")
    data.writerow(FavList)
    file1.close()      

"""
```
@CheckExistancecsv: Check if text Exist in a file trom text file

```
"""    
def CheckExistancecsv(FileName,line,row=None):
  print (line)
  time.sleep(2)
  with open("{}.txt".format(FileName),"r") as data:
    data= csv.reader(data,delimiter=",",lineterminator="\n")
    for lined in data:
      if row==None:
        if lined[0] in line:
          return True
      else:
        if lined[row] in line:
          return True  
    return False    

"""
```
@GetData Retrive Data from {FileName}.txt file and returns it

```
"""        
def GetData(FileName,ReturnType=None,row=None):
  with open("{}.txt".format(FileName),"r") as data:
    data= csv.reader(data,delimiter=",",lineterminator="\n")
    for line in data:
      if ReturnType=="list":
          if line==[]:
            pass
          else:
            return line
      else:      
        if row==None:
          if line==[]:
            pass
          else:
            return line[0]
        else:
          return line[row]           
                
"""
```
@main: Starter Function Starts here

```
"""      
async def Starter():
  date=time.localtime()
  weekday_index=date.tm_wday
  if Weekdays[weekday_index]!=Today[0]:
      await client.send_message("https://t.me/Jemaw123",Weekdays[weekday_index]+" " +datetime.now().strftime("%d-%m-%Y ") +time.strftime("%I:%M %p")) #@https://t.me/Jemaw123 replace destination channel with your channel name
      Today.insert(0,Weekdays[weekday_index])
  NewmessageID=[]
  MessageID=GetData("Senderid_MessageId","list")
  try:
    async with client.takeout() as takeout:
      async for message in takeout.iter_messages(str(MessageID[1]), wait_time=10):
        NewmessageID.append(str(message.id))
        if str(message.id).strip() == str(MessageID[0]).strip():
                break 
        for mes in  str(message.message).splitlines():
          if "Job Title" in mes:
            newdata=mes.replace("Job Title:"," ").strip().lower()
            result=CheckExistancecsv("JobTitles",newdata)
            print(result)
            if result==True:
              await client.forward_messages(entity="https://t.me/Jemaw123",messages=message.id,from_peer=MessageID[1],silent=False)
              time.sleep(3) 
            else:
              continue           
      Handlewritecsv(FileName="Senderid_MessageId",FavList=[NewmessageID[0],MessageID[1]],mode="w+",Type="list")              
  except:
    pass    
"""                    
```
Run the code forever

```  
"""       
while True:
    now = time.localtime()
    now1 = time.strftime("%I:%M %p")
    weekday_index = now.tm_wday
    if Weekdays[weekday_index]=="Sunday" or now1<="07:00 AM" and now1>="07:22 PM":
        time.sleep(3600)
        pass
    elif Weekdays[weekday_index]=="Saturday" : 

      with client:
          client.loop.run_until_complete(Starter())  
          time.sleep(3600)        
    else:
      with client:
          client.loop.run_until_complete(Starter())  
          time.sleep(300)      