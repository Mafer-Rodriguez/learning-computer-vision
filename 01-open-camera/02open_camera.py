import cv2 #esta es la libreria de opencv

#buscamos la camara activa o disponible, con regularidad la camara esta en la posicion es la que tenemos instalada
cap = cv2.VideoCapture(0)

#iniciamos un ciclo while infinito para ejecutar nuestra camara, es infinito por que queremos que se mantenga abierta hasta que el usuario decida cerrarla (q)
while True:

    #obtenemos dos variables
    is_working, frame = cap.read()

    #
    if not is_working:
        print("la camara no se esta iniciando")
        break

    cam_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)



    #si esta funcionando, abrimos una ventana con la informacion de cada frame que detecta nuestra camara
    cv2.imshow("mi primera vez abriendo la camara", cam_gray)

    #si esta funcionando, abrimos la ventana 
    if cv2.waitKey(1) &  0XFF  == ord('q'):
        break
#una vez fuera del ciclo, debemos liberar la camara
cap.release()
#y destruir toda las ventanas que abrimos
cv2.destroyAllWindows()