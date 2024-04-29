import os

file_path =r'C:\Users\busin\OneDrive\Desktop\Reading Notes hst 100\Reading Notes\Week 1 Notes.docx'

print(file_path)

if os.path.isfile(file_path):
    os.remove(file_path)
    print("File has successfully been deleted!")
else:
    print("This file does not exist!!!")
