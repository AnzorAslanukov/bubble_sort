import random
import tkinter as tk
import test
import time

# Initial tkinter setup for GUI
root = tk.Tk()
root.geometry('704x480')

# Frame setup for labels
# upper_frame contains label with generated array
# lower frame contains label showing incremental changes to sorted array
upper_frame = tk.Frame(root).pack()
lower_frame = tk.Frame(root).pack()

# Label showing generated array
gen_arr_lbl = tk.Label(upper_frame, text='Something', bg='red')
gen_arr_lbl.config(width=75)
gen_arr_lbl.pack()

# Set text for sorted_arr_lbl
sorted_arr_lbl = tk.Label(lower_frame, text='')
sorted_arr_lbl.pack()

test_list = test.list_of_lists
expanding_var = ''
for list in test_list:
    expanding_var += str(list) + '\n'
    sorted_arr_lbl['text'] = expanding_var
    time.sleep(.5)

# Wrap-up of GUI
root.title('Bubble Sort')
root.mainloop()
