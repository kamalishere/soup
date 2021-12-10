# import dearpygui.dearpygui as dpg

# dpg.create_context()

# with dpg.window(label="Window"):
#     with dpg.table(header_row=False):

#         # use add_table_column to add columns to the table,
#         # table columns use child slot 0
#         dpg.add_table_column()
#         dpg.add_table_column()
#         dpg.add_table_column()

#         # add_table_next_column will jump to the next row
#         # once it reaches the end of the columns
#         # table next column use slot 1
#         for i in range(0, 4):
#             with dpg.table_row():
#                 for j in range(0, 3):
#                     dpg.add_text(f"Row{i} Column{j}")

# dpg.create_viewport(title='Custom Title', width=800, height=10)
# dpg.setup_dearpygui()
# dpg.show_viewport()
# dpg.start_dearpygui()
# dpg.destroy_context()

# 
import dearpygui.dearpygui as dpg
from src.node_editor import NodeEditor

dpg.create_context()
dpg.create_viewport(title="Node Editor Template",
                    width=1500,
                    height=768)


def callback_close_program(sender, data):
    exit(0)


def callback_show_debugger(sender, data):
    dpg.show_debug()


with dpg.font_registry():
    default_font = dpg.add_font("fonts/OpenSans-Regular.ttf", 15)


with dpg.viewport_menu_bar():
    dpg.add_menu_item(label="Debugger", callback=callback_show_debugger)
    dpg.add_menu_item(label="Close", callback=callback_close_program)
    dpg.bind_font(default_font)

    nodeEditor = NodeEditor()


# Main Loop
dpg.show_viewport()
dpg.setup_dearpygui()
dpg.start_dearpygui()
dpg.destroy_context()
