import os, shutil, sys, re

happy_val = os.path.join('./validation/', 'happy')
happy_train = os.path.join('./train/', 'happy')
anger_val = os.path.join('./validation/', 'anger')
anger_train = os.path.join('./train/', 'anger')
fear_val = os.path.join('./validation/', 'fear')
fear_train = os.path.join('./train/', 'fear')
neutral_val = os.path.join('./validation/', 'neutral')
neutral_train = os.path.join('./train/', 'neutral')
sad_val = os.path.join('./validation/', 'sad')
sad_train = os.path.join('./train/', 'sad')
#disgust_val = os.path.join('./validation/', 'disgust')
#disgust_train = os.path.join('./train/', 'disgust')
#surprise_val = os.path.join('./validation/', 'surprise')
#surprise_train = os.path.join('./train/', 'surprise')
#contempt_val = os.path.join('./validation/', 'contempt')
#contempt_train = os.path.join('./train/', 'contempt')

exists = os.path.exists(happy_val)

if not exists:
    os.mkdir(happy_val)
    os.mkdir(anger_val)
    os.mkdir(fear_val)
    os.mkdir(neutral_val)
    os.mkdir(sad_val)
    #os.mkdir(disgust_val)
    #os.mkdir(surprise_val)
    #os.mkdir(contempt_val)

happy_size = len(os.listdir(happy_train))
anger_size = len(os.listdir(anger_train))
fear_size = len(os.listdir(fear_train))
neutral_size = len(os.listdir(neutral_train))
sad_size = len(os.listdir(sad_train))
#disgust_size = len(os.listdir(disgust_train))
#surprise_size = len(os.listdir(surprise_train))
#contempt_size = len(os.listdir(contempt_train))

happy_break = happy_size * 0.2
anger_break = anger_size * 0.2
fear_break = fear_size * 0.2
neutral_break = neutral_size * 0.2
sad_break = sad_size * 0.2
#disgust_break = disgust_size * 0.2
#surprise_break = surprise_size * 0.2
#contempt_break = contempt_size * 0.2


i = 0
for fname in os.listdir(happy_train):
    src = os.path.join(happy_train, fname)
    dst = os.path.join(happy_val, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
    i += 1
    if i >= happy_break:
        break
i = 0
for fname in os.listdir(anger_train):
    src = os.path.join(anger_train, fname)
    dst = os.path.join(anger_val, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
    i += 1
    if i >= anger_break:
        break
i = 0
for fname in os.listdir(fear_train):
    src = os.path.join(fear_train, fname)
    dst = os.path.join(fear_val, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
    i += 1
    if i >= fear_break:
        break
i = 0
for fname in os.listdir(neutral_train):
    src = os.path.join(neutral_train, fname)
    dst = os.path.join(neutral_val, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
    i += 1
    if i >= neutral_break:
        break
i = 0
for fname in os.listdir(sad_train):
    src = os.path.join(sad_train, fname)
    dst = os.path.join(sad_val, fname)
    shutil.copyfile(src, dst)
    os.remove(src)
    i += 1
    if i >= sad_break:
        break
#i = 0
#for fname in os.listdir(disgust_train):
#    src = os.path.join(disgust_train, fname)
#    dst = os.path.join(disgust_val, fname)
#    shutil.copyfile(src, dst)
#    os.remove(src)
#    i += 1
#    if i >= disgust_break:
#        break
#i = 0
#for fname in os.listdir(surprise_train):
#    src = os.path.join(surprise_train, fname)
#    dst = os.path.join(surprise_val, fname)
#    shutil.copyfile(src, dst)
#    os.remove(src)
#    i += 1
#    if i >= surprise_break:
#        break
#i = 0
#for fname in os.listdir(contempt_train):
#    src = os.path.join(contempt_train, fname)
#    dst = os.path.join(contempt_val, fname)
#    shutil.copyfile(src, dst)
#    os.remove(src)
#    i += 1
#    if i >= contempt_break:
#        break
