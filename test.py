import dearpygui.dearpygui as dpg
dpg.create_context()

dpg.create_viewport()

dpg.setup_dearpygui()
def save_callback():
    print(" Clicked")
 
with dpg.window(label="Example Window",width=600,height=700):
    b0 = dpg.add_button(label="button   0")
    dpg.add_text("hello this")
    dpg.add_button(label="save",callback=save_callback)
    # dpg.add_input_text(label="enter name",name="password",on_enter='True',callback=save_callback)
    dpg.add_button(tag="btn1",label="button 1")

# print(b0)
dpg.show_viewport()

dpg.start_dearpygui()

dpg.destroy_context()

