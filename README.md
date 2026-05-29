# GRA BIM-to-Reality Alignment — Indoor AR

Graduate Research Assistant project under Dr. Srijeet Halder, Kennesaw State University (2026)

## Project Overview

Automated BIM-to-reality alignment for indoor AR using instance segmentation and reinforcement learning.

## Pipeline

Stage 1 - Coarse Localization: YOLOv26 instance segmentation detects architectural elements (doors, walls, columns). Object matching narrows location to a 10cm x 10cm x 45 degree grid.

Stage 2 - Fine Localization: SAC reinforcement learning agent makes iterative pose corrections until precisely aligned.

## Tools

Python, OpenCV, NumPy, ultralytics YOLOv26, stable-baselines3 SAC, Roboflow, Pandas

## Progress

- [x] Environment setup
- [x] YOLO detection test
- [ ] YOLO segmentation on indoor images
- [ ] Roboflow labeling
- [ ] Model training
- [ ] RL environment setup
- [ ] SAC training
