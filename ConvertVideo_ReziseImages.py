import numpy as np

import cv2
import glob

def convertVideoInImages():
    name = "r1"
    cap = cv2.VideoCapture(name + ".MOV")
    count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        count += 1;
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        if count % 30 == 0:
            cv2.imshow("image", frame)
            cv2.imwrite("out/%s-%d.jpg" % (name, count), frame)

    cap.release()
    cv2.destroyAllWindows()

def resizeImagesInFolder():
    for img in glob.glob("dataset/**.jpg"):
        n = cv2.imread(img)
        n = cv2.resize(n, (400, 400))
        img = img.split('/')[1]
        print(img + "writed")
        cv2.imwrite("dataset_resized/%s" % img, n)



