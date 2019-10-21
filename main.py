#Import Section
from smtplib import SMTP
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox
import time
import sys

class Application:
    def __init__(self,master=None):
        self.master = master
        self.Frame = Frame(self.master)
    def main(self):
        self.MF = Frame(self.master)
        self.MF.pack()
        self.mailLBL = Label(self.MF,text="Enter Sender Mail id ")
        self.mailLBL.grid(row = 0,column=0,padx=8,pady=8)
        self.mailEntry = Entry(self.MF)
        self.mailEntry.grid(row = 0,column=1,padx=8,pady=8)
        self.psswdLBL = Label(self.MF,text="Enter Sender Mail Password ")
        self.psswdLBL.grid(row = 1,column=0,padx=8,pady=8)
        self.psswdEntry = Entry(self.MF,show='*')
        self.psswdEntry.grid(row = 1,column=1,padx=8,pady=8)
        self.SubLBL = Label(self.MF,text = "Enter your subject here ")
        self.SubLBL.grid(row=2,column=0,padx=8,pady=8)
        self.SubEntry = Entry(self.MF)
        self.SubEntry.grid(row=2,column=1,padx=8,pady=8)
        self.MessLBL  = Label(self.MF,text = "Enter your message here ")
        self.MessLBL.grid(row = 3,column=0,padx=8,pady=8)
        self.MSG = Text(self.MF,height = 20,width = 50)
        self.MSGScroll = Scrollbar(self.MSG,orient=VERTICAL)
        self.MSG.config(yscrollcommand=self.MSGScroll.set)
        self.MSGScroll.config(command=self.MSG.yview)
        self.MSG.grid(row = 4,column=0,padx=8,pady=8)
        self.WLBL = Label(self.MF,text="Enter mail ids in below Text Area ")
        self.WLBL.grid(row=3,column=1,padx=8,pady=8)
        self.IP = Text(self.MF,height=20,width=50)
        self.TextScroll = Scrollbar(self.IP,orient=VERTICAL)
        self.IP.config(yscrollcommand=self.TextScroll.set)
        self.TextScroll.config(command=self.IP.yview)
        self.IP.grid(row=4,column=1,padx=8,pady=8)
        self.sendBtn = Button(self.MF,text = "Send Mails",command=self.startSend)
        self.sendBtn.grid(row=5,columnspan=2,padx=8,pady=8)
    def startSend(self):
        self.mails = self.IP.get('1.0',END)
        sendList = [mail for mail in self.mails.split('\n') if len(mail)>=5]
        data = {
        'send_id':self.mailEntry.get(),
        'send_psswd':self.psswdEntry.get(),
        'sub':self.SubEntry.get(),
        'msg':self.MSG.get('1.0',END),
        'mails':sendList,
        }
        main(sendData=data)
        messagebox.showinfo("Success","All mails have been sent successfully")

# Function to get the message to email format
def frame_message(sender,reciever,subject,message):
  m_raw = MIMEText(message)
  m_raw['From']=sender #Replace with your maid id
  m_raw['To']=reciever
  m_raw['Subject']=subject
  return m_raw

# Main Function - Program Starts Here
def main(start=0,*,sendData):
    try_Count = 0
    print("Started Sending")
    #Connecting to your mail provider
    server = SMTP('smtp.gmail.com',587) #This is for gmail
    server.starttls() # Encrypt Message
    server.login(sendData['send_id'],sendData['send_psswd']) # Replace with your credintials
    try:
        i = start
        for mail in sendData['mails'][start:]:
            print(mail)
            m = frame_message(sendData['send_id'],mail,sendData['sub'],sendData['msg'])
            # Single Line Code to send mails
            server.sendmail(sendData['send_id'],mail,m.as_string())# Replace with your mail id
            i+=1
    except Exception as e: # Incase of Server Timed out
        try_Count+=1
        #prevent blocking of account
        if try_Count > 10:
            return 
        print(e)
        print("Error Occoured at "+ str(i)+"\n Retrying in 5sec... ")
        time.sleep(5000)
        main(start=i,sendData=sendData)
    return

root = Tk()
root.title("Python Mailer")
app = Application(master=root)
app.main()
root.mainloop()
