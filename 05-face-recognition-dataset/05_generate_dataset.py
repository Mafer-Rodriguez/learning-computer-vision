import cv2
cam= cv2.VideoCapture(0)
detector = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
#Ingresamos el ID de cada persona
face_id = int(input('\n Ingresa el ID del usuario: '))
print ("\n [INFO] Iniciando la camara, porfavor ver directamente a la camara")
count =0
#Entramos a nuestro bucle para capturar las imagenes de cada rostro, y guardarlas en la carpeta dataset
while(True):
    #Cambiamos cada frame a escala de grises para que el algoritmo de detección de rostros funcione mejor, y luego detectamos los rostros en la imagen en escala de grises.
    is_working, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray,scaleFactor=1.1, minNeighbors=5, minSize=(30,30))
    #Recorremos cada rostro detectado, dibujamos un rectángulo alrededor de cada rostro y guardamos la imagen del rostro en la carpeta dataset con el formato User.ID.Cout.jpg
    for (x,y,w,h) in faces: 
        #Si encuentra un rostro, dibuja un rectángulo verde alrededor del rostro detectado y guarda la imagen del rostro en la carpeta dataset con el formato User.ID.Cout.jpg
        cv2.rectangle(img, (x,y), (x+w, y+h), (0,0,255), 2)
        #Cambiamos el contador para cada imagen guardada, y guardamos la imagen del rostro en la carpeta dataset con el formato User.ID.Cout.jpg
        count += 1
        #El metodo imwrite de OpenCV se utiliza para guardar la imagen del rostro detectado en la carpeta dataset con el formato User.ID.Cout.jpg, donde face_id es el ID del usuario ingresado por el usuario y cout es el contador que se incrementa para cada imagen guardada.
        #En otras palabras mas senciññas, recibe 2 parametros: el nombre del archivo y la data a guardar 
        #En este caso el nombre del archivo se compone de una base user, el ID de usuario y el conteo
        #Finalmente le pasamos las coordenadas donde se encontró el rostro en la imagen. 
        cv2.imwrite(f"dataset/user_{face_id}_{count}.jpg", gray[y:y+h,x:x+w])
        #Mostramos la imagen del rostro detectado en una ventana llamada 'image' utilizando el método imshow de OpenCV, y esperamos a que el usuario presione la tecla 'q' para salir del bucle y finalizar la captura de imágenes.
    cv2.imshow('image', img)
    #salir del programa 
    if cv2.waitKey(1) & 0xFF == ord('q') or count >= 30:
        break
     #Si el contador llega a 30, significa que se han capturado suficientes imágenes del rostro del usuario, y se sale del bucle para finalizar la captura de imágenes.
        

print("\n [INFO] Conjunto completo")
cam.release()
cv2.destroyAllWindows()


