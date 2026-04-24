"""
servo_braco3d.py
Módulo de controle dos servos da mão robótica via pyfirmata.

Mapeamento de pinos (Arduino UNO):
  pin1 = 10 → Polegar
  pin2 =  9 → Indicador
  pin3 =  8 → Médio
  pin4 =  7 → Anelar
  pin5 =  6 → Mínimo
  pinPulso = 5 → Pulso
"""
from pyfirmata import Arduino, SERVO
import time

board = Arduino('COM9')

pin1 = 10  # Polegar
pin2 = 9   # Indicador
pin3 = 8   # Médio
pin4 = 7   # Anelar
pin5 = 6   # Mínimo
pinPulso = 5  # Pulso

# Configura todos os pinos como SERVO
for pino in (pinPulso, pin1, pin2, pin3, pin4, pin5):
    board.digital[pino].mode = SERVO


def rotateServo(pino, angle):
    """Envia comando PWM para rotacionar o servo no pino indicado."""
    board.digital[pino].write(angle)
    time.sleep(0.05)


def abrir_fechar(pin, on_off):
    """
    Abre (on_off=1) ou fecha (on_off=0) o dedo correspondente ao pino.
    Ângulos diferentes para polegar (pin 10) e indicador (pin 9)
    devido à montagem mecânica dos tendões.
    """
    if on_off == 1:
        rotateServo(pin, 0)
    elif on_off == 0 and pin != 10 and pin != 9:
        rotateServo(pin, 140)
    elif on_off == 0 and pin == 10:
        rotateServo(pin, 150)
    elif on_off == 0 and pin == 9:
        rotateServo(pin, 180)


def testeTodos():
    """Rotina de teste — abre e fecha cada dedo individualmente."""
    for pin in (pin1, pin2, pin3, pin4, pin5):
        rotateServo(pin, 0)
    time.sleep(1)

    for pin, ang in [(pin1, 150), (pin2, 130), (pin3, 130), (pin4, 130), (pin5, 130)]:
        rotateServo(pin, ang)
        time.sleep(1)
        rotateServo(pin, 0)
        time.sleep(1)
    time.sleep(2)
