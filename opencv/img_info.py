import numpy as np
import cv2

img = cv2.imread('./opencv/test.jpg')

if img is None:
    print('img read error')
else:
    print('img type : ',type(img))
    print('img.shape : ',img.shape)
    print('img.dtype : ',img.dtype)
    print('img.size : ',img.size)

    #cv2.imshow('test',img)

    #cv2.waitKey()
    #cv2.destroyAllWindows()
