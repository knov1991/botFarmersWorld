from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from time import sleep
from datetime import datetime
#import numpy as np
#import random
#import keyboard
#import pyautogui

#########################
#####   VARIÁVEIS   #####
#########################
totalFerramentas = 5
memberWood = 2
memberGold = 0
memberFood = 2
membership = memberGold+memberWood+memberFood

#############################
#####   GOOGLE CHROME   #####
#############################
options = Options()
options.add_experimental_option("debuggerAddress", "127.0.0.1:10001")
driver = webdriver.Chrome(options=options)

########################
#####   FUNÇÔES    #####
########################
def telaHome():
    try:
        home = driver.find_element(By.CLASS_NAME, "container__header--tilte").text
        return home
    except:
        return 'error'

def verificarGold():
    try:
        valorGold = driver.find_elements(By.CLASS_NAME, "resource-number")[0].text
        return int(float(valorGold))
    except:
        return 0
def verificarWood():
    try:
        valorWood = driver.find_elements(By.CLASS_NAME, "resource-number")[1].text
        return int(float(valorWood))
    except:
        return 0
def verificarFood():
    try:
        valorFood = driver.find_elements(By.CLASS_NAME, "resource-number")[2].text
        return int(float(valorFood))
    except:
        return 0
def verificarEnergia():
    try:
        getEnergia = driver.find_elements(By.CLASS_NAME, "resource-number")[3].text
        valorEnergia = getEnergia.split('/')
        return int(valorEnergia[0])
    except:
        return 0
def maxEnergia():
    try:
        getEnergia = driver.find_elements(By.CLASS_NAME, "resource-number")[3].text
        valorEnergia = getEnergia.split('/')
        return int(valorEnergia[1])
    except:
        return 0


def nomeFerramenta():
    try:
        nome = driver.find_element(By.CLASS_NAME, "info-title-name").text
        return nome
    except:
        return 'error'
def stackFarm():
    try:
        valorStack = driver.find_element(By.CLASS_NAME, "info-title-level").text
        return int(valorStack[0])
    except:
        return 0
def durabilidade():
    try:
        valorDurabilidade = driver.find_element(By.CLASS_NAME, "card-number")
        getDurability = valorDurabilidade.find_element(By.CLASS_NAME, "content").text
        durability = getDurability.split('/')
        return int(durability[0])
    except:
        return 0

def trocarFerramenta(numeroFerramenta):
    try:
        btnTroca = driver.find_elements(By.CLASS_NAME, "carousel__img--item")[numeroFerramenta]
        driver.execute_script("arguments[0].click();", btnTroca)
    except:
        return

def clickMinerar(ferramenta):
    try:
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),'- Minerar', ferramenta)
        btnMinerar = driver.find_elements(By.CLASS_NAME, "button-section")[0]
        driver.execute_script("arguments[0].click();", btnMinerar)
    except:
        return
def clickReparar():
    try:
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),'- Reparar Ferramenta')
        btnReparar = driver.find_elements(By.CLASS_NAME, "button-section")[1]
        driver.execute_script("arguments[0].click();", btnReparar)
    except:
        return


def minerar():
    try:
        nome = nomeFerramenta()
        stack = stackFarm()
        """ if nome == 'Saw':
            if durabilidade() < 15*(1+memberWood*2):
                clickReparar()
                sleep(20)
            if stack == 1+(memberWood*2):
                clickMinerar('Saw')
                sleep(20) """
        if nome == 'Chainsaw':
            if durabilidade() < 45*(1+memberWood*2):
                clickReparar()
                sleep(20)
            if stack == 1+(memberWood*2):
                clickMinerar('Chainsaw')
                sleep(20)
        if nome == 'Mining Excavator':
            if durabilidade() < 5*(1+memberGold*2):
                clickReparar()
                sleep(20)
            if stack == 1+(memberGold*2):
                clickMinerar('Mining Excavator')
                sleep(20)
    except:
        return

def recarregaEnergia(qtdClicks):
    try:
        print(datetime.now().strftime('%d/%m/%Y %H:%M:%S'),'- Recarregar Energia')
        btnEnergia = driver.find_element(By.CLASS_NAME, "resource-energy--plus")
        driver.execute_script("arguments[0].click();", btnEnergia)
        sleep(2)
        modal = driver.find_element(By.CLASS_NAME, "modal-body")
        btnPlus = modal.find_elements(By.CLASS_NAME, "image-button")[1]
        for i in range(int(qtdClicks)):
            driver.execute_script("arguments[0].click();", btnPlus)
            sleep(0.05)
        sleep(1)
        modalRecarregar = driver.find_element(By.CLASS_NAME, "modal-close-button")
        btnRecarregar = modalRecarregar.find_element(By.CLASS_NAME, "button-section")
        driver.execute_script("arguments[0].click();", btnRecarregar)
        sleep(5)
    except:
        return


#########################
#####   INICIAR BOT #####
#########################
print('BOT INICIADO!\n'+
    'Gold:'+str(verificarGold()),
    'Wood:'+str(verificarWood()),
    'Food:'+str(verificarFood()),
    'Energia:'+str(verificarEnergia())
 )

while True:
    for i in range(totalFerramentas):
        trocarFerramenta(i)
        sleep(2)
        #Recarregar Energia
        if verificarEnergia() < 300:
            energiaFaltando = maxEnergia() - verificarEnergia()
            if int(verificarFood())*5 > energiaFaltando:
                recarregaEnergia(energiaFaltando/5)
        #Minerar
        sleep(3)
        minerar()