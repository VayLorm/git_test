import dearpygui.dearpygui as dpg
import pygame
import time

class UserInputData:
    def __init__(self):
        self.first_input_text = ""
        self.second_input_text = ""

def close_viewport(sender, app_data):
    dpg.stop_dearpygui()

def get_user_inputs(sender, app_data):
    inputs_data = app_data["inputs"]
    first_input_text = inputs_data.first_input_text
    second_input_text = inputs_data.second_input_text
    
    # Вывод результата или любые другие действия с текстом
    print(f'First input text: {first_input_text}')
    print(f'Second input text: {second_input_text}')

def update_app_data(sender, app_data):
    inputs_data = app_data['inputs']
    new_input_values = {}

    for child_id in sender.children:
        control_type = dpg.get_value_converted(child_id, dpg.mvItemType.MV_ITEM_TYPE_USER_DEFINED)
        if control_type == 'input_text':
            value = dpg.get_value(child_id)
            new_input_values[control_type + str(child_id)] = value

    inputs_data.update(new_input_values)

pygame.init()
size = pygame.display.get_desktop_sizes()[0]

width = size[0]
height = size[1]

dpg.create_context()

with dpg.font_registry():
    with dpg.font("C:/fonts/SourceCodePro-VariableFont.ttf", 20) as font1:
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Default)
        dpg.add_font_range_hint(dpg.mvFontRangeHint_Cyrillic)

app_data = {"inputs": UserInputData()}

with dpg.window(label="Example Window", height=500, width=800, min_size=(500, 300)):
    dpg.add_text("Enter two strings:")
    first_input_id = dpg.add_input_text(label="String 1", default_value="Quick brown fox")
    second_input_id = dpg.add_input_text(label="String 2", default_value="Lazy dog")
    dpg.add_button(label="Show Inputs", callback=get_user_inputs, user_data=app_data)
    dpg.bind_item_user_data(first_input_id, app_data, "inputs.first_input_text")
    dpg.bind_item_user_data(second_input_id, app_data, "inputs.second_input_text")
    dpg.set_item_callback(first_input_id, update_app_data)
    dpg.set_item_callback(second_input_id, update_app_data)

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
