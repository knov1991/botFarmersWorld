import pyautogui

max = 5

lista = list(range(1, max+1))

print(lista)

for i in lista:
    pyautogui.screenshot('test'+str(i)+'.png')
    print(i)
    i+=1