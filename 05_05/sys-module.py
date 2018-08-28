import sys
import datetime
 
if len(sys.argv) > 3:
    x = int(sys.argv[1])
    y = int(sys.argv[2])
    z = int(sys.argv[3])
    print("{}:{}".format(datetime.datetime.now(), x+y+z))
