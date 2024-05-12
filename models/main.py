import cv2
import face_recognition

# Inicializa a webcam
video_capture = cv2.VideoCapture(0)

# Verifica se a câmera foi aberta corretamente
if not video_capture.isOpened():
    print("Erro ao abrir a câmera.")
    video_capture.release()
    cv2.destroyAllWindows()
    exit()

# Loop principal
while True:
    ret, frame = video_capture.read()
    if not ret:
        print("Falha ao capturar imagem da câmera.")
        continue

    # Converte a imagem capturada de BGR para RGB
    rgb_frame = frame[:, :, ::-1]

    # Encontra os locais dos rostos detectados na imagem
    face_locations = face_recognition.face_locations(rgb_frame)

    # Calcula os encodings dos rostos detectados
    face_encodings = face_recognition.face_encodings(rgb_frame, face_locations)

    # Processa cada rosto detectado
    for (top, right, bottom, left), face_encoding in zip(face_locations, face_encodings):
        # Desenha um retângulo ao redor de cada rosto detectado
        cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)

    # Exibe a imagem resultante
    cv2.imshow('Webcam Face Detection', frame)

    # Pressione 'q' para sair do loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Libera a câmera e fecha todas as janelas abertas
video_capture.release()
cv2.destroyAllWindows()
