import cv2 #Importa la libreria  de OpenCV para procesamiento de imágenes y video
# Carga el clasificador Haar Cascade para la detección de rostros
#Inicializa el haarcades que tiene OpenCV  y el archivo que descargamos.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

cap = cv2.VideoCapture(0)
while True: 
    #variables booleana que dice si detecta o no un rostro y la variable frame que es el cuadro de video que se esta leyendo
    ret,frame = cap.read()  
    #Cambiamos las imagenes a blanco y negro para que el algoritmo de detección de rostros funcione mejor, y luego detectamos los rostros en la imagen en escala de grises.
    gris = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    #Detectamos los rostros 
    #detectMultiScale: Detecta objetos de diferentes tamaños en la imagen, en otras palabras es el metodo que realiza el analisis de las imagenes 
    #scaleFactor: Redimenciona cada imagen, en ejemplo (1.1) hace 10 % mas
    #pequeña la imagen en otras palbras sacaleFactor 
    #minNeighbors: Cunta la cantidad de capas sobre un rostro , en otras palabras mas sensillas  
    #minSize : Es el tamaño mínimo que un objeto debe tener para ser considerado un rostro (minimo de tamaño aceptable por rostro)
    rostros = face_cascade.detectMultiScale(gris, scaleFactor=1.1, minSize=(30, 30))
    #Ross¿tros es lo siguiente : 
    """[
    (23,123,123,354)
    (23,123,123,354)
    (23,123,123,354)
    ]"""
    for (x, y, w, h) in rostros:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2) #Verde en BGR
        cv2.imshow('Detección de Rostros', frame)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
cap.release()
cv2.destroyAllWindows()