import cv2

img = cv2.imread("solar-system.jpg")
cv2.putText(img,
            "Sun",
            (70,60),
            cv2.FONT_HERSHEY_COMPLEX,
            1,
            (0,0,255))
cv2.putText(img,
            "Mercury",
            (100,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,255,255)) 
cv2.putText(img,
            "Venus",
            (190,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,0,255))
cv2.putText(img,
            "Earth",
            (290,160),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (205,205,0)) 
cv2.putText(img,
            "Mars",
            (390,180),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (255,205,205)) 
cv2.putText(img,
            "Jupiter",
            (550,50),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (200,0,250))
cv2.putText(img,
            "Saturn",
            (750,120),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (0,250,0)) 
cv2.putText(img,
            "Uranus",
            (960,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (200,250,0)) 
cv2.putText(img,
            "Pluto",
            (1130,140),
            cv2.FONT_HERSHEY_COMPLEX,
            0.5,
            (200,210,0))                                                                            
cv2.imshow("output",img)  
cv2.imwrite("Solar_systemwithname.jpg",img)         
cv2.waitKey(0)