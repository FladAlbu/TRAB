import cv2 as cv
import numpy as np 

### Alterar depois como será o repositório da imagem
imagem = cv.imread("images/seilaoq.png")

#Alteração de cores para tons de cinza, assim diminui todo o processamento
nuvemGray = cv.cvtColor(imagem,cv.COLOR_BGR2GAY)

# CROP
crop = imagem[yIni:yFim,xIni:XFim]

# RESIZE
height, width, bpp = np.shape(imagem)

#DIMINUI A FIGURA
resizeMin = cv2.resize(imagem, (width/2, height/2))
#DOBRA O TAMANHO DA FIGURA UTILIZANDO O INTERPOLATION PARA TER UMA MELHORIA
resizeMax = cv2.resize(imagem, (width*2, height*2), interpolation=cv.INTER_CUBIC)

#PERSEPECTIVA -> 
rows,cols, ch = imagem.shape

pts1 = np.float32([[56,65],[368,52],[28,387],[389,390]])
pts2 = np.float32([[0,0],[300,0],[0,300],[300,300]])
M = cv.getPerspectiveTransform(pts1,pts2)
dst = cv.warpPerspective(img,M,(300,300))


#ROTATION
rows,cols = img.shape[imagem]
#M = np.float32([[1,0,5],[0,1,5]])
#dst = cv2.warpAffine(img,M,(cols,rows))
M = cv2.getRotationMatrix2D((cols/2,rows/2),180,1)
dst = cv2.warpAffine(img,M,(cols,rows))


cv.imshow("ImagemGray", nuvemGray)
cv.imshow("Camiseta", imagem)
cv2.imshow("Rezise:", res)
cv2.imshow("Rezise:", img)
cv.imshow("Perspective", dst)
cv2.imshow('img',dst)

cv.waitKey(0)
cv.destroyALLWindows()
