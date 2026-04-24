"""
main.py
Script principal — captura imagem da webcam, detecta landmarks da mão
via MediaPipe e envia comandos para os servos da mão robótica.
"""
import cv2
import mediapipe as mp
import servo_braco3d as mao
import math

# ====== Inicialização da câmera ======
cap = cv2.VideoCapture(0)
if not cap.isOpened():
    print("❌ Erro ao abrir a câmera. Verifique conexões e permissões.")
    exit()
else:
    print("✅ Câmera funcionando corretamente!")

cap.set(3, 640)
cap.set(4, 480)

# ====== MediaPipe Hands ======
hands = mp.solutions.hands
Hands = hands.Hands(max_num_hands=1)
mpDraw = mp.solutions.drawing_utils

pulso_antigo = None

try:
    while True:
        success, img = cap.read()
        frameRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        results = Hands.process(frameRGB)
        handPoints = results.multi_hand_landmarks
        h, w, _ = img.shape
        pontos = []

        if handPoints:
            for points in handPoints:
                mpDraw.draw_landmarks(img, points, hands.HAND_CONNECTIONS)
                for id, cord in enumerate(points.landmark):
                    cx, cy = int(cord.x * w), int(cord.y * h)
                    cv2.circle(img, (cx, cy), 4, (255, 0, 0), -1)
                    pontos.append((cx, cy))

            if pontos:
                # === Cálculo das distâncias entre articulações ===
                distPolegar  = abs(pontos[17][0] - pontos[4][0])
                distIndicador = pontos[5][1]  - pontos[8][1]
                distMedio    = pontos[9][1]  - pontos[12][1]
                distAnelar   = pontos[13][1] - pontos[16][1]
                distMinimo   = pontos[17][1] - pontos[20][1]

                # === Aciona os servos com base nas distâncias ===
                mao.abrir_fechar(10, int(distPolegar  >= 80))
                mao.abrir_fechar(9,  int(distIndicador >= 1))
                mao.abrir_fechar(8,  int(distMedio    >= 1))
                mao.abrir_fechar(7,  int(distAnelar   >= 1))
                mao.abrir_fechar(6,  int(distMinimo   >= 1))

                # === Detecção do movimento do pulso ===
                x1, y1 = pontos[0]  # WRIST
                x2, y2 = pontos[9]  # base do dedo médio
                dx = x2 - x1
                dy = y2 - y1
                angulo_rad = math.atan2(dy, dx)
                angulo_graus = math.degrees(angulo_rad)
                print("Ângulo do pulso:", round(angulo_graus, 2))

                if angulo_graus > -60:
                    mao.abrir_fechar(5, 1)
                elif angulo_graus < -80:
                    mao.abrir_fechar(5, 0)

        cv2.imshow('Imagem', img)
        if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
            break

except KeyboardInterrupt:
    print("⛔ Execução interrompida manualmente.")

finally:
    cap.release()
    cv2.destroyAllWindows()
    mao.board.exit()
    print("✅ Comunicação encerrada com segurança.")
