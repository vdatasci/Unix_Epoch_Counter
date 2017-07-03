import datetime
import sys
import time
import argparse
import unix_period as up


#For the help file:
#go to the command-line,
#change directory (cd) to the folder where this file is located,
#type the letters
#'python' unix_counter.py -h
#or
#'python' unix_counter.py --help

parser=argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
    description='''This Python script contains a function called unix_countup(), which counts up to a unix time. \r 
                    Unix time (also known as POSIX time or epoch time) is a system for describing instants in time, defined as the number of seconds that have elapsed since 00:00:00 Coordinated Universal Time (UTC), Thursday, 1 January 1970, minus the number of leap seconds that have taken place since then.


COMMAND-LINE EXAMPLE (1):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py 1500000000 0.01 0


COMMAND-LINE EXAMPLE (2):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py -p 1500000000 -m 0.01 -o 0


COMMAND-LINE EXAMPLE (3):
 F:
 cd F:\\Python\\Projects\\Epoch
 python unix_counter.py --party 1500000000 --moment 0.01 --offset 0
---------------------''',
    epilog="""
---------------------
DETAILS ABOUT AUTHOR:
https://www.JoshingAroundBlog.WordPress.com/
https://www.LinkedIn.com/in/Josh-Voss
https://www.Twitter.com/VossDataScience
""")
#NOTE (fix): dashes make the argument optional, not required


if __name__ == '__main__':
    up.unix_countup(1500000000, 0.1, 0)



while True:
    try:
        counter = up.unix_countup(int(sys.argv[1]), float(sys.argv[2]), int(sys.argv[3]),)
        counter
    except:
        parser.add_argument('-p', '--party', nargs='*', type=int, default=1500000000, help='The unix time for the party!  Default:[party=1500000000]')
        parser.add_argument('-m', '--moment', nargs='*', type=float, default=0.01, help='The moment generator for the unix time counter.  Default:[moment=0.01]')
        parser.add_argument('-o','--offset', nargs='*', type=float, default=0, help='The place out of line from the actual time.  Default:[offset=0]')
        args=parser.parse_args()
        
        if args.party and args.moment and args.offset:
            counter = up.unix_countup(args.party[0], args.moment[0], args.offset[0])
            counter
        #If you want to exit the counter, then press ctrl c

