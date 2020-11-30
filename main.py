import tkinter as tk
import test
import random

'''
Random Array
'''


# Generates a random array of "arr_len" length
def random_arr_gen():
    arr_len = int(arr_length_entry.get())
    random_arr = []
    for i in range(0, arr_len):
        random_arr.append(random.randint(0, 100))

    generated_array_label['text'] = random_arr

    return random_arr


'''
Frames
'''

# Initial tkinter setup for GUI
root = tk.Tk()

# Contains label which shows generated array
upper_frame = tk.Frame(root)
upper_frame.pack()
# Contains label which shows sorting of generated array
middle_frame = tk.Frame(root)
middle_frame.pack(fill=tk.X)
# Contains GUI controls
lower_frame = tk.Frame(root)
lower_frame.pack()

'''
Labels
'''

# Title label for "generated_array_label"
generated_array_title_label = tk.Label(upper_frame,
                                       anchor='center',
                                       text='Generated Array',
                                       padx=2,
                                       pady=2,
                                       font='Arial')
generated_array_title_label.pack(fill=tk.X,
                                 pady=5)

# Label showing generated array
generated_array_label = tk.Label(upper_frame,
                                 anchor='center',
                                 text='Something',
                                 padx=2,
                                 pady=2,
                                 relief='sunken',
                                 font='Arial')
generated_array_label.pack(fill=tk.X,
                           pady=5)

# Title label for scrollbar Listbox with sorted arrays
scrollbar_title_label = tk.Label(middle_frame,
                                 anchor='center',
                                 text='Sorted Array',
                                 font='Arial')
scrollbar_title_label.pack(fill=tk.X,
                           pady=5,
                           padx=80)

# Scrollbar object for sorted array
array_scrollbar = tk.Scrollbar(middle_frame)
array_scrollbar.pack(fill=tk.Y, side='right')

# Listbox object showing sorted array
array_listbox = tk.Listbox(middle_frame,
                           yscrollcommand=array_scrollbar.set)
for index in range(0, len(test.list_of_lists)):
    array_listbox.insert(index, test.list_of_lists[index])
array_listbox.pack(fill=tk.X)
array_scrollbar.config(command=array_listbox.yview)

# Int input title label for list length
int_length_title = tk.Label(lower_frame,
                            text='Choose Array Length \n'
                                 '(Value between 2 & 50)')
int_length_title.pack(fill=tk.X)

# Error message label
error_label = tk.Label(lower_frame,
                       text='Error')

'''
Text Input 
'''

arr_length_entry = tk.Entry(lower_frame)
arr_length_entry.pack()

'''
Button
'''

start_button = tk.Button(lower_frame,
                         text='Start',
                         command=random_arr_gen)
start_button.pack()

# Wrap-up of GUI
root.title('Bubble Sort')
root.mainloop()
