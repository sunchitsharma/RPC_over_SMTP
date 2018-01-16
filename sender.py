import smtplib
import time
import imaplib
import email
import datetime

# Initiating SMTP
s = smtplib.SMTP('students.iiit.ac.in', 587)
# security Thing
s.starttls()
# login
s.login("sunchit.sharma@students.iiit.ac.in", "G@te2017")

# Data input that needs to be mailed
x=raw_input("Message to be sent : ")

# Identity of current message : Goes as subject
hash = datetime.datetime.now()

########################################## MESSAGE WITH HASH ###############################################
message="""From: From Sunchit Sharma <sunchit.sharma@students.iiit.ac.in>
To: To Person <sunchit@zoho.com>
MIME-Version: 1.0
Content-type: text/html
Subject:"""+str(hash)+"""

@!!!!@
"""+x
############################################## END OF MESSAGE ##############################################

# Send the mail
s.sendmail("sunchit.sharma@students.iiit.ac.in", "sunchit@zoho.com", message)
# DEBUG
print 'SENT'
# End this session
s.quit()

############################################## FETCHING REPLY ############################################### 

while(True):
    try:
        #initiate the smtp again
        mail = imaplib.IMAP4_SSL("imap.zoho.com")
        # Login
        mail.login("sunchit@zoho.com","G@te2017")
        # Goto inbox
        mail.select('Inbox')
        # fetching all mails
        type, data = mail.search(None, 'ALL')
        # Fetching mail id's
        mail_ids = data[0]
        id_list = mail_ids.split()
        # Last mail id
        latest_email_id = int(id_list[-1])
        #Fetching the last mail
        typ, data = mail.fetch(latest_email_id, '(RFC822)' )


        for response_part in data:
            if isinstance(response_part, tuple):
                #Extracting message
                msg = email.message_from_string(response_part[1])
                email_subject = msg['subject']
                # if subject != Response
                print "I AM NOW WAITING FOR : "+('R'+str(hash))
                if str(email_subject)!=('R'+str(hash)):
                    break
                email_from = msg['from']
                email_message = msg['message']
                mess=str(msg)
                # Find the answer
                ind=mess.index('@!!!!@')
                data_found=mess[ind+6:]
                print 'From : ' + email_from + '\n'
                print 'Subject : ' + email_subject + '\n'
                # Print answer
                print 'Message :' + data_found
                # Exit
                exit(0)

    except Exception, e:
        print str(e)
