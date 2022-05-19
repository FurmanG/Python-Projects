"""
FILE TRANSFER ASSIGNMENT

Gil Furman
May 19 2022
"""

from tkinter import *
import tkinter as tk
from tkinter import filedialog
import shutil
import os
import schedule
import time

win = Tk()
win.title('File Transfer')
win.geometry("360x400")

# Open folder to be check daily
def get_from_folder():
  global folder_to_check
  folder_to_check = filedialog.askdirectory()
  txt_name_1.insert(END,folder_to_check)

# Open folder to send files daily
def send_to_folder():
  global folder_to_send
  folder_to_send = filedialog.askdirectory()
  txt_name_2.insert(END,folder_to_send)
  
# move files from folder to folder
def move_files():
  source = folder_to_check.replace('C:','') + '/'
  destination = folder_to_send.replace('C:','') + '/'
  files = os.listdir(source)
  for i in files:
    if i[-3:] == 'txt':
      shutil.move(source+i, destination)

# Once per day,  files are sent to the home office. 
def on_off_auto(On_the_run):
  schedule.every(86400).seconds.do(move_files)  
  while On_the_run:
    schedule.run_pending()
    time.sleep(1)

# Choose a folder to be checked daily.
lbl_browse_1 = Label(win, text='choose a folder that will contain the files to be checked daily:')
lbl_browse_1.grid(row=0,column=0, padx=(10,0),pady=(10,0), sticky=W)
btn_browse_1 = tk.Button(win, width=12, height=1, text='Browse', command=get_from_folder)
btn_browse_1.grid(row=1,column=0,padx=(10,0),pady=(10,0),sticky=W)
txt_name_1 = tk.Entry(win,text="")
txt_name_1.grid(row=2,column=0, padx=(10,10),pady=(10,10),sticky=W)
txt_name_1.config(width=40)

# Choose a folder for sending files daily.
lbl_browse_2 = Label(win, text='choose a folder that will receive the files:')
lbl_browse_2.grid(row=3,column=0, padx=(10,0),pady=(10,0),sticky=W)
btn_browse_2 = tk.Button(win, width=12, height=1, text='Browse', command=send_to_folder)
btn_browse_2.grid(row=4,column=0,padx=(10,0),pady=(10,0),sticky=W)
txt_name_2 = tk.Entry(win,text="")
txt_name_2.grid(row=5,column=0, padx=(10,10),pady=(10,10),sticky=W)
txt_name_2.config(width=40)

# Transfer files to the other folder
btn_browse_3 = tk.Button(win, width=12, height=1, text='Move files', command=move_files)
btn_browse_3.grid(row=6,column=0,padx=(10,0),pady=(10,0),sticky=W)

# On /Off automated file send
btn_Auto_on = tk.Button(win, width=12, height=1, text='Set Auto On', command=lambda: on_off_auto((True)))
btn_Auto_on.grid(row=7,column=0,padx=(10,0),pady=(10,0),sticky=W)
btn_Auto_off = tk.Button(win, width=12, height=1, text='Set Auto Off', command=lambda: on_off_auto((False)))
btn_Auto_off.grid(row=8,column=0,padx=(10,0),pady=(10,0),sticky=W)

# Close windo buttom
btn_close_program = tk.Button(win, width=12, height=2, text='Close Window', command= win.destroy)
btn_close_program.grid(row=10,column=0,padx=(10,10),pady=(10,10),sticky=E)

win.mainloop()


