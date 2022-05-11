# PYTHON COURSE
# DATABASE SUBMISSION ASSIGNMENT
# The Tech Academy Coding Bootcamp
# Author: Gil Furman
# Mat 5 2022

import sqlite3
from tkinter import N
# list of file names to use for this assignment
fileList = ('information.dock','hello.txt','myImage.png','myMovie.mpg','World.txt','data.pdf','myPhoto.jpg')

# determine only the files from the list which end with a “.txt” file extension.
file_txt = ()
for file in fileList:
  if file.endswith("txt"):
    file_txt +=  (file, )

# Creating a  database, with 2 fields: an auto-increment primary integer field and a field with the data type “string.”
conn = sqlite3.connect('Data_Base_Submission.db')
with conn:
  cur = conn.cursor()
  cur.execute("CREATE TABLE IF NOT EXISTS tbl_txt_files ( \
    ID INTEGER PRIMARY KEY AUTOINCREMENT, \
    text_files TEXT \
    )")
  conn.commit()
conn.close()

# Inserting the file names  with a “.txt” file extension.
conn = sqlite3.connect('Data_Base_Submission.db')
with conn:
  cur = conn.cursor()
  for i in file_txt:
    cur.execute("INSERT INTO tbl_txt_files(text_files) VALUES ($s)", [i])
  conn.commit()
conn.close()

# Selecting and printing the qualifying text files to the console.
conn = sqlite3.connect('Data_Base_Submission.db')
with conn:
  cur = conn.cursor()
  cur.execute("SELECT ID, text_files FROM tbl_txt_files")
  var_text_file = cur.fetchall()
  for item in var_text_file:
    print(item)
   
