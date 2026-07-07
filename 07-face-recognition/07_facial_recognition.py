import cv2 

#CArgamos todas las 
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainer/trainer.yml")
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath)

#Vamos a definir las variables pricipales del sistema 
font = cv2.FONT_HERSHEY_COMPLEX
id = 0
names= {

}
cap = cv2.VideoCapture(0)

#Inicializamos el ciclo infinito para analizar las imagenes 
while True:
    #Los siguinetes pasos son los basicos, leer la camara, trasformar cada 
    #imagen a blancos y negro, detectar cada rostro en le fame y procesar cada imagen 
    is_working, img = cap.read()
    if not is_working:
        print("No se pudo iniciar la camara :")
        break 
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor = 1.2,
        minNeighbors =5,
        minSize = (50, 50),

    )

    #Pasamos rostro por rostro, ponemos el cuadro de deteccion 
    #Predecimo el rostro 
    #Calculamos el nivel de coincidencia 
    #Pintamos los textos en la imagen 
    for(x,y,w,h) in faces :
        cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])
        #Check if confidence is less them 100 ==> "0" is perfect march 
        if (confidence < 100):
            id = names[id]
            confidence = f"{round(100 - confidence)}%"
        else:
            id = "unknown"
            confidence = f"{round(100 - confidence)}%"

        cv2.putText(img, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(img, str(confidence), (x+5,y+h-5), font, 1, (255,255,255), 1)
    cv2.imshow('camera',img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
print("\n [INFO] Exiting Program and cleanup stuff")
cap.release()
cv2.destroyAllWindows()
