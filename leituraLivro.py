import pytesseract as ocr
import numpy as np
import cv2


from PIL import Image

imagem = Image.open('livro1  .jpg').convert('RGB')

npimagem =np.asarray(imagem).astype(np.uint8)

npimagem[:, :, 0] = 0
npimagem[:, :, 2] = 0

im = cv2.cvtColor(npimagem, cv2.COLOR_RGB2GRAY) 


ret, thresh = cv2.threshold(im, 127, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

binimagem = Image.fromarray(thresh)

phrase = ocr.image_to_string(binimagem, lang = 'por')

print(phrase)