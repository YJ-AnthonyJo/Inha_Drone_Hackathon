import cv2 as cv
import time
import requests
from PIL import ImageGrab
import numpy as np
import win32api

hsv = 0
lower_blue1 = 0
upper_blue1 = 0
lower_blue2 = 0
upper_blue2 = 0
lower_blue3 = 0
upper_blue3 = 0

street1=0
street2=0

def nothing(x):
    pass

while True:
    a,b=win32api.GetCursorPos()
    img_color = np.array(ImageGrab.grab(bbox=(0, 68, a, b)))
    img_color = cv.cvtColor(img_color, cv.COLOR_RGB2BGR)
    cv.imshow("screen", img_color)
    if cv.waitKey(1) == ord('c') :
        st=time.time()
        while time.time()-st <=10:
            img_color = np.array(ImageGrab.grab(bbox=(0, 68, a, b)))
            img_color = cv.cvtColor(img_color, cv.COLOR_RGB2BGR)
            cv.imshow("screen", img_color)

            height, width = img_color.shape[:2]
            img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

            # 원본 영상을 HSV 영상으로 변환합니다.
            img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

            ################################
            lower_blue1 = np.array([125, 30, 30])
            upper_blue1 = np.array([135, 255, 255])

            lower_blue2 = np.array([115, 30, 30])
            upper_blue2 = np.array([125, 255, 255])

            lower_blue3 = np.array([115, 30, 30])
            upper_blue3 = np.array([115, 255, 255])

            ###############################
            # 범위 값으로 HSV 이미지에서 마스크를 생성합니다.
            img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
            img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
            img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
            img_mask = img_mask1 | img_mask2 | img_mask3

            kernel = np.ones((11, 11), np.uint8)
            img_mask = cv.morphologyEx(img_mask, cv.MORPH_OPEN, kernel)
            img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)

            # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분을 획득합니다.
            img_result = cv.bitwise_and(img_color, img_color, mask=img_mask)

            ### 렉탱글 치기
            recnum = 0
            munOfLabels, img_label, stats, centroids = cv.connectedComponentsWithStats(img_mask)
            for idx, centroid in enumerate(centroids):
                if stats[idx][0] == 0 and stats[idx][1] == 0:
                    continue
                if np.any(np.isnan(centroid)):
                    continue
                x, y, width, height, area = stats[idx]
                cenX, cenY = int(centroid[0]), int(centroid[1])

                if area > 20:
                    cv.rectangle(img_color, (x, y), (x + width, y + height), (0, 0, 255))
                    recnum = recnum + 1
            if time.time()-st >=5:
                street1=recnum
            # 렉탱글 치기

            #cv.imshow('img_mask', img_mask)
            cv.imshow("screen", img_color)
            cv.imshow('img_result', img_result)
            print("recnum : ", str(recnum))
            
        st=time.time()
        while time.time()-st <=10:
            img_color = np.array(ImageGrab.grab(bbox=(0, 68, a, b)))
            img_color = cv.cvtColor(img_color, cv.COLOR_RGB2BGR)
            cv.imshow("screen", img_color)

            height, width = img_color.shape[:2]
            img_color = cv.resize(img_color, (width, height), interpolation=cv.INTER_AREA)

            # 원본 영상을 HSV 영상으로 변환합니다.
            img_hsv = cv.cvtColor(img_color, cv.COLOR_BGR2HSV)

            ################################
            lower_blue1 = np.array([125, 30, 30])
            upper_blue1 = np.array([135, 255, 255])

            lower_blue2 = np.array([115, 30, 30])
            upper_blue2 = np.array([125, 255, 255])

            lower_blue3 = np.array([115, 30, 30])
            upper_blue3 = np.array([115, 255, 255])

            ###############################
            # 범위 값으로 HSV 이미지에서 마스크를 생성합니다.
            img_mask1 = cv.inRange(img_hsv, lower_blue1, upper_blue1)
            img_mask2 = cv.inRange(img_hsv, lower_blue2, upper_blue2)
            img_mask3 = cv.inRange(img_hsv, lower_blue3, upper_blue3)
            img_mask = img_mask1 | img_mask2 | img_mask3

            kernel = np.ones((11, 11), np.uint8)
            img_mask = cv.morphologyEx(img_mask, cv.MORPH_OPEN, kernel)
            img_mask = cv.morphologyEx(img_mask, cv.MORPH_CLOSE, kernel)

            # 마스크 이미지로 원본 이미지에서 범위값에 해당되는 영상 부분을 획득합니다.
            img_result = cv.bitwise_and(img_color, img_color, mask=img_mask)

            ### 렉탱글 치기
            recnum = 0
            munOfLabels, img_label, stats, centroids = cv.connectedComponentsWithStats(img_mask)
            for idx, centroid in enumerate(centroids):
                if stats[idx][0] == 0 and stats[idx][1] == 0:
                    continue
                if np.any(np.isnan(centroid)):
                    continue
                x, y, width, height, area = stats[idx]
                cenX, cenY = int(centroid[0]), int(centroid[1])

                if area > 20:
                    cv.rectangle(img_color, (x, y), (x + width, y + height), (0, 0, 255))
                    recnum = recnum + 1
            if time.time()-st >=5:
                street2=recnum
            # 렉탱글 치기

            #cv.imshow('img_mask', img_mask)
            cv.imshow("screen", img_color)
            cv.imshow('img_result', img_result)
            print("recnum : ", str(recnum))
            
        break
st=time.time()
while True:
    if time.time()-st>=5:
        img_color = np.array(ImageGrab.grab(bbox=(0, 68, a, b)))
        img_color = cv.cvtColor(img_color, cv.COLOR_RGB2BGR)
        cv.imwrite("situ.jpg",img_color)
        break

cv.destroyAllWindows()
if stree1>street2:
    r=requests.get("http://localhost/inha_drone/main.php?a=2")
elif street1<street2:
    r=requests.get("http://localhost/inha_drone/main.php?a=1")
try:
    url = 'http://localhost/inha_drone/upload.php'
    files = {'myfile': open('situ.jpg', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)
    print("성공!!")
except:
    print("")

