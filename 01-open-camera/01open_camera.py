import cv2

cap = cv2.VideoCapture(0)

while True:
    is_working, frame = cap.read()
    break
    if not is_working:
        print("La camara no se a inicializo por alguna razon")
        break

    cv2.imshow("Mi primera vez abrindo la camara", frame)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()