import cv2
import sys

WIDTH = 400

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Webcam gagal dibuka!")
    sys.exit()


def render_rgb(r, g, b):
    return (
        # RED
        f"\033[38;2;{r};0;0m█"

        # GREEN
        f"\033[38;2;0;{g};0m█"

        # BLUE
        f"\033[38;2;0;0;{b}m█"
    )


while True:

    ret, frame = cap.read()

    if not ret:
        break

    # BGR → RGB
    frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    h, w, _ = frame.shape

    # Karena setiap pixel dibuat 2 lane
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

        lane1 = ""
        lane2 = ""

        for pixel in row:

            r, g, b = map(int, pixel)

            rgb = render_rgb(r, g, b)

            # Lane pertama
            lane1 += rgb

            # Lane kedua
            lane2 += rgb

        output.append(lane1)
        output.append(lane2)

    # Kembali ke pojok kiri atas
    sys.stdout.write("\033[H")

    sys.stdout.write(
        "\n".join(output)
    )

    sys.stdout.flush()

    # Q = keluar
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break


cap.release()
cv2.destroyAllWindows()

sys.stdout.write("\033[0m")