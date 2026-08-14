import cv2
import sys
import random

SHADES = " ░▒▓█"
SHADES = " .:-=+*#%@"
WIDTH = 1000
NOISE = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam gagal dibuka!")
    sys.exit()

# 0.5 = kompensasi aspect ratio karakter terminal
while True:
    ret, frame = cap.read()

    if not ret:
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    h, w = gray.shape
    height = max(1, int(h / w * WIDTH * 0.45))

    gray = cv2.resize(
        gray,
        (WIDTH, height),
        interpolation=cv2.INTER_AREA
    )

    output = []

    for row in gray:
        line = ""

        for pixel in row:
            # Tambahkan noise
            pixel = int(pixel) + random.randint(-NOISE, NOISE)
            pixel = max(0, min(255, pixel))

            index = pixel * (len(SHADES) - 1) // 255
            line += SHADES[index]

        output.append(line)

    # Pindahkan cursor ke awal tanpa clear
    sys.stdout.write("\033[H")
    sys.stdout.write("\n".join(output))
    sys.stdout.flush()

    # Q untuk keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()