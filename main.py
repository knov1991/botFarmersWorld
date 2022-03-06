import pyautogui
from time import sleep
from procuraCoordenadas import procuraCoordenadas, verificaStackFarm
from random import randint
from datetime import datetime


######################
### FUNÇÕES DO BOT ###
######################
def procuraClick(alvo):
    sleep(0.5)
    pyautogui.moveTo(960,150)
    sleep(0.5)
    btnAlvo = procuraCoordenadas(alvo)
    if(btnAlvo):
        pyautogui.moveTo(btnAlvo)
        sleep(0.5)
        pyautogui.click()
        sleep(3)
        return True

#########################
### INICIAR VARIÁVEIS ###
#########################

maxFarm = 5 #maxFarm ideal = 3x qtd de ferramentas
farmAtual = 0


#######################
##### INICIAR BOT #####
#######################
while True:
    sleep(randint(10,15))

    #Logar no jogo
    if(procuraClick('login') == True):
        sleep(3)
    if(procuraClick('waxWalletAccount') == True):
        sleep(10)

    #minerar e esperar alguns segundos
    if(verificaStackFarm('3stackMinerar') == True):
        if(procuraClick('mine') == True):
            sleep(10)
    #qndo farmar aumentar contador de farm
    if(procuraClick('ok') == True):
        farmAtual += 1
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),'- Total Minerado:',farmAtual)
        sleep(0.5)

    if(procuraClick('acabouCpuNet') == True):
        pyautogui.moveTo(960,150)
        sleep(0.5)
        pyautogui.click()
        sleep(0.5)

    #se farmAtual passar do maxFarm // refresh na página
    if(farmAtual > maxFarm):
        farmAtual = 0
        pyautogui.moveTo(960,150)
        sleep(0.5)
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),'- Refresh Página')
        pyautogui.click()
        pyautogui.press('f5')