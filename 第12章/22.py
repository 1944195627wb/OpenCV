#凸缺陷
#convexityDefects = cv2.convexityDefects(contour,convexhull)
import cv2
img = cv2.imread("D:/photo/hand.png",0)
cv2.imshow("original",img)
ret,binary =cv2.threshold(img,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(binary,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
cnt = contours[0]
hull = cv2.convexHull(cnt,returnPoints=False)
defects = cv2.convexityDefects(cnt,hull)
print("defects=\n",defects)
for i in range(defects.shape[0]):
    s,e,f,d = defects[i,0]
    start = tuple(cnt[s,0])
    end =tuple(cnt[e][0])
    far =tuple(cnt[f][0])
    cv2.line(img,start,end,[255,0,255],2)
    cv2.circle(img,far,5,[255,255,0],-1)
cv2.imshow("result",img)
cv2.waitKey()
cv2.destroyAllWindows()