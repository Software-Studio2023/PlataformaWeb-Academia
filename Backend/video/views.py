from django.shortcuts import render
from django.http import StreamingHttpResponse
import cv2
import mediapipe as mp
import math
import time

# Creamos nuestra funcion de dibujo
mpDibujo = mp.solutions.drawing_utils
ConfDibu = mpDibujo.DrawingSpec(thickness=1, circle_radius=1)

# Creamos un objeto donde almacenaremos la malla facial
mpMallaFacial = mp.solutions.face_mesh
MallaFacial = mpMallaFacial.FaceMesh(max_num_faces=1)

# Realizamos la Videocaptura
cap = cv2.VideoCapture(0)

# Mostramos el video en tiempo real
def gen_frame():
    parpadeo = False
    conteo = 0
    tiempo = 0
    inicio = 0
    final = 0
    conteo_sue = 0
    muestra = 0
    # Empezamos
    while True:
        # Leemos la VideoCaptura
        ret, frame = cap.read()

        px = []
        py = []
        lista = []

        # Si tenemos un error
        if not ret:
            break
        else:
            # Correccion de color
            frameRGB = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

            # Observamos los resultados
            resultados = MallaFacial.process(frameRGB)

            # Si tenemos rostros
            if resultados.multi_face_landmarks:
                # Iteramos
                for rostros in resultados.multi_face_landmarks:
                    # Dibujamos
                    mpDibujo.draw_landmarks(frame, rostros, mpMallaFacial.FACEMESH_TESSELATION, ConfDibu, ConfDibu)

                    for id, puntos in enumerate(rostros.landmark):
                        al, an, c = frame.shape
                        x, y = int(puntos.x * an), int(puntos.y * al)
                        px.append(x)
                        py.append(y)

                        lista.append([id, x, y])

                        if len(lista) == 468:
                            x1, y1 = lista[145][1:]
                            x2, y2 = lista[159][1:]

                            logintud1 = math.hypot(x2 - x1, y2 - y1)

                            x3, y3 = lista[374][1:]
                            x4, y4 = lista[386][1:]

                            logintud2 = math.hypot(x4 - x3, y4 - y3)

                            cv2.putText(frame, f'Parpadeo: {int(conteo)}', (30, 60), cv2.FONT_HERSHEY_SIMPLEX, 1,
                                        (0, 255, 0), 2)

                            cv2.putText(frame, f'Micro Sueno: {int(conteo_sue)}', (380, 60),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

                            cv2.putText(frame, f'Duracion:  {int(muestra)}', (210, 450),
                                        cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

                            if logintud1 <= 10 and logintud2 <= 10 and not parpadeo:
                                parpadeo = True
                                inicio = time.time()

                            elif logintud2 > 10 and logintud1 > 10 and parpadeo:
                                parpadeo = False
                                final = time.time()
                                conteo += 1

                            tiempo = round(final - inicio, 0)

                            if tiempo >= 3:
                                conteo_sue += 1
                                muestra = tiempo
                                inicio = 0
                                final = 0

            # Codificamos nuestro video en Bytes
            _, encode = cv2.imencode('.jpg', frame)
            frame = encode.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


# Ruta de la aplicacion 'principal'
def index(request):
    return render(request, 'index.html')


# Ruta del video
def video(request):
    return StreamingHttpResponse(gen_frame(), content_type='multipart/x-mixed-replace; boundary=frame')