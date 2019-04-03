def main():
    import time
    import datetime
    # current = datetime.datetime.now()

    def SysteemActief():
        # tijd en input
        dag = datetime.datetime.today().weekday()
        # Monday is 1 and Sunday is 7
        now = datetime.datetime.now()
        AC = input("Activeer --> Y?: ")
        if (dag) <= 5 and now.hour >= 15 or AC.capitalize() == "Y":
            print("Activeer syteem")
        #     werkt tot 16:00 van maandag t/m vrijdag
            def herkenning():
                import cv2
                import numpy as np
                import os
                recognizer = cv2.face.LBPHFaceRecognizer_create()
                recognizer.read('trainer/trainer.yml')
                cascadePath = "haarcascade_frontalface_default.xml"
                faceCascade = cv2.CascadeClassifier(cascadePath);
                font = cv2.FONT_HERSHEY_SIMPLEX

                #iniciate id counter
                id = 1
                # Maakt lijst van namen met LLn-ID en

                namen = []
                def get_namen():
                    global X
                    global namen
                    namen = []
                    import gspread
                    from oauth2client.service_account import ServiceAccountCredentials
                    scope = ['https://spreadsheets.google.com/feeds' , 'https://www.googleapis.com/auth/drive' ]
                    credentials = ServiceAccountCredentials.from_json_keyfile_name('Loods5-d71de8db7c29.json', scope)
                    gc = gspread.authorize(credentials)
                    worksheet = gc.open('Leerlingen_data').sheet1
                    namen = worksheet.col_values(3)
                    X = (namen[2:])
                get_namen()


                names = X

                # Initialize and start realtime video capture
                cam = cv2.VideoCapture(0)
                cam.set(3, 640) # set video widht
                cam.set(4, 480) # set video height
                # Define min window size to be recognized as a face
                minW = 0.1*cam.get(3)
                minH = 0.1*cam.get(4)


                while True:
                    ret, img =cam.read()

                    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

                    faces = faceCascade.detectMultiScale(
                        gray,
                        scaleFactor = 1.2,
                        minNeighbors = 5,
                        minSize = (int(minW), int(minH)),
                        # scaleFactor: This function compensates a false perception in size that occurs when one face appears to be bigger than the other simply because it is closer to the camera.
                        # minNeighbors: Detection algorithm that uses a moving window to detect objects, it does so by defining how many objects are found near the current one before it can declare the face found.
                       )
                    for(x,y,w,h) in faces:
                        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2)
                        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])

                        # If confidence is less them 100 ==> "0" : perfect match
                        if (confidence < 100):
                            id = names[id-1]
                            confidence = "  {0}%".format(round(100 - confidence))





                        else:
                            id = "unknown"
                            confidence = "  {0}%".format(round(100 - confidence))

                        cv2.putText(
                                    img,
                                    str(id),
                                    (x+5,y-5),
                                    font,
                                    1,
                                    (255,255,255),
                                    2
                                   )
                        cv2.putText(
                                    img,
                                    str(confidence),
                                    (x+5,y+h-5),
                                    font,
                                    1,
                                    (255,255,0),
                                    1
                                   )

                    cv2.imshow('camera',img)



                    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
                    if k == 27:
                        break
                # Do a bit of cleanup
                print("\n Exiting Program ")
                cam.release()
                cv2.destroyAllWindows()
            herkenning()
        else:
            exit()
    SysteemActief()


