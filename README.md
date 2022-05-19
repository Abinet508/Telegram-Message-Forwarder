#  ``` Telegram-Message-Forwarder   ```

> Forward job post messages from Freelance Ethiopia channel based on your job titles preference to a group or telegram member

### ``` Files And Folder ```

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------

- Create A Folder Credential in main Folder where forwardcript.py resides
- create .env file in Credential Folder and put you api and hash in it, you can get your api id and api hash from [here](https://my.telegram.org/auth?to=apps)
- Put your Api id and hash in Credential/.env
    -API_ID =your Api id 
     API_HASH= your api hash
     
- when you run the code for the first time it  will ask you put your phone  number and  code after it will create your session and stores  it in Credential Folder you created     

- Senderid_MessageId.txt stores Message Id (last  Id it will  updated when ever a new post is released you can get  message id by Right clicking on the message and  copying message post link and paste  it  somewhere it will look like this  "https://t.me/freelance_ethio/32524", "32524" this is your message id )  Sender link in this case freelance telegram link you can replace it with any channel as long as you are  member of that channel.  

- JobTitles.txt all the job titles(in lower case) will be stored here separated by new line.

- requirements.txt prerequisites to use this script install it using ```pip install -r requirements.txt```

----------------------------------------------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------------------------------------------
