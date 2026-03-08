# 🤖 Robotic Hand Control via Computer Vision (TCC)

This project consists of a high-fidelity robotic hand controlled in real-time by human gestures. The system bridges the gap between software-based artificial intelligence and physical mechanical motion.

---

## 🛠️ The Tech Stack

### 💻 Software Layer (The "Brain")
*   **Python:** The core programming language.
*   **OpenCV:** Used for image processing and camera feed management.
*   **MediaPipe:** A cross-platform framework for hand landmark detection. It tracks **21 key points** on the human hand to calculate finger angles.
*   **Pyserial:** Used to establish a high-speed communication link between Python and the Arduino.

### 🔌 Hardware Layer (The "Body")
*   **Arduino:** Acts as the microcontroller processing PWM signals.
*   **Servo Motors:** High-torque motors for individual finger articulation.
*   **Protoboarding & Circuitry:** Organized electrical layout for power distribution to the servos.
*   **External Power Supply:** To ensure stable current for multiple motors under load.

---

## 🚀 How it Works

1.  **Detection:** The camera captures the hand; **MediaPipe** identifies the XYZ
