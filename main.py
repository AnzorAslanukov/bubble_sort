import random
import tkinter as tk
import test
import time

# Initial tkinter setup for GUI
root = tk.Tk()
root.geometry('704x480')

# Contains label which shows generated array
upper_frame = tk.Frame(root,
                       height=100,
                       width=704)
upper_frame.pack()
# Contains label which shows sorting of generated array
middle_frame = tk.Frame(root,
                        height=180,
                        width=704).pack()
middle_frame.pack()
# Contains GUI controls
lower_frame = tk.Frame(root,
                       height=200,
                       width=704)
lower_frame.pack()

# Label showing generated array
generated_array_label = tk.Label(upper_frame, text="Something")
generated_array_label.pack()

# Wrap-up of GUI
root.title('Bubble Sort')
root.mainloop()
