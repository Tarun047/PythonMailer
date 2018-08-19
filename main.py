#Import Section
from smtplib import SMTP
from email.mime.text import MIMEText

#Global Variables

#Replace Send list with desired mail ids strings sepereated by commas
sendList = ["some_mail_id1@some.com","some_mail_id2@some.com",]
message = """
Thank you for showing interest to attend the Python workshop.


Please join the whatsapp group for further updates.
https://chat.whatsapp.com/1kI7k656Y9P4fQocYwQrir


Ignore if already joined
"""

# Function to get the message to email format
def frame_message(recv):
  m_raw = MIMEText(message)
  m_raw['From']="your_mail_id" #Replace with your maid id
  m_raw['To']=recv
  m_raw['Subject']="Invite to Python Workshop Whatsapp Group"
  return m_raw

# Main Function - Program Starts Here
def main(start=0):
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
        main(start=i)
    return

main()
