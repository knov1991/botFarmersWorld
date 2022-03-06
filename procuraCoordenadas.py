import cv2
from time import sleep
from printMonitor import printMonitor

def procuraCoordenadas(imagemAlvo):

    printMonitor()
    image = cv2.imread('./images/image.png')#, cv2.COLOR_BGR2GRAY)
    imgAlvo = cv2.imread('./images/'+imagemAlvo+'.png')#, cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.85
    #Primeira comparação pra pegar coordenadas das contas
    res = cv2.matchTemplate(image, imgAlvo, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val > threshold):
        return max_loc
    else:
        return None


def verificaStackFarm(imagemAlvo):

    printMonitor()
    image = cv2.imread('./images/image.png')#, cv2.COLOR_BGR2GRAY)
    imgAlvo = cv2.imread('./images/'+imagemAlvo+'.png')#, cv2.COLOR_BGR2GRAY)
    method = cv2.TM_CCOEFF_NORMED
    threshold = 0.95
    #Primeira comparação pra pegar coordenadas das contas
    res = cv2.matchTemplate(image, imgAlvo, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    if(max_val > threshold):
        return True
    else:
        return None