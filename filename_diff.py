# -*- coding: utf-8 -*-

import os
from datetime import datetime

def fild_all_files(directory):
    for root,dirs,files in os.walk(directory):
        yield root
        for file in files:
            n='\n'
            yield n
            yield os.path.join(root,file)

filename = str(datetime.now().year) +"_" + str(datetime.now().month)+"_"+str(datetime.now().day)+".txt"
fileobj = open(filename,'wt')

for file in fild_all_files('/'):
   fileobj.write(file)
fileobj.close()
