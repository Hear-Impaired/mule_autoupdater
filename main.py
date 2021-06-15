import sys

from mule import Mule

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Insufficient arguments")
        sys.exit()
    
    bot = Mule(sys.argv[1], sys.argv[2])
    bot.setArgs()
    bot.run()