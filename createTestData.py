import re
import os
import shutil
import pandas as pd

path = os.path.join(os.getcwd(), 'realTests')
exists = os.path.exists(path)

if not exists:
    os.mkdir(path)
    
test_csv = open('./data/500_picts_satz.csv', 'r')

path = path + '/'


for line in test_csv.readlines():
    line = list(line.split(','))
    fname = line[1]
    src = os.path.join('./images/', fname)
    dst = os.path.join(path, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
