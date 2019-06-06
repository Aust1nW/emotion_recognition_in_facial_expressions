import shutil
import sys
import os
import re

happy_dir = os.path.join('./train/', 'happy')
os.mkdir(happy_dir)
anger_dir = os.path.join('./train/', 'anger')
os.mkdir(anger_dir)
fear_dir = os.path.join('./train/', 'fear')
os.mkdir(fear_dir)
neutral_dir = os.path.join('./train/', 'neutral')
os.mkdir(neutral_dir)
sad_dir = os.path.join('./train/', 'sad')
os.mkdir(sad_dir)
disgust_dir = os.path.join('./train/', 'disgust')
os.mkdir(disgust_dir)
surprise_dir = os.path.join('./train/', 'surprise')
os.mkdir(surprise_dir)
contempt_dir = os.path.join('./train/', 'contempt')
os.mkdir(contempt_dir)
labels_file = open('./data/legend.csv', 'r')


for line in labels_file.readlines():
    line = list(line.split(','))
    line[2] = re.sub(r'\n', '', line[2])
    src = os.path.join('./images/', line[1])
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
        dst = os.path.join('./train/disgust', line[1])
        shutil.copyfile(src, dst)
    elif line[2] == 'surprise' or line[2] == 'SURPRISE':
        dst = os.path.join('./train/surprise', line[1])
        shutil.copyfile(src, dst)
    elif line[2] == 'contempt' or line[2] == 'CONTEMPT':
        dst = os.path.join('./train/contempt', line[1])
        shutil.copyfile(src, dst)
    else:
        print("File not processed " + line[1] + " the emotion is " + line[2])
