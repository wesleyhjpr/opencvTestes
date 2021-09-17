import cv2

# -----------------------------------------
# img = cv2.imread("Resources/clown-world.jpg")
#
# cv2.imshow("Clown", img)
#
# cv2.waitKey(5000)
# -----------------------------------------

frameWidth = 640
frameHeight = 360

cap = cv2.VideoCapture("Resources/Escape_From_Tarkov.mp4")
# cap = cv2.VideoCapture(0)

# cap.set(3,frameWidth)
# cap.set(4,frameWidth)

while True:
    success,img = cap.read()
    # img = cv2.resize(img, (frameWidth, frameHeight))
    cv2.imshow("Video", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
