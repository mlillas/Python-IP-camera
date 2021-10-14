import os
import ftplib
from config import *

image00 = "image00.jpg"
image01 = "image01.jpg"
image02 = "image02.jpg"
image03 = "image03.jpg"
image04 = "image04.jpg"
image05 = "image05.jpg"
image06 = "image06.jpg"
image07 = "image07.jpg"
image08 = "image08.jpg"
image09 = "image09.jpg"
image10 = "image10.jpg"
image11 = "image11.jpg"
image12 = "image12.jpg"
image13 = "image13.jpg"
image14 = "image14.jpg"
image15 = "image15.jpg"
image16 = "image16.jpg"
image17 = "image17.jpg"
image18 = "image18.jpg"
image19 = "image19.jpg"
image20 = "image20.jpg"
image21 = "image21.jpg"
image22 = "image22.jpg"
image23 = "image23.jpg"

os.chdir('images')


def rename():
    try:
        latest = os.path.exists("latest.jpg")
    except:
        latest = False
        print("latest.jpg doesn not exist")

    if(latest):
        try:
            os.remove(image23)
        except:
            print(image23 + " was not found!")
        try:
            os.rename(image22, image23)
        except:
            print(image22 + " was not found!")
        try:
            os.rename(image21, image22)
        except:
            print(image21 + " was not found!")
        try:
            os.rename(image20, image21)
        except:
            print(image20 + " was not found!")
        try:
            os.rename(image19, image20)
        except:
            print(image19 + " was not found!")
        try:
            os.rename(image18, image19)
        except:
            print(image18 + " was not found!")
        try:
            os.rename(image17, image18)
        except:
            print(image17 + " was not found!")
        try:
            os.rename(image16, image17)
        except:
            print(image16 + " was not found!")
        try:
            os.rename(image15, image16)
        except:
            print(image15 + " was not found!")
        try:
            os.rename(image14, image15)
        except:
            print(image14 + " was not found!")
        try:
            os.rename(image13, image14)
        except:
            print(image13 + " was not found!")
        try:
            os.rename(image12, image13)
        except:
            print(image12 + " was not found!")
        try:
            os.rename(image11, image12)
        except:
            print(image11 + " was not found!")
        try:
            os.rename(image10, image11)
        except:
            print(image10 + " was not found!")
        try:
            os.rename(image09, image10)
        except:
            print(image09 + " was not found!")
        try:
            os.rename(image08, image09)
        except:
            print(image08 + " was not found!")
        try:
            os.rename(image07, image08)
        except:
            print(image07 + " was not found!")
        try:
            os.rename(image06, image07)
        except:
            print(image06 + " was not found!")
        try:
            os.rename(image05, image06)
        except:
            print(image05 + " was not found!")
        try:
            os.rename(image04, image05)
        except:
            print(image04 + " was not found!")
        try:
            os.rename(image03, image04)
        except:
            print(image03 + " was not found!")
        try:
            os.rename(image02, image03)
        except:
            print(image02 + " was not found!")
        try:
            os.rename(image01, image02)
        except:
            print(image01 + " was not found!")
        try:
            os.rename(image00, image01)
        except:
            print(image00 + " was not found!")

        os.rename("latest.jpg", image00)


def ftpUpload():
    #session = ftplib.FTP(FTP_url+FTP_port, FTP_username, FTP_passwd)
    session = ftplib.FTP(FTP_url)

    try:
        session.login(user=FTP_username, passwd=FTP_passwd)
    except:
        print('Login Failed!')

    try:
        session.cwd('cam')
    except:
        session.mkd('cam')
        session.cwd('cam')

    for filename in os.listdir():
        if filename.endswith('.jpg'):
            file = open(filename,'rb')
            session.storbinary('STOR ' + filename, file)
        else:
            continue
    
    try:
        file.close()
    except:
        print("No files found!!!")

    session.quit()
    print('Upload Finished Successfully!')
