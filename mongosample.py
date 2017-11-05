#import os 
#dirlist=os.listdir('/home/swathi')
#from pprint import pprint
#pprint(dirlist)

import os,time
from datetime import datetime
for dir, subdir, files in os.walk('/home/swathi/Documents'):
    for file in files:
 	a = os.stat(os.path.join(dir,file))
        print os.path.join(dir, file) +","+ time.ctime(a.st_atime)+","+time.ctime(a.st_ctime)


