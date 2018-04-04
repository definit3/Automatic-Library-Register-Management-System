import cv2                                                                    
import numpy as np                                                             
import sqlite3
import dlib
import os   
import urllib3
urllib3.disable_warnings()                                                                 

cap = cv2.VideoCapture(0)
#address = "http://172.16.181.195:8080/video" 
#cap.open(address)
detector = dlib.get_frontal_face_detector()

def insertOrUpdate(Id, Name, roll) :                                           
    connect = sqlite3.connect("Face-DataBase")                                 
    cmd = "SELECT * FROM Students WHERE ID = " + Id                            
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                         
        isRecordExist = 1
    if isRecordExist == 1:                                                      
        connect.execute("UPDATE Students SET Name = ? WHERE ID = ?",(Name, Id))
        connect.execute("UPDATE Students SET Roll = ? WHERE ID = ?",(roll, Id))
    else:
    	params = (Id, Name, roll)                                              
    	connect.execute("INSERT INTO Students(ID, Name, Roll) VALUES(?, ?, ?)", params)
    connect.commit()                                                            
    connect.close()                                                             

name = raw_input("Enter student's name : ")
roll = raw_input("Enter student's Roll Number : ")
Id = roll[-2:]
insertOrUpdate(Id, name, roll)                                                  


folderName = "user" + Id                                                       
folderPath = os.path.join(os.path.dirname(os.path.realpath(__file__)), "dataset/"+folderName)
if not os.path.exists(folderPath):
    os.makedirs(folderPath)

sampleNum = 0
while(True):
    ret, img = cap.read()                                                      
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)                               
    dets = detector(img, 1)
    for i, d in enumerate(dets):                                               
        sampleNum += 1
        cv2.imwrite(folderPath + "/User." + Id + "." + str(sampleNum) + ".jpg",
                    img[d.top():d.bottom(), d.left():d.right()])                                                
        cv2.rectangle(img, (d.left(), d.top())  ,(d.right(), d.bottom()),(0,255,0) ,2) 
        cv2.waitKey(200)                                                       
    cv2.imshow('frame', img)                                                   
    cv2.waitKey(1)
    if(sampleNum >= 20):                                                        
        break

cap.release()                                                                  
cv2.destroyAllWindows()                                                        
