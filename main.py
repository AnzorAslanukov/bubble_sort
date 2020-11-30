import tkinter as tk
import random

'''
Random Array
'''


# Generates a random array of "arr_len" length
def random_arr_gen():
    len_input = arr_length_entry.get()
    if len_input.isnumeric() and 2 <= int(len_input) <= 20:
        error_label.pack_forget()
        error_label_desc.pack_forget()
        arr_len = int(arr_length_entry.get())
        random_arr = []

        for i in range(0, arr_len):
            random_arr.append(random.randint(0, 100))
        generated_array_label['text'] = random_arr

        for x in range(0, len(random_arr)):
            for j in range(0, len(random_arr) - 1):
                if random_arr[j] > random_arr[j + 1]:
                    temp_var = random_arr[j]
                    random_arr[j] = random_arr[j + 1]
                    random_arr[j + 1] = temp_var

        sorted_arr_lbl['text'] = random_arr

    else:
        error_label.pack()
        error_label_desc.pack(pady=5)
        generated_array_label['text'] = ''
        sorted_arr_lbl['text'] = ''


'''
Frames
'''

# Initial tkinter setup for GUI
root = tk.Tk()

# Contains label which shows generated array
upper_frame = tk.Frame(root)
upper_frame.pack(padx=10)
# Contains label which shows sorting of generated array
middle_frame = tk.Frame(root)
middle_frame.pack(padx=10,
                  fill=tk.X)
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
                                       font='Arial',
                                       width=60)
generated_array_title_label.pack(fill=tk.X,
                                 pady=5)

# Label showing generated array
generated_array_label = tk.Label(upper_frame,
                                 anchor='center',
                                 text='',
                                 padx=2,
                                 pady=2,
                                 relief='sunken',
                                 font='Arial')
generated_array_label.pack(fill=tk.X,
                           pady=5)

# Title label for sorted array
sorted_arr_title = tk.Label(middle_frame,
                            text='Sorted Array',
                            font='Arial')
sorted_arr_title.pack(fill=tk.X)

# Label for sorted array
sorted_arr_lbl = tk.Label(middle_frame,
                          text='',
                          relief='sunken',
                          font='Arial')
sorted_arr_lbl.pack(fill=tk.X)

# Int input title label for list length
int_length_title = tk.Label(lower_frame,
                            text='Choose Array Length \n'
                                 '(Value between 2 & 50)')
int_length_title.pack(pady=5,
                      fill=tk.X)

# Error message label
error_label = tk.Label(lower_frame,
                       text='ERROR')
error_label_desc = tk.Label(lower_frame,
                            text='Characters must be\n'
                            'integers between 1 and 21')

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
start_button.pack(pady=5)

# Wrap-up of GUI
root.title('Bubble Sort')
root.mainloop()
