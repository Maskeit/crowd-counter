from ultralytics import YOLO
import cv2
import time
from process import send_person_count
model = YOLO("yolov8m.pt")

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: no se puede abrir la camara")
    exit()

# Intervalo de detección en segundos
detection_interval = 5
last_detection_time = 0

while cap.isOpened():
    success, frame = cap.read()
    if not success:
        print("Error: No se puede leer el frame de la cámara")
        break

    # obtener el tiempo actual
    current_time = time.time()

    # Realizar deteccion de objetos solo si ha pasado el intervalo
    if current_time - last_detection_time > detection_interval:
        last_detection_time = current_time

        # realizar deteccion de objetos
        results = model(frame)

        # inicializar el contador
        person_count = 0

        # Procesar resultados
        for result in results:
            for box in result.boxes:
                x1, y1, x2, y2 = box.xyxy[0]
                conf = box.conf[0]
                cls = box.cls[0]

                if conf > 0.5:  # Umbral de confianza
                    label = model.names[int(cls)]
                    if label == 'person':
                        person_count += 1
                        # Dibujar rectángulo alrededor de la persona
                        cv2.rectangle(frame, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
                        cv2.putText(frame, f'{label} {conf:.2f}', (int(x1), int(y1)-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

        # Enviar el número de personas detectadas a la API
        send_person_count(person_count)
        # Mostrar el número de personas detectadas en la imagen
        cv2.putText(frame, f'Personas detectadas: {person_count}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    # mostra la imagen con las detecciones
    cv2.imshow("smartCrowd 1.0.0", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    continue
cap.release()
cv2.destroyAllWindows()