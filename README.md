# keylogger-withMAILservice   ONLY FOR WINDOWS operating system
an advanced keylogger which mails you the keystrokes when the victim press 'Enter'

-------------------------------------------------------------------------------------------------------------------------------------------------------------------
          IMPORTANT_INFORMATION_ABOUT_THE CODE  
   for your own security you have to activate less security app in your gmail.
   And give your less secured password in the code {otherwise there will be an error}.
   ENABLE THE LESS_SECURE_APP {for your own privacy & security}  watch the video : 'https://www.youtube.com/watch?v=pBtQ4IHkuQE'
-------------------------------------------------------------------------------------------------------------------------------------------------------------------


FIRSTLY, you need to enter your credentials in the code to get the keylogger file

![Screenshot (12)](https://user-images.githubusercontent.com/92925838/178463520-2f3a74e4-93e2-4be6-b4c1-e882b1a2544e.png)

* In 24th & 25th line in the above picture --> provide your gmail-id & less secure app-password. (to send the keylogger file from the victim's pc)
* In 30th line in the above picture --> provide your mail-id ...that is the mail-id you will get the keylogger file

AFTER ENTERING THE CREDENTIALS :
  * you need to rename the file extension from "py to pyw"  (for hiding the cmd window & for continues working)
  
               example : mailing_keylogger.pyw
 ![Screenshot (14)](https://user-images.githubusercontent.com/92925838/178469376-a70ac2c9-e35f-4006-82b1-b461d77e1857.png)
  
 * IF YOU WANT TO CONVERT THE pyw FILE TO exe :
 install nuitka software to compile the pyw file to exe file
 
                 pip install Nuitka
                 nuitka -h 
 
 * HOW TO INSTALL NUITKA SOFTWARE : 'https://www.youtube.com/watch?v=Yq3Qrm1CtQ0'
 
 AFTER INSTALLING NUITKA :
                 
                 py -m nuitka --mingw64 'filename.pyw' --standalone --onefile
                 
                 example : py -m nuitka --mingw64 mailing_keylogger.pyw --standalone --onefile
                 
* SCREENSHOT of recieved MAIL from mailing_keylogger :

![scrshotforkeyloggergit](https://user-images.githubusercontent.com/92925838/178474076-ff19ad2a-0648-4182-989e-609efdec33da.jpg)

* working :
first it creates a folder in c:\ drive and save the keylogger file as sys/log in a temp folder.After sending the mail the folder automatically deletes everything.
There wont be anything to trace.
folder creating path : c:/temp/sys.log


