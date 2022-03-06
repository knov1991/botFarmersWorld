# https://www.classicgame.com/game/Whack+a+Mole

#imports
import cv2
import pyautogui
from time import sleep
from datetime import datetime
import random

#Contador de Farm
farmStoneAxe = 0
farmFishingRod = 0
#Contador de Reparo
repairStoneAxe = 0
repairFishingRod = 0


#template and dimensions
home = cv2.imread('imagens/home.png')
home_gray = cv2.cvtColor(home, cv2.COLOR_RGB2GRAY)
home_w, home_h = home_gray.shape[::-1]
#template and dimensions
mine = cv2.imread('imagens/mine.png')
mine_gray = cv2.cvtColor(mine, cv2.COLOR_RGB2GRAY)
mine_w, mine_h = mine_gray.shape[::-1]
#template and dimensions
login = cv2.imread('imagens/login.png')
login_gray = cv2.cvtColor(login, cv2.COLOR_RGB2GRAY)
login_w, login_h = login_gray.shape[::-1]
#template and dimensions
ok = cv2.imread('imagens/ok.png')
ok_gray = cv2.cvtColor(ok, cv2.COLOR_RGB2GRAY)
ok_w, ok_h = ok_gray.shape[::-1]
#template and dimensions
acabouCpuNet = cv2.imread('imagens/acabouCpuNet.png')
acabouCpuNet_gray = cv2.cvtColor(acabouCpuNet, cv2.COLOR_RGB2GRAY)
acabouCpuNet_w, acabouCpuNet_h = acabouCpuNet_gray.shape[::-1]
#template and dimensions
waxWalletAccount = cv2.imread('imagens/waxWalletAccount.png')
waxWalletAccount_gray = cv2.cvtColor(waxWalletAccount, cv2.COLOR_RGB2GRAY)
waxWalletAccount_w, waxWalletAccount_h = waxWalletAccount_gray.shape[::-1]
#template and dimensions
stoneAxe = cv2.imread('imagens/stoneAxe.png')
stoneAxe_gray = cv2.cvtColor(stoneAxe, cv2.COLOR_RGB2GRAY)
stoneAxe_w, stoneAxe_h = stoneAxe_gray.shape[::-1]
#template and dimensions
repair = cv2.imread('imagens/repair.png')
repair_gray = cv2.cvtColor(repair, cv2.COLOR_RGB2GRAY)
repair_w, repair_h = repair_gray.shape[::-1]
#template and dimensions
btnX = cv2.imread('imagens/btnX.png')
btnX_gray = cv2.cvtColor(btnX, cv2.COLOR_RGB2GRAY)
btnX_w, btnX_h = btnX_gray.shape[::-1]



# Resolução que sera usada na screenshot
x, y, w, h = 400, 240, 1200, 700

#wait
sleep(5)

def resetMouse():
    pyautogui.moveTo(960,280)
    sleep(1)

def screenshot():
    #screenshot
    pyautogui.screenshot('imagens/image.png', (x, y, w, h))
    image = cv2.imread('imagens/image.png')
    #show what the computer sees
    image_mini = cv2.resize(
        src = image,
        dsize = (450,350) #must be integer, not float
    )
    cv2.imshow('vision', image_mini)
    cv2.waitKey(10)
    image_gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    return image_gray

#Função de procurar imagem
def findImage(imagem_gray):
    result = cv2.matchTemplate(
            image = screenshot(),
            templ = imagem_gray,
            method = cv2.TM_CCOEFF_NORMED
        )
    return result

#Função LOGIN
def logar():
    resetMouse()
    #Procura a imagem Login para conectar no jogo
    result = findImage(login_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        pyautogui.click(
            x = max_loc[0] + x, #screen x
            y = max_loc[1] + y  #screen y
        )
        sleep(5)
    resetMouse()
    #Procura a imagem WaxWalletAccount para conectar no jogo
    result = findImage(waxWalletAccount_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        pyautogui.click(
            x = max_loc[0] + x, #screen x
            y = max_loc[1] + y  #screen y
        )
        sleep(5)

def reiniciarJogo():
    resetMouse()
    #Procura a imagem AcabouCpuNet para resetar pagina e iniciar login
    result = findImage(acabouCpuNet_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        pyautogui.press('f5')
        sleep(5)


def verificarDurabilidade():
    global repairStoneAxe, repairFishingRod
    resetMouse()
    #Verifica durabilidade do Stone Axe
    result = findImage(stoneAxe_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.9: # acima de 0.9 // o valor 1/100 desejado as vezes é confundido com 7/100 quando deixa >= 0.8
        sleep(1)
        #Conserta Ferramentas
        result = findImage(repair_gray)
        min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
        if max_val >= 0.8:
            pyautogui.click(
                x = max_loc[0] + x, #screen x
                y = max_loc[1] + y  #screen y
            )
            repairStoneAxe += 1
            now = datetime.now()
            current_time = now.strftime("%H:%M:%S")
            print(current_time,'Reparo Stone Axe:', repairStoneAxe)
            #Esperar após reparar ferramenta - evitar bugs
            sleep(15)


def fecharJanela():
    resetMouse()
    #Procura a imagem de fechar janela
    result = findImage(btnX_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        #Se tiver que fechar janela, dar refresh na pagina - evitar bugs
        pyautogui.press('f5')
        sleep(5)

#Minerar - utiliza pause largo para evitar bugs ~30segundos
def minerar():
    global farmStoneAxe, farmFishingRod
    resetMouse()
    #Procura a imagem Mine para minerar recurso
    result = findImage(mine_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        randMine = random.randint(2,5)
        sleep(randMine)
        pyautogui.click(
            x = max_loc[0] + x, #screen x
            y = max_loc[1] + y  #screen y
        )
        farmStoneAxe += 1
        now = datetime.now()
        current_time = now.strftime("%H:%M:%S")
        print(current_time,'Farms Stone Axe:', farmStoneAxe)
        #Esperar após minerar - evitar bugs
        sleep(15)

    resetMouse()
    #Procura a imagem Ok para confirmar recurso minerado
    result = findImage(ok_gray)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    if max_val >= 0.8:
        pyautogui.click(
            x = max_loc[0] + x, #screen x
            y = max_loc[1] + y  #screen y
        )
        sleep(5)

while True:
    rand = random.randint(1,5)
    #Chama função de login
    logar()
    #Chama função de reiniciar jogo
    reiniciarJogo()
    #Verifica durabilidade das ferramentas
    verificarDurabilidade()
    #Chama função de minerar
    minerar()
    
    #Sleep de 1~5 segundos no fim da execução
    sleep(rand)
    fecharJanela()

    if cv2.waitKey(1) == ord('q'):
        cv2.destroyAllWindows()
        break


