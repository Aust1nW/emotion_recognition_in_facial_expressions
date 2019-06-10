import re
import json
import os
from keras.models import load_model
from keras.preprocessing import image
from keras.applications.vgg16 import preprocess_input
import numpy as np

def predict(model, fname):
    path = os.path.join('./realTests', fname)
    image = image.load(path, target_size=(350,350))
    x = image.img_to_array(image)
    x = np.expand_dims(x, axis=0)
    x = preprocess_input(x)
    preds = model.predict(x)
    return np.argmax(preds[0])




def main():
    model = load_model('vgg1.h5')
    test_files = open('./data/500_picts_satz.csv', 'r')
    
    fear = 0
    happiness = 0
    neutral = 0
    anger = 0
    sad = 0
    correct = False
    with open('class_map.json', 'r') as fname:
        fstr = fname.read()
        class_map = json.loads(fstr)

    for line in test_files.readlines():
        line = list(line.split(','))
        line[2] = re.sub(r'\n', '', line[2])
        emotion = line[2]
        fname = line[1]
        val = predict(None, fname)
        actual = class_map[emotion]
        print(actual, val)
        if(actual == val):
            correct = True
    
        if correct and val == 0:
            anger += 1
        elif correct and val == 1:
            fear += 1
        elif correct and val == 2:
            happy += 1
        elif correct and val == 3:
            neutral+= 1
        elif correct and val == 4:
            sad += 1

        correct = False

    fear_acc = fear / 54
    happy_acc = happiness / 197
    neutral_acc = neutral / 84
    anger_acc = anger / 115
    sad_acc = sad / 50

    print('Fear acc:    %.2f' % fear_acc)
    print('Happy acc:   %.2f' % happy_acc)
    print('Neutral acc: %.2f' % neutral_acc)
    print('Anger acc:   %.2f' % anger_acc)
    print('Sad acc:     %.2f' % sad_acc)

    weighted_acc = (fear_acc * 0.108 +
                    happy_acc * 0.394 +
                    neutral_acc * 0.168 + 
                    anger_acc * 0.23 + 
                    sad_acc * 0.1)
    print('-----------------')
    print('Weighted Acc: %.2f' % weighted_acc)


    #TODO: 
    #1. load json file containing labels_map
    #2. check and see if prediction is correct
    #3. add to tally for respective emotion
    #4. Calculate weighted accuracy



if __name__ == "__main__":
   main()
