# IMPORTS
import smtplib
import time
import imaplib
import email
import sendmail as sm

# Read mails and reply for the query
def readmail():
    # To track new mails
    count =0;
    # Running Server
    while(True):
        try:
            # Initiating the imap request
            mail = imaplib.IMAP4_SSL("imap.zoho.com")
            # Logging in to recieve mails
            mail.login("sunchit@zoho.com","G@te2017")
            mail.select('Inbox')
            # recieving all data
            type, data = mail.search(None, 'ALL')
            # Fetching the id's
            mail_ids = data[0]
            # if new mails recieved
            if(count != len(mail_ids)):
                # Increase count
                count =len(mail_ids)
                id_list = mail_ids.split()
                latest_email_id = int(id_list[-1])
                # Read the last mail
                typ, data = mail.fetch(latest_email_id, '(RFC822)' )

                for response_part in data:
                    if isinstance(response_part, tuple):
                        msg = email.message_from_string(response_part[1])
                        email_subject = msg['subject']
                        if email_subject[0]=='R':
                            break
                        mess=str(msg)
                        # Extracting Data
                        ind=mess.index('@!!!!@')
                        data_found=mess[ind+6:]
                        # TESTING MESSAGES
                        print "##################################"
                        print 'Subject :' + email_subject + '\n'
                        print 'Message :' + data_found
                        print "##################################"
                        dict_of_mess=data_found.split();
                        # Calculate the answer : in this case sum
                        sum=0
                        for k in dict_of_mess:
                            sum=sum+int(k)

                        ########################### RESPONSE ###############################
                        ans_to_return=str(sum)
                        sm.sendmail("R"+email_subject,"@!!!!@ "+ans_to_return)
                        #DEBUG
                        print "********************"
                        print "Sent the reply back"
                        print "********************"

        except Exception, e:
            if(str(e)!="global name 'message' is not defined"):
                sm.sendmail("R"+email_subject,"@!!!!@ "+str(e))
            print str(e)


readmail()
