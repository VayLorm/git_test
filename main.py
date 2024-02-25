import dearpygui.dearpygui as dpg
import pygame

def close_viewport(sender, app_data):
    dpg.stop_dearpygui()

def get_input_text(sender, app_data, user_data):
    text = dpg.get_value(sender)
    print(f"text: {text}\nsender: {sender}\napp_data: {user_data}")

pygame.init()
size = pygame.display.get_desktop_sizes()[0]

width = size[0]
height = size[1]

dpg.create_context()

with dpg.font_registry():
    with dpg.font("C:/fonts/SourceCodePro-VariableFont.ttf", 20) as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

with dpg.window(label="Tutorial"):
    dpg.add_checkbox(label="Radio Button1", source="bool_value")
    dpg.add_checkbox(label="Radio Button2", source="bool_value")

    dpg.add_input_text(label="Text Input 1", source="string_value")
    dpg.add_input_text(label="Text Input 2", source="string_value", password=True)
    
    dpg.add_button(label="Close", callback=close_viewport)

dpg.create_viewport(title='MXmanager', 
                    width=width, 
                    height=height, 
                    resizable=False, 
                    always_on_top=True, 
                    decorated=False, 
                    x_pos=0, 
                    y_pos=0, 
                    disable_close=True,
                    clear_color=(0, 100, 0, 255))

dpg.setup_dearpygui()
dpg.show_viewport()
dpg.start_dearpygui()
dpg.destroy_context()
