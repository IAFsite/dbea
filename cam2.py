
import cv2
import sys
import random

SHADES = " ░▒▓█"
SHADES = "█"
WIDTH = 200
NOISE = 0

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam gagal dibuka!")
    sys.exit()

while True:
    ret, frame = cap.read()

    if not ret:
        break

    # BGR -> RGB
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    h, w, _ = frame.shape

    height = max(
        1,
        int(h / w * WIDTH * 0.45)
    )

    frame = cv2.resize(
        frame,
        (WIDTH, height),
        interpolation=cv2.INTER_AREA
    )

    output = []

    for row in frame:
        line = ""

        for pixel in row:

            r, g, b = map(int, pixel)

            # Noise
            if NOISE:
                r += random.randint(-NOISE, NOISE)
                g += random.randint(-NOISE, NOISE)
                b += random.randint(-NOISE, NOISE)

            r = max(0, min(255, r))
            g = max(0, min(255, g))
            b = max(0, min(255, b))

            # Intensitas berdasarkan brightness
            brightness = max(r, g, b)

            index = (
                brightness *
                (len(SHADES) - 1)
                // 255
            )

            char = SHADES[index]

            # ANSI true color
            line += (
                f"\033[38;2;{r};{g};{b}m"
                f"{char}"
            )

        output.append(line)

    sys.stdout.write("\033[H")
    sys.stdout.write("\n".join(output))
    sys.stdout.flush()

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()

# Reset warna terminal
sys.stdout.write("\033[0m")
