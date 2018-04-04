import sys
import os,time
import cognitive_face as CF
from global_variables import personGroupId
import sqlite3
import urllib3
urllib3.disable_warnings()
import urllib

Key = 'db85583701c04bf08f8a9fb9a9290b78'
CF.Key.set(Key)
BASE_URL = 'https://westcentralus.api.cognitive.microsoft.com/face/v1.0'
CF.BaseUrl.set(BASE_URL)

def get_person_id():
	person_id = ''
	extractId = str(sys.argv[1])[-2:]
	connect = sqlite3.connect("Face-DataBase")
	c = connect.cursor()
	cmd = "SELECT * FROM Students WHERE ID = " + extractId
	c.execute(cmd)
	row = c.fetchone()
	person_id = row[3]
	return person_id

if len(sys.argv) is not 1:
    res = CF.person.create(personGroupId, str(sys.argv[1]))
    print(res)
    extractId = str(sys.argv[1])[-2:]
    connect = sqlite3.connect("Face-DataBase")
    cmd = "SELECT * FROM Students WHERE ID = " + extractId
    cursor = connect.execute(cmd)
    isRecordExist = 0
    for row in cursor:                                                          
        isRecordExist = 1
    if isRecordExist == 1:                                                      
        connect.execute("UPDATE Students SET personID = ? WHERE ID = ?",(res['personId'], extractId))

    print "ok"

    connect.commit()


    currentDir = os.path.dirname(os.path.abspath(__file__))
    imageFolder = os.path.join(currentDir, "dataset/" + str(sys.argv[1]))
    person_id = get_person_id()
    for filename in os.listdir(imageFolder):
        if filename.endswith(".jpg"):
        	print(filename)
        	imgurl = urllib.pathname2url(os.path.join(imageFolder, filename))
		print imgurl
        	res = CF.face.detect(imgurl)
        	if len(res) != 1:
        		print "No face detected in image"
        	else:
        		res = CF.person.add_face(imgurl, personGroupId, person_id)
        		print(res)	
        	time.sleep(6)


                                                               
    connect.close()

