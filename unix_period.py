import datetime
import sys
import time


#Press ctrl c to interrupt the unix_countup function.

def unix_countup(party=1500000000, moment=0.01, offset=0):
    '''Unix Time Stamp CountUp'''
    now = round((datetime.datetime.utcnow() - datetime.datetime(1970, 1, 1)).total_seconds() + offset, 2)
    while now < party:
        print("{:,}".format(now)),'\r',
        now+=moment if moment!=0 else now;
        sys.stdout.flush()
        time.sleep(moment)








###If text is marked in the command-line, then the function pauses and does not resync time. I will upgrade this file in the future, so the time will resync after text is marked.
###Note: The counter ascends. I might add a parameter to the unix_countup() that allows for ascending or descending the counter.
