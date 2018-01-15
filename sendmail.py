import smtplib
def sendmail(subject,message):

	# initiate SMTP session
	s = smtplib.SMTP('students.iiit.ac.in', 587)

	# start TLS for security
	s.starttls()

	# Authentication
	s.login("sunchit.sharma@students.iiit.ac.in", "G@te2017")

	# message to be sent

	message="""From: sunchit.sharma@students.iiit.ac.in\nSubject: """+subject+"""

	:MESSAGE:

	"""+message

	# sending the mail
	s.sendmail("sunchit.sharma@students.iiit.ac.in","sunchit@zoho.com", message)

	print 'SENT'

	# terminating the session
	s.quit()
