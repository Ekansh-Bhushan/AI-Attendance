import cv2
import numpy as np
import face_recognition 
import os
from datetime import datetime
import mysql.connector as my

mydb=my.connect(host='localhost',user='root',passwd='Ekansh@04',database='ayushi')
mycursor=mydb.cursor()

def create_table() :
     try:
          query = "create table if not exists attendance (SNO integer(10) primary key ,student_name varchar(30) ,come_date date )"                                              
          mycursor.execute(query)
     except Exception as e:
          print(e)
create_table()
)



def add_records() :
     try :
          while True :
               
               C
               Client_loc = input('Enter the location of client  =  ')
               Orders = int(input('Enter the number of orders  =  '))
               Payments = int(input('Enter the amount of payments  =  '))
               query = f"insert into orders values({Order_no},'{Client_name}','{Client_loc}',{Orders},{Payments})"
               mycursor.execute(query)
               ans = input('WANNA ENTER MORE VALUES(y/n)  : ')
               if ans.lower() == 'n' :
                    break
          mydb.commit()
     except Exception as e:
          print(e)
     



# FUNCTION TO DELETE RECORD FOR THE GIVEN ORDER NUMBER

def del_rec() :
     try :
          ord_num = int(input('\n Enter the order number for which the record is to be deleated  =  '))
          query = f"delete from orders where Order_no = {ord_num}"
          mycursor.execute(query)
          mydb.commit()
     except Exception as e :
          print(e)


# FUNCTION TO DISPLAY ALL RECORDS OF THE TABLE

def display_all() :
     try:
          query = f"select * from ORDERS"
          mycursor.execute(query)
          myrecords = mycursor.fetchall()
          c = mycursor.rowcount
          if c == 0 :
               print('Not Found')
          else :
               print('Order_no'.ljust(15), 'Client_name'.ljust(15),'Client_loc'.ljust(15),'Orders'.ljust(15),'Payments'.ljust(15))
               for x in myrecords :
                    print('\n',end='')
                    for i in x :
                         print(str(i).ljust(15) , end = '|')  
          
     except Exception as e :
          print(e)

create_table()
add_records()
del_rec()
display_all()
     
"""
path = 'images'
images = []
personName = []
mylist = os.listdir(path)
print(mylist)
for cu_img in mylist:
    current_img = cv2.imread(f"{path}/{cu_img}")
    images.append(current_img)
    personName.append(os.path.splitext(cu_img)[0])
print(personName)


def faceEncodings(images):
    encodelist = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodelist.append(encode)
    return encodelist

#print(faceEncodings(images)) #hog transformation


def attendance(name):
    with open('attendane.txt', 'w+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            time_now = datetime.now()
            tStr = time_now.strftime('%H:%M:%S')
            dStr = time_now.strftime('%d/%m/%Y')
            f.writelines(f'\n{name},{tStr},{dStr}')




encodeListKnown = faceEncodings(images)
print(" ALL Encoding are completed")

cap =  cv2.VideoCapture(0, cv2.CAP_DSHOW) #captureDevice = camera need to check

while True:
    ret, frame = cap.read()
    faces = cv2.resize(frame, (0, 0), None, 0.25, 0.25)
    faces = cv2.cvtColor(faces, cv2.COLOR_BGR2RGB)

    facesCurrentFrame = face_recognition.face_locations(faces)
    encodesCurrentFrame = face_recognition.face_encodings(faces,facesCurrentFrame)

    for encodeFace, faceLoc in zip(encodesCurrentFrame,facesCurrentFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        
        matchIndex = np.argmin(faceDis)

        if matches[matchIndex]:
            name = personName[matchIndex].upper()
            #print(name)
            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2) # 0,255,0 is green color
            cv2.rectangle(frame, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
            cv2.putText(frame, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
            attendance(name)
            
    cv2.imshow("camera",frame)
    if cv2.waitKey(10) == 13:
        break

cap.release()
cv2.destroyAllWindows()
"""