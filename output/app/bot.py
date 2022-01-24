
from tkinter.font import BOLD
import pyautogui



import pyautogui


def accept_game():
    global run_start1
    run_start1= True
    pyautogui.alert("Czekanie na rozgrywke")
    while run_start1== True:
        pos =pyautogui.locateCenterOnScreen('przyjmij4.png')
       
        #print(pos)

        if not pos == None:
            pyautogui.click(pos)
            pyautogui.alert("Zaakceptowano mecz")
        elif not pyautogui.locateCenterOnScreen("koniec.png")== None or not pyautogui.locateCenterOnScreen("koniec2.png")==None or not pyautogui.locateCenterOnScreen("flash.png")==None :
            #print(pyautogui.locateCenterOnScreen("koniec.png"))
            stop_loop()
            pyautogui.alert("Serio ?? Yasuo !")


def stop_loop():
    global run_start1
    run_start1=False
    #print("Koniec oczekiwania")
    pyautogui.alert("Program zakonczyl oczekiwanie")

def button_exit():
    stop_loop()
    exit()
    
            
            
    

 

    



