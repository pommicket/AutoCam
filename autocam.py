import cv2
import numpy as np
import random
import time

print 'Press q to quit while the video is playing'

rec = raw_input('Record to video [y/n]? ').lower()[0] == 'y'

single = ['np.cos', 'np.sin', 'np.tan'] #Operations on a single number
binary = ['*', '+', '-'] #Operations for 2 numbers
numlist = ['frame', 't', 'Constant']

def randFunction(functionLength, singleweight, numberweight):
    hasframe = False
    hast = False
    while not(hasframe and hast):
        #Types: b for binary, s for single, f for first, n for number
        function = ''
        lasttype = 'f'
        thistype = 0
        hasframe = False
        hast = False
        chanceend = 0
        length = 1 #Number of operations done so far
        while True:
            chanceend = (1.0 - (1.0 / length)) ** (float(functionLength)/7)
            if lasttype == 'n':
                number = random.random()
                if number < chanceend:
                    break
                function = '(' + function + ')' + random.choice(binary)
                lasttype = 'b'
            elif lasttype == 's' or lasttype == 'b' or lasttype == 'f':
                function += '('
                thistype = random.random()
                if thistype < singleweight / (singleweight + numberweight):
                    function += random.choice(single)
                    lasttype = 's'
                else:
                    what = random.choice(numlist)
                    if what == 'Constant':
                        function += str(random.gauss(150, 50))
                    else:
                        function += what
                        if what == 'frame':
                            hasframe = True
                        elif what == 't':
                            hast = True
                    lasttype = 'n'
                    function += ')'
            length += 1
    if function.count('(') > function.count(')'):
        function += ')' * (function.count('(') - function.count(')'))
    return function

start = time.time()

t = 0
cap = cv2.VideoCapture(0)
function = randFunction(80, 1, 1)

try:
    w = cap.get(cv2.CV_CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.CV_CAP_PROP_FRAME_HEIGHT)
except:
    w = cap.get(cv2.cv.CV_CAP_PROP_FRAME_WIDTH)
    h = cap.get(cv2.cv.CV_CAP_PROP_FRAME_HEIGHT)

if rec:
    try:
        fourcc = cv2.cv.CV_FOURCC(*'XVID')
    except:
        fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter(' '.join([namemaker3.generate() for i in range(3)]) + '.avi', fourcc, 10, (int(w),int(h)))


while True:
    t += 0.1
    ret, frame = cap.read()
    frame = frame.astype(float)
    frame = eval(function).astype(np.uint8)
    if rec:
        out.write(frame)
    cv2.imshow('Video',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

cap.release()
if rec:
    out.release()
cv2.destroyAllWindows()


