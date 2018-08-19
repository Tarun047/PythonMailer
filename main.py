#Import Section
from smtplib import SMTP
from email.mime.text import MIMEText
from tkinter import *
from tkinter import messagebox

#Global Variables

#Replace Send list with desired mail ids strings sepereated by commas

message = """
Thank you for showing interest to attend the Python workshop.


Please join the whatsapp group for further updates.
https://chat.whatsapp.com/1kI7k656Y9P4fQocYwQrir


Ignore if already joined
"""

class Application:
    def __init__(self,master=None):
        self.master = master
        self.Frame = Frame(self.master)
    def main(self):
        self.MF = Frame(self.master)
        self.MF.pack()
        self.WLBL = Label(self.MF,text="Enter mail ids: ")
        self.WLBL.grid(row=0,column=0,padx=8,pady=8)
        self.IP = Text(self.MF,height=20,width=50)
        self.TextScroll = Scrollbar(self.IP,orient=VERTICAL)
        self.IP.config(yscrollcommand=self.TextScroll.set)
        self.TextScroll.config(command=self.IP.yview)
        self.IP.grid(row=1,column=0,padx=8,pady=8)
        self.sendBtn = Button(self.MF,text = "Send Mails",command=self.startSend)
        self.sendBtn.grid(row=2,column=0,padx=8,pady=8)
    def startSend(self):
        self.mails = self.IP.get('1.0',END)
        sendList = [mail for mail in self.mails.split('\n') if len(mail)>=5]
        main(sendList = sendList)
        messagebox.showinfo("Success","All mails have been sent successfully")

# Function to get the message to email format
def frame_message(recv):
  m_raw = MIMEText(message)
  m_raw['From']="your_mail_id" #Replace with your maid id
  m_raw['To']=recv
  m_raw['Subject']="Invite to Python Workshop Whatsapp Group"
  return m_raw

# Main Function - Program Starts Here
def main(start=0,*,sendList):
    print("Started Sending")
    #Connecting to your mail provider
    server = SMTP('smtp.gmail.com',587) #This is for gmail
    server.starttls() # Encrypt Message
    server.login('your_mail_id','your_password') # Replace with your credintials
    try:
        i = start
        for mail in sendList[start:]:
            print(mail)
            m = frame_message(mail)
            # Single Line Code to send mails
            server.sendmail("your_mail_id",mail,m.as_string())# Replace with your mail id
            i+=1
    except Exception as e: # Incase of Server Timed out
        print(e)
        print("Error Occoured at "+ str(i)+"\n Retrying ... ")
        main(start=i,sendList=sendList)
    return

root = Tk()
root.title("WS Mailer")
app = Application(master=root)
app.main()
root.mainloop()
