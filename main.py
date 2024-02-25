import customtkinter
import os
from PIL import Image

customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("blue")  # Themes: blue (default), dark-blue, green
customtkinter.set_widget_scaling(0.8)

class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("POGInstaller")
        self.geometry("1280x720")

        self.grid_rowconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)


        assets = os.path.join(os.path.dirname(os.path.realpath(__file__)), "assets")
        self.logo = customtkinter.CTkImage(Image.open(os.path.join(assets, "poggers.webp")), size=(26, 26))


        self.nav = customtkinter.CTkFrame(self, corner_radius=0)
        self.nav.grid(row=0, column=0, sticky="nsew")
        self.nav.grid_rowconfigure(4, weight=1)

        self.nav_label = customtkinter.CTkLabel(self.nav, text="  POGInstaller", image=self.logo,
                                                             compound="left", font=customtkinter.CTkFont(size=15))
        self.nav_label.grid(row=0, column=0, padx=20, pady=20)


        self.home_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="Активация",
                                                   fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                   anchor="w")
        self.home_button.grid(row=1, column=0, sticky="ew")

        self.about_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="(Кратко) О программе",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w")
        self.about_button.grid(row=2, column=0, sticky="ew")

        self.credits_button = customtkinter.CTkButton(self.nav, corner_radius=0, height=40, border_spacing=10, text="Разработчики",
                                                      fg_color="transparent", text_color=("gray10", "gray90"), hover_color=("gray70", "gray30"),
                                                      anchor="w")
        self.credits_button.grid(row=3, column=0, sticky="ew")


        self.appearance_mode_label = customtkinter.CTkLabel(self.nav, text="Appearance Mode:", anchor="w")
        self.appearance_mode_label.grid(row=5, column=0, padx=20, pady=(10, 0))
        self.appearance_mode_optionemenu = customtkinter.CTkOptionMenu(self.nav, values=[ "System", "Light", "Dark"],
                                                                       command=self.change_appearance_mode_event)
        self.appearance_mode_optionemenu.grid(row=6, column=0, padx=20, pady=(10, 10))

        self.scaling_label = customtkinter.CTkLabel(self.nav, text="UI Scaling:", anchor="w")
        self.scaling_label.grid(row=7, column=0, padx=20, pady=(10, 0))
        self.scaling_optionemenu = customtkinter.CTkOptionMenu(self.nav, values=["80%", "90%", "100%", "110%", "120%", "Режим бабушки"],
                                                               command=self.change_scaling_event)
        self.scaling_optionemenu.grid(row=8, column=0, padx=20, pady=(10, 20))

    def change_appearance_mode_event(self, new_appearance_mode: str):
        customtkinter.set_appearance_mode(new_appearance_mode)

    def change_scaling_event(self, new_scaling: str):
        match new_scaling:
            case "Режим бабушки":
                new_scale = 2
            case _:
                new_scale = int(new_scaling.replace("%", "")) / 100
        
        customtkinter.set_widget_scaling(new_scale)

if __name__ == "__main__":
    app = App()
    app.mainloop()