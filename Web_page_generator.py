"""
WEB PAGE GENERATOR ASSIGNMENT

Gil Furman
May 18 2022
"""
from cProfile import label
import webbrowser
from tkinter import *
from tkinter import filedialog
from numpy import pad

root = Tk()
root.title('Web Generator')
root.geometry("346x640")

# Browse for an existing file to edit
def browse_file():
  global filepath
  filepath = filedialog.askopenfilename()
  ent_txt_box.insert(END,filepath)

# Adds the existing file found to the edit box
def upload_to_edit():
  file_text = open(filepath, 'r')
  s = file_text.read()
  my_edit_box.insert(END,s)
  ent_txt_box.delete(0,'end')

# Save changes to the file 
def Save_change():
  html_file = open('new_file.html', 'w')
  html_file.write(my_edit_box.get(1.0, END))

# Open the html file in the browser
def open_to_browser():
    webbrowser.get('C:/Program Files/Google/Chrome/Application/chrome.exe %s').open_new_tab('file:///C:/Users/Gil/Documents/Tech%20Acadeny/Python-Projects/new_file.html')

# Label button and entry for Search for existing html file
lbl_browse = Label(root, text='Search for existing html file --->')
lbl_browse.grid(row=0,column=0, padx=(0,0),pady=(10,10))
btn_browse = Button(root, width=12, height=1, text='Browse', command=browse_file)
btn_browse.grid(row=0,column=1, padx=(0,0),pady=(10,10))
ent_txt_box = Entry(root,width=50, text="")
ent_txt_box.grid(row=1,column=0, columnspan=2, padx=(0,0),pady=(10,10))

# label and button for upload existing html file for edit 
lbl_upload = Label(root, text='Upload the file for edit  --->')
lbl_upload.grid(row=2,column=0, padx=(0,0),pady=(10,10))
btn_upload_file = Button(root, width=12, height=1, text='Upload', command=upload_to_edit)
btn_upload_file.grid(row=2,column=1,padx=(0,0),pady=(10,10))

# Editor box
my_edit_box = Text(root, width=40, height=20 )
my_edit_box.grid(row=4,column=0, rowspan=3, columnspan=2, padx=(10,10),pady=(10,10))

# Label and button for open in brwoser
lbl_open_browser = Label(root, text='Open to the brwoser -->')
lbl_open_browser.grid(row=8,column=0, padx=(0,0),pady=(10,10))
btn_open_on_browser = Button(root, width=12, height=1, text='To browser', command= open_to_browser)
btn_open_on_browser.grid(row=8,column=1,padx=(10,10),pady=(10,10))

# button for saving changes
btn_save_changes = Button(root, width=12, height=1, text='Save', command= Save_change)
btn_save_changes.grid(row=9,column=0,padx=(10,10),pady=(10,10))

# Button for closing the window
btn_close_program = Button(root, width=12, height=1, text='Close', command= root.destroy)
btn_close_program.grid(row=9,column=1,padx=(10,10),pady=(10,10))

root.mainloop()
