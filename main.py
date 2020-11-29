import tkinter as tk
import test


'''
FRAMES
'''

# Initial tkinter setup for GUI
root = tk.Tk()

# Contains label which shows generated array
upper_frame = tk.Frame(root,
                       bg='pink')
upper_frame.pack()
# Contains label which shows sorting of generated array
middle_frame = tk.Frame(root,
                        bg='turquoise')
middle_frame.pack()
# Contains GUI controls
lower_frame = tk.Frame(root,
                       bg='grey')
lower_frame.pack()

'''
IMAGE OBJECTS
'''

test_img = tk.PhotoImage(file='static/images/test_label_img.png')

'''
LABELS
'''

# Title label for "generated_array_label"
generated_array_title_label = tk.Label(upper_frame,
                                       anchor='center',
                                       text='Generated Array',
                                       bg='blue',
                                       padx=2,
                                       pady=2,
                                       relief='raised',
                                       font=('Arial', 22, 'bold'),
                                       image=test_img)
generated_array_title_label.pack(fill=tk.X,
                                 pady=5)

# Label showing generated array
generated_array_label = tk.Label(upper_frame,
                                 anchor='center',
                                 text='Something',
                                 bg='red',
                                 padx=2,
                                 pady=2,
                                 relief='sunken',
                                 font=('Arial', 22))
generated_array_label.pack(fill=tk.X,
                           pady=5)

# Title label for scrollbar Listbox with sorted arrays
scrollbar_title_label = tk.Label(middle_frame,
                                 anchor='center',
                                 text='Sorted Array',
                                 bg='yellow',
                                 relief='raised',
                                 font=('Arial', 22, 'bold'))
scrollbar_title_label.pack(fill=tk.X,
                           pady=5)

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

# Wrap-up of GUI
root.title('Bubble Sort')
root.mainloop()
