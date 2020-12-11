##############################################################################################

##############################OBJECT DETECTION OF AN IMAGE#############################3######

##############################################################################################
#import opencv library
import cv2

# Read example/input images
img1 = cv2.imread('example_01.jpg')
# img2 = cv2.imread('example_02.jpg')
# img3 = cv2.imread('example_03.jpg')
# img4 = cv2.imread('example_04.jpg')
# img5 = cv2.imread('example_05.jpg')
# img6 = cv2.imread('example_06.jpg')
# img7 = cv2.imread('example_07.jpg')
# img8 = cv2.imread('example_08.jpg')
# img9 = cv2.imread('example_09.jpg')

########printing the input image############
cv2.imshow('Image1', img1)
# cv2.imshow('Image2', img2)
# cv2.imshow('Image3', img3)
# cv2.imshow('Image4', img4)
# cv2.imshow('Image5', img5)
# cv2.imshow('Image6', img6)
# cv2.imshow('Image7', img7)
# cv2.imshow('Image8', img8)
# cv2.imshow('Image9', img9)
cv2.waitKey(0)

# #Importing the COCO dataset in a list
classNames = []
classFile = 'coco.names'
with open(classFile, 'rt') as f:
    classNames = f.read().rstrip('\n').split('\n')

# print(classNames)

##Configuring both SSD model and weights (assigning)

configPath = 'ssd_mobilenet_v3_large_coco_2020_01_14.pbtxt'
weightsPath = 'frozen_inference_graph.pb'

#dnn-Inbuilt method of OpenCV
net = cv2.dnn_DetectionModel(weightsPath, configPath)
net.setInputSize(320, 320)
net.setInputScale(1.0 / 127.5)
net.setInputMean((127.5, 127.5, 127.5))
net.setInputSwapRB(True)

# using Detect method
classIds, confs, bbox = net.detect(img1, confThreshold=0.5)
print(classIds, bbox)

#Loop for assigning text and box for each object
for classId, confidence,box in zip(classIds.flatten(),confs.flatten(), bbox):
    cv2.rectangle(img1, box, color = (0, 255, 0),thickness=2)
    cv2.putText(img1, classNames[classId-1].upper(), (box[0]+10,box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)
    cv2.putText(img1, str(round(confidence*100, 2)), (box[0]+200, box[1]+30), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 2)

#printing the final image
cv2.imshow('Final Image1', img1)
# cv2.imshow('Final Image2', img2)
# cv2.imshow('Final Image3', img3)
# cv2.imshow('Final Image4', img4)
# cv2.imshow('Final Image5', img5)
# cv2.imshow('Final Image6', img6)
# cv2.imshow('Final Image7', img7)
# cv2.imshow('Final Image8', img8)
# cv2.imshow('Final Image9', img9)
cv2.waitKey(0)