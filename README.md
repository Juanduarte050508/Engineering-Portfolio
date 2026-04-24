<div align="center">

# Engineering Portfolio

**Selected mechatronics and engineering projects by Juan Duarte Moura**

[![Python](https://img.shields.io/badge/Python-1F2937?style=flat-square&logo=python&logoColor=3776AB)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C++-1F2937?style=flat-square&logo=cplusplus&logoColor=00599C)](https://isocpp.org/)
[![OpenCV](https://img.shields.io/badge/OpenCV-1F2937?style=flat-square&logo=opencv&logoColor=5C3EE8)](https://opencv.org/)
[![Arduino](https://img.shields.io/badge/Arduino-1F2937?style=flat-square&logo=arduino&logoColor=00979D)](https://www.arduino.cc/)
[![Fusion 360](https://img.shields.io/badge/Fusion_360-1F2937?style=flat-square&logo=autodesk&logoColor=FF6F00)](https://www.autodesk.com/products/fusion-360/)

</div>

---

## Overview

This repository hosts two engineering projects developed during my Mechatronics technical degree at ETEC Horácio Augusto da Silveira (2024–2025). Together, they cover the full spectrum from mechanical design and aerodynamics to embedded systems and computer vision.

| Project | Field | Stack |
|---|---|---|
| [Robotic Hand via Computer Vision](#1-robotic-hand-via-computer-vision-tcc) | Robotics, Embedded, CV | Python, OpenCV, MediaPipe, Arduino, C++ |
| [F1 in Schools — Rise 5](#2-f1-in-schools--rise-5-equipe-allset) | Mechanical Engineering, CFD | Fusion 360, CFD, 3D Printing, CNC |

---

## 1. Robotic Hand via Computer Vision (TCC)

> **Capstone project (TCC) — Mechatronics Technical Degree, 2025**

A robotic hand controlled in real time by a webcam. Python detects human hand landmarks via OpenCV/MediaPipe and translates finger positions into PWM signals sent to an Arduino, which drives 5 servo motors mounted on the prosthetic structure.

### Architecture

```
Webcam → OpenCV → MediaPipe (21 landmarks)
                       ↓
              Finger angle calculation (Python)
                       ↓
              Serial (USB) → Arduino → 5 servos → Robotic hand
```

### Highlights

- **Real-time tracking** of all 5 fingers with sub-100ms latency
- **Custom angle-mapping algorithm** that converts landmark distances into servo angles, compensating for hand orientation
- **3D-printed mechanical structure** designed in Fusion 360
- **Direct precursor to VisuAll** — the same MediaPipe landmark approach was later expanded into the Libras recognition system

### Tech Stack

`Python` · `OpenCV` · `MediaPipe` · `Arduino C++` · `PySerial` · `Fusion 360` · `3D Printing`

📂 **[View project files →](./robotic-hand-computer-vision)**

---

## 2. F1 in Schools — Rise 5 (Equipe Allset)

> **Role: Assistant Engineer / Fusion 360 Designer · 2024**

The **Rise 5** is a CO2-powered prototype car developed by Equipe Allset for the F1 in Schools international competition. My role focused on aerodynamic surface modeling and CFD analysis.

### Highlights

- **43 design iterations** before reaching the final body geometry
- **CFD simulations** to optimize aerodynamic drag coefficient
- **Full project lifecycle**: ideation → CAD → simulation → CNC machining → 3D printing → final assembly
- Project management artifacts: **WBS (Work Breakdown Structure)** and budget control

### Tech Stack

`Autodesk Fusion 360` · `CFD (Fluid Dynamics)` · `CNC Machining` · `3D Printing` · `Technical Drawing`

📂 **[View project files →](./F1-in-Schools-Alset-Brasil)**

---

## Skills Demonstrated

| Category | Skills |
|---|---|
| **Design / CAD** | Fusion 360, surface modeling, technical drawing, prototyping |
| **Simulation** | CFD (aerodynamics), basic FEA (stress analysis) |
| **Programming** | Python (OpenCV, MediaPipe, PySerial), C++ (Arduino) |
| **Electronics** | Servo control, PWM, breadboarding, basic circuit design |
| **Manufacturing** | 3D printing (FDM), CNC awareness, assembly |
| **Project Management** | WBS, budgeting, technical documentation |

---

## About the author

**Juan Duarte Moura** — Software Engineering student at FIAP (class of 2030) and certified Mechatronics Technician. Currently working on [VisuAll](https://github.com/Juanduarte050508/VisuAll), a real-time Libras recognition system.

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=flat-square&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/juan-duarte-moura/)
[![GitHub](https://img.shields.io/badge/GitHub-Profile-1F2937?style=flat-square&logo=github&logoColor=white)](https://github.com/Juanduarte050508)

---

<sub>*"Bridging the gap between mechanical engineering, embedded systems, and software."*</sub>
