#

def main():
    import cv2
    import os
    import time

    leerlingnummer = ""
    print("Toevoegen nieuwe leerling")
    def New_lln():
        global beschikbaar_lln_id
        # checkt wifi verbinding
        # import urllib
        # try:
        #     url = "https://www.google.com"
        #     urllib.urlopen(url)
        # except:
        #     status = "Not connected"
        #     print(status)

#       gspread werkt als API met google sheets
#       Ipv een echte database wordt spreadsheet gebruikt, dit vanwege de snelheid ervan
        import gspread
        from oauth2client.service_account import ServiceAccountCredentials

        # Waar ik toegang tot wil
        scope = ['https://spreadsheets.google.com/feeds' , 'https://www.googleapis.com/auth/drive' ]
        credentials = ServiceAccountCredentials.from_json_keyfile_name('Loods5-d71de8db7c29.json', scope)
        gc = gspread.authorize(credentials)

        #open bestand als variabel worksheet
#       Het bestand Leerlingen_data is 1x aangemaakt en kan als de master worden gezien. 
#       Bij het toevoegen wordt gegevens van leerlingen in dit bestand gestopt
        worksheet = gc.open('Leerlingen_data').sheet1
        
        laatste_leerling_ID = worksheet.col_values(1)
        beschikbaar_lln_id = ( int(laatste_leerling_ID[-1]) + 1 )
        leerlingnummer = int(input('Wat is je leerlingnummer? : '))
        VoornaamenAchternaam = str(input("Wat is je voornaam en achternaam?: "))
        Klas = (input("In welke klas zit je?: "))

        def Uren_toevoegen():
            global uur_van_de_week
            Nogmeer = input("Zelfstudie-uren toevoegen druk Y , anders N")
            while Nogmeer.capitalize() == "Y":

                print('Geef je uren op de volgende manier: Ma_1, Ma_2, Di_3, Woe_4, Do_5, Vr_6')
                domein_uur = input("Geef je uur op:")
                dagen = ['Ma_1','Ma_2','Ma_3','Ma_4','Ma_5','Ma_6','Ma_7','Di_1','Di_2','Di_3','Di_4','Woe_1','Woe_2','Woe_3','Woe_4','Woe_5','Woe_6','Woe_7','Do_1','Do_2','Do_3','Do_4','Do_5','Do_6','Do_7','Vr_1','Vr_2','Vr_3','Vr_4','Vr_5','Vr_6','Vr_7']
                # kijken of input in lijst zit
                try:
                    index = dagen.index(domein_uur)
                except ValueError:
                    print("Er ging iets mis!")
                uur_van_de_week = index + 1

                print(uur_van_de_week)
                worksheet.update_cell((beschikbaar_lln_id + 2), uur_van_de_week + 4,"Zelfstudie")

                print("Gegevens toevoegen")
                print('\n')
                Nogmeer = input("Meer zelfstudie-uren toevoegen druk Y , anders N")
            print("We zijn bijna klaar, nu alleen nog voor zo'n 10 sec. naar de webcam kijken")

        Uren_toevoegen()



        # werkt volgens row,colom
#       update het bestand 
        worksheet.update_cell((beschikbaar_lln_id + 2), 1, beschikbaar_lln_id)
        worksheet.update_cell((beschikbaar_lln_id + 2), 2, leerlingnummer)
        worksheet.update_cell((beschikbaar_lln_id + 2), 3, VoornaamenAchternaam)
        worksheet.update_cell((beschikbaar_lln_id + 2), 4, Klas)

    New_lln()
   

    print('Toevoegen nieuwe leerling met leerling-ID',beschikbaar_lln_id)
    
#   Vanaf hier begint beeldverwerking
    cam = cv2.VideoCapture(0)
    cam.set(3, 640) # set video width
    cam.set(4, 480) # set video height

    # module voor herkennen die sneller maar minder effectief werkt 
    face_detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')



    print("\n [INFO] Initializing face capture. Look the camera and wait ...")
    # Initialize individual sampling face count
    count = 0

    while(True):

        ret, img = cam.read()
        face_id = (beschikbaar_lln_id)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        faces = face_detector.detectMultiScale(gray, 1.3, 5)

        for (x,y,w,h) in faces:

            cv2.rectangle(img, (x,y), (x+w,y+h), (255,0,0), 2)
#           voordat hij 
            time.sleep(3)
            count += 1
            # Save de afbeeldingen in de folder dataset met .face_id
            cv2.imwrite("dataset/User." + str(face_id) + '.' + str(count) + ".jpg", gray[y:y+h,x:x+w])
            cv2.imshow('image', img)

        k = cv2.waitKey(100) & 0xff # Druk 'ESC' om te stoppen
        if k == 27:
            break
        elif count >= 7: # Neemt nu 7 foto's 
             break

    # cleanup
    print("\n", "Bye")
    cam.release()
    cv2.destroyAllWindows()



