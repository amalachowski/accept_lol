from email.mime import image
import bot
import threading

import tkinter
from PIL import Image, ImageTk


def main_app():
   
   
    root= tkinter.Tk()

    root.title("Auto accept")

    canvas=tkinter.Canvas(root , height=700,width=480)
    canvas.grid(columnspan=3,rowspan=6)

    frame=tkinter.Frame(root,bg="white")

    #logo
    logo = Image.open("media/ikona3.png")
    logo= ImageTk.PhotoImage(logo)
    logo_label= tkinter.Label(image= logo)
    logo_label.image= logo
    logo_label.grid(column=1,row=0,)

    #button_start
    start_text=tkinter.StringVar()
    start_buttton= tkinter.Button(root,textvariable=start_text,command=lambda:threading.Thread(target=bot.accept_game).start(), bg="black",fg="white",height=2,width=15)
    start_buttton.grid(column=1,row=1)
    start_text.set("Start")
    #button_stop
    stop_text=tkinter.StringVar()
    stop_buttton= tkinter.Button(root,textvariable=stop_text, bg="black",command=lambda:bot.stop_loop(), fg="white",height=2,width=15)
    stop_buttton.grid(column=1,row=2)
    stop_text.set("Stop")
    #button_exit
    exit_text=tkinter.StringVar()
    exit_buttton= tkinter.Button(root,textvariable=exit_text,command=lambda:bot.button_exit(), bg="black",fg="white",height=2,width=15)
    exit_buttton.grid(column=1,row=3)
    exit_text.set("Exit")
    
    
    
    root.mainloop()

if __name__== "__main__":
    #print("Running....")
    main_app()
    









#canvas.pack()

