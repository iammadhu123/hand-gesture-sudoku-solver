import streamlit as st
import cv2

st.title("Hand Gesture Sudoku Solver")

run = st.checkbox("Start Camera")

FRAME_WINDOW = st.image([])

cap = cv2.VideoCapture(0)

while run:
    ret, frame = cap.read()
    if not ret:
        break

    # your processing here (mediapipe + sudoku)
    
    FRAME_WINDOW.image(frame, channels="BGR")

cap.release()