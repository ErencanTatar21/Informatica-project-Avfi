def main():
    import cv2
    import numpy as np
    from PIL import Image
    import os

    # Path voor de folder waar alle foto's in staan
    path = 'dataset'

    recognizer = cv2.face.LBPHFaceRecognizer_create()
    detector = cv2.CascadeClassifier("haarcascade_frontalface_default.xml");

    # afbeeldingen groeperen
    def getImagesAndLabels(path):

        imagePaths = [os.path.join(path,f) for f in os.listdir(path)]
        faceSamples=[]
        ids = []

        for imagePath in imagePaths:

            PIL_img = Image.open(imagePath).convert('L') # convert it to grayscale
            img_numpy = np.array(PIL_img,'uint8')

            id = int(os.path.split(imagePath)[-1].split(".")[1])
            faces = detector.detectMultiScale(img_numpy)

            for (x,y,w,h) in faces:
                faceSamples.append(img_numpy[y:y+h,x:x+w])
                ids.append(id)

        return faceSamples,ids

    print ("\n [INFO] De gezichten worden in de database verwerkt...")
    faces,ids = getImagesAndLabels(path)
    recognizer.train(faces, np.array(ids))

    # Opslaan in yml bestand
    recognizer.write('trainer/trainer.yml') # recognizer.save() worked on Mac, but not on Pi

    # Print het aantal mensen dat erin zit
    print("\n [INFO] {0} faces trained. Exiting Program".format(len(np.unique(ids))))
