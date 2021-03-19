import numpy as np
from keras.models import model_from_json
from keras.preprocessing import image

import cv2

from time import sleep

#############

model = model_from_json(open("fer3.json", "r").read())
model.load_weights('fer3.h5')

face_haar_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

#############

class emo:
        
    cap = cv2.VideoCapture(0)      
    
    @classmethod
    def fRecognize( self, duration ):
        
        self.duration = duration
             
        timerCounter = 0
        fDetected = False
        emoFitnessPoints = np.zeros( 7 )   
        
        while True:
    
            ret, testIMG = self.cap.read()
            
            if not ret:
                continue
            
            gray_img = cv2.cvtColor(testIMG, cv2.COLOR_BGR2GRAY)
    
            faces_detected = face_haar_cascade.detectMultiScale(gray_img, 1.32, 5)
    
            for (x, y, w, h) in faces_detected:
    
                cv2.rectangle(testIMG, (x, y), (x+w, y+h), (255, 0, 0), thickness=7)
                roi_gray = gray_img[y: y+w, x: x+h]
                roi_gray = cv2.resize(roi_gray, (48, 48))
                img_pixels = image.img_to_array(roi_gray)
                img_pixels = np.expand_dims(img_pixels, axis=0)
                img_pixels /= 255.0
    
                # Tahminleri Alıyorum ( Birden Fazla Tahmin Bulacak Fitness Oranına Göre )       
                predictions = model.predict( img_pixels )     
                
                emoFitnessPoints += predictions[ 0 ]   
                fDetected = True                          
            
            if fDetected == True:
                timerCounter += 1
                fDetected = False
                
            # Timer İle Duygunun Devamlılığı Kontrolü Sağlanır
            sleep( 0.3 )
                
            if timerCounter >= self.duration:
                return emoFitnessPoints
