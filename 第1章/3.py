#等待按键 retval = cv2.waitKey([delay])delay 等待按键触发时间单位是ms，负数或者0为无限等待
#没按键按下 返回-1 如果有按键按下 返回ASCII码
import cv2
img = cv2.imread("D:/photo/1.png")
cv2.imshow("img",img)
key = cv2.waitKey()
if key == ord('A'):
    cv2.imshow("PressA",img)
elif key == ord('B'):
    cv2.imshow("PressB",img)