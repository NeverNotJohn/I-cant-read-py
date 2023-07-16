from makeMP3 import createMP3
import dearpygui.dearpygui as dpg



def main():
    
    dpg.create_context()
    dpg.create_viewport(title='I can\'t read', width=1000, height=1000)

    with dpg.window(label="I can't read", width=1000, height=1000):
        dpg.add_text("Hello, world")
        dpg.add_button(label="Save")
        dpg.add_input_text(label="string", default_value="Quick brown fox")
        dpg.add_slider_float(label="Volume", default_value=50, max_value=100)



        dpg.setup_dearpygui()
        dpg.show_viewport()
        dpg.start_dearpygui()
        dpg.destroy_context()
    
    
    
    """ Debug """
    
    # createMP3("Test", 200, 1.0, 1)

if __name__ == "__main__":
    main()