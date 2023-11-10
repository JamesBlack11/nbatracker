import cv2
import os


path = '/Users/jamesschwartz/PycharmProject/nbatracker/Frames'
vidcap = cv2.VideoCapture('/Users/jamesschwartz/PycharmProject/nbatracker/TestDetection/highlight38.mp4')
def getFrame(sec):
    vidcap.set(cv2.CAP_PROP_POS_MSEC,sec*1000)
    hasFrames,image = vidcap.read()
    if hasFrames:

        cv2.imwrite(os.path.join(path, "image"+str(count)+".jpg"), image)     # save frame as JPG file

    return hasFrames
sec = 0
frameRate = 0.01 #//it will capture image in each 0.2 second
count=1
success = getFrame(sec)
while success:
    count = count + 1
    sec = sec + frameRate
    sec = round(sec, 2)
    success = getFrame(sec)

