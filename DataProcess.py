import shutil
import sys
import os
import re

happy_dir = os.path.join('./train/', 'happy')
anger_dir = os.path.join('./train/', 'anger')
fear_dir = os.path.join('./train/', 'fear')
neutral_dir = os.path.join('./train/', 'neutral')
sad_dir = os.path.join('./train/', 'sad')
#disgust_dir = os.path.join('./train/', 'disgust')
#surprise_dir = os.path.join('./train/', 'surprise')
#contempt_dir = os.path.join('./train/', 'contempt')

exists = os.path.exists(happy_dir)

if not exists:
    #os.mkdir(contempt_dir)
    #os.mkdir(surprise_dir)
    #os.mkdir(disgust_dir)
    os.mkdir(sad_dir)
    os.mkdir(neutral_dir)
    os.mkdir(fear_dir)
    os.mkdir(anger_dir)
    os.mkdir(happy_dir)
labels_file = open('./data/legend.csv', 'r')

fnames = os.listdir('./images')

for line in labels_file.readlines():
    line = list(line.split(','))
    line[2] = re.sub(r'\n', '', line[2])
    src = os.path.join('./images/', line[1])
    infile = os.path.isfile(src)
    if infile:
        if line[2] == 'happiness' or line[2] == 'HAPPINESS':
            dst = os.path.join('./train/happy', line[1])
            shutil.copyfile(src, dst)
        elif line[2] == 'anger' or line[2] == 'ANGER':
            dst = os.path.join('./train/anger', line[1])
            shutil.copyfile(src, dst)
        elif line[2] == 'fear' or line[2] == 'FEAR':
            dst = os.path.join('./train/fear', line[1])
            shutil.copyfile(src, dst)
        elif line[2] == 'neutral' or line[2] == 'NEUTRAL':
            dst = os.path.join('./train/neutral', line[1])
            shutil.copyfile(src, dst)
        elif line[2] == 'sadness' or line[2] == 'SADNESS':
            dst = os.path.join('./train/sad', line[1])
            shutil.copyfile(src, dst)
        elif line[2] == 'disgust' or line[2] == 'DISGUST':
            pass
            #dst = os.path.join('./train/disgust', line[1])
            #shutil.copyfile(src, dst)
        elif line[2] == 'surprise' or line[2] == 'SURPRISE':
            pass
            #dst = os.path.join('./train/surprise', line[1])
            #shutil.copyfile(src, dst)
        elif line[2] == 'contempt' or line[2] == 'CONTEMPT':
            pass
            #dst = os.path.join('./train/contempt', line[1])
            #shutil.copyfile(src, dst)
        else:
            print("File not processed " + line[1] + " the emotion is " + line[2])
