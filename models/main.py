import cv2
import face_recognition

# Inicializa a webcam
video_capture = cv2.VideoCapture(0)

# Loop principal
while True:
    ret, frame = video_capture.read()
    if not ret:
        continue

    # Converte a imagem de BGR para RGB (necessário para face_recognition)
    rgb_frame = frame[:, :, ::-1]

    # Encontra todos os rostos no frame atual
    face_locations = face_recognition.face_locations(rgb_frame)

    # Verifica o número de rostos detectados
    if len(face_locations) == 2:
        # Desenha retângulos ao redor de cada rosto detectado
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 255, 0), 2)  # Desenha um retângulo verde ao redor dos rostos
    elif len(face_locations) > 2:
        # Mostra uma mensagem de erro se mais de dois rostos forem detectados
        cv2.putText(frame, "Mais de duas faces detectadas, por favor, se posicione em um ambiente mais tranquilo!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    elif len(face_locations) == 1:
        # Mostra uma mensagem pedindo ao usuário para posicionar-se corretamente com o documento
        cv2.putText(frame, "Por favor, posicione-se em frente a câmera e segure seu documento ao lado do rosto!", (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)
    else:
        # Se nenhum rosto for detectado, talvez você queira adicionar uma mensagem aqui
        pass

    # Exibe o frame
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()

